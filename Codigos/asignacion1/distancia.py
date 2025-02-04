# import libraries

import os
from itertools import product
from os import listdir
from os.path import isfile, join

import time
from datetime import datetime
from pathlib import Path

import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns

pd.option_context('display.max_rows', None, 'display.max_columns', None)


# define distance function

def distance(reference, measure):
    return np.sqrt(np.sum((reference - measure) ** 2)) / np.prod(reference.shape)

windows = np.linspace(1, 601, 61).astype(int)[::4]
strides = [1, 2, 4, 6, 8, 10, 12, 14, 16]
type_data = ['no_interpolate', 'interpolate']

# load reference data

reference_path = Path('datos/Datos Estaciones AMB.xlsx')
reference_data = pd.read_excel(reference_path, sheet_name="Normal", skiprows=[1], index_col='Date&Time',
                               usecols=['Date&Time', 'PM2.5'])
reference_data['PM2.5'] = reference_data['PM2.5'].apply(lambda x: pd.to_numeric(x, errors='coerce')).dropna()
reference_data.index.name = 'DateTime'
reference_data = reference_data.rename(columns={'PM2.5': 'reference'})

# load measure data

main_measure_path = Path('datos/mediciones')
measure_paths = [f for f in listdir(main_measure_path) if isfile(join(main_measure_path, f))]
measure_paths = ["mediciones_clg_normalsup_pm25_a_2018-12-01T00_00_00_2018-12-31T23_59_59.csv"]

for measure_path in measure_paths:
    print(f'Evaluating {measure_path}')
    ms_path = main_measure_path / measure_path
    try:
        measure_subdata = pd.read_csv(ms_path, index_col='fecha_hora_med', usecols=['fecha_hora_med', 'valor'])
        measure_subdata.index = pd.to_datetime(measure_subdata.index, format='%Y-%m-%dT%H:%M:%S.%fZ')
        measure_subdata.index = measure_subdata.index.map(lambda t: t.replace(microsecond=0))
        measure_subdata['valor'] = measure_subdata['valor'].apply(lambda x: pd.to_numeric(x, errors='coerce')).dropna()
        measure_subdata.index.name = 'DateTime'
        measure_subdata = measure_subdata.rename(columns={'valor': 'measure'})
        measure_subdata = measure_subdata.sort_index()

        # set range by time

        time_range = (measure_subdata.index.min(), measure_subdata.index.max())
        mask = (reference_data.index > time_range[0]) & (reference_data.index <= time_range[1])
        reference_subdata = reference_data.loc[mask]

        interleave = pd.concat([measure_subdata, reference_subdata])
        interleave = interleave.sort_index()

        # moving average (full range)

        save_path = Path('resultados/resultados actuales')
        (save_path / measure_path).mkdir(exist_ok=True, parents=True)

        distances = []

        # np.linspace(2, len(interleave), 100).astype(int)
        for window, stride, t_data in product(windows, strides, type_data):
            print(f'Window={window}, stride={stride}, t_data={t_data}')
            if t_data == 'interpolate':
                interleave_interpolate = interleave.interpolate(method='linear')
                interleave_rolling = interleave_interpolate.rolling(window=window, min_periods=1).mean()[window::stride]
            else:
                interleave_rolling = interleave.rolling(window=window, min_periods=1).mean()[window::stride]

            D = np.round(distance(interleave_rolling['reference'], interleave_rolling['measure']), 4)
            distances.append([window, stride, t_data, D])
            interleave_rolling.plot()
            plt.title(f'window: {window}, stride={stride}, t_data={t_data}, distance: {D}')
            plt.savefig(f'{save_path / measure_path}/window={window}_stride={stride}_t_data={t_data}.png')
            plt.close('all')

        # plot window vs distance

        table_distances = pd.DataFrame(distances, columns=['window', 'stride', 't_data', 'distance'])
        empty_distances = table_distances.loc[table_distances['t_data'] == 'no_interpolate']
        interpolation_distances = table_distances.loc[table_distances['t_data'] == 'interpolate']

        empty_result = empty_distances.pivot(index='window', columns='stride', values='distance')
        empty_result = empty_result.sort_index(level=0, ascending=False)
        empty_result = empty_result.drop(labels=1)
        interpolation_result = interpolation_distances.pivot(index='window', columns='stride', values='distance')
        interpolation_result = interpolation_result.sort_index(level=0, ascending=False)

        plt.figure(figsize=(7, 7))
        sns.heatmap(empty_result, annot=True, fmt='.2f', cmap='viridis'), plt.title(
            'Distance without interpolation')
        plt.savefig(f'{save_path / measure_path}/performance_not_interpolation.png')

        plt.figure(figsize=(7, 7))
        sns.heatmap(interpolation_result, annot=True, fmt='.2f', cmap='viridis'), plt.title(
            'Distance with interpolation')
        plt.savefig(f'{save_path / measure_path}/performance_interpolation.png')

        plt.close('all')

    except:
        print(f'There is not data in {ms_path}')

print('Final feliz')

