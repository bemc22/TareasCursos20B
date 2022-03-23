# import libraries

import os
from os import listdir
from os.path import isfile, join

import time
from datetime import datetime
from pathlib import Path

import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import matplotlib.animation as animation

pd.option_context('display.max_rows', None, 'display.max_columns', None)


# define distance function

def distance(reference, measure):
    return np.sqrt(np.sum((reference - measure) ** 2))


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

for measure_path in measure_paths:
    print(f'Evaluating {measure_path}')
    try:
        ms_path = main_measure_path / measure_path

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

        save_path = Path('resultados')
        (save_path / measure_path).mkdir(exist_ok=True, parents=True)

        distances = []
        window = 15

        interleave_rolling = interleave.rolling(window=window, min_periods=1).mean()[window:]
        D = distance(interleave_rolling['reference'], interleave_rolling['measure'])
        distances.append([window, D])

        y = np.array(interleave_rolling['reference'])
        x = np.array(interleave_rolling['measure'])

        plt.figure()
        interleave_rolling.plot()
        plt.title(f'window: {window}, distance: {np.round(D, 4)}')
        plt.savefig(f'{save_path / measure_path}/comparison.png')

        x = x[:, None]
        y = y[:, None]

        print(x.shape)
        print(y.shape)

        c = (x.T @ y) / (x.T @ x)
        c = np.sum(c)

        recta = lambda x: c * x
        eje_x = np.linspace(np.min(x), np.max(x), 100)
        eje_y = recta(eje_x)

        plt.figure()
        label = r"$f(\epsilon_j) = \alpha \hat{f}(\epsilon_j)$"
        label += f", alpha = {c}"
        plt.plot(eje_x, eje_y, color='red', label=label)
        plt.title('')
        plt.xlabel(r"$\hat{f}(\epsilon_j)$")
        plt.ylabel(r"$f(\epsilon_j)$")
        plt.scatter(x, y, s=4)
        plt.legend()
        plt.savefig(f'{save_path / measure_path}/mse_0.png')

        plt.figure()
        interleave_rolling['calibrated'] = interleave_rolling['measure'].apply(recta)
        calibrated_D = distance(interleave_rolling['reference'], interleave_rolling['calibrated'])
        interleave_rolling.plot()
        plt.title(f'window: {window}, distance: {np.round(D, 4)}, calibrated distance: {np.round(calibrated_D, 4)}')
        plt.savefig(f'{save_path / measure_path}/calibration_train_100_test_0.png')

        # train / test

        for percentage in [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8]:
            n = int(percentage * len(x))
            x_train, x_test = x[:n], x[n:]
            y_train, y_test = y[:n], y[n:]

            print(x_train.shape, x_test.shape)
            print(y_train.shape, y_test.shape)

            c = (x_train.T @ y_train) / (x_train.T @ x_train)
            c = np.sum(c)

            recta = lambda x: c * x
            eje_x = x_test
            y_pred = recta(eje_x)

            plt.figure()
            label = r"$f(\epsilon_j) = \alpha \hat{f}(\epsilon_j)$"
            label += f", alpha = {np.round(c, 4)}"
            plt.plot(eje_x, y_pred, color='red', label=label)
            plt.title('')
            plt.xlabel(r"$\hat{f}(\epsilon_j)$")
            plt.ylabel(r"$f(\epsilon_j)$")
            plt.scatter(x, y, s=4)
            plt.legend()
            plt.savefig(
                f'{save_path / measure_path}/calibration_points_train_{int(100 * percentage)}_test_{int(100 * (1 - percentage))}.png')

            interleave_rolling['calibrated'] = np.concatenate([np.nan * np.zeros_like(x_train), y_pred])
            calibrated_train_D = distance(y_train, recta(x_train))
            calibrated_test_D = distance(y_test, y_pred)
            interleave_rolling.plot(figsize=(20, 10))
            plt.title(f'window: {window}, distance: {np.round(D, 4)}, '
                      f'calibrated train distance: {np.round(calibrated_train_D)}, '
                      f'calibrated test distance: {np.round(calibrated_test_D)}')
            plt.savefig(
                f'{save_path / measure_path}/calibration_train_{int(100 * percentage)}_test_{int(100 * (1 - percentage))}.png')

            plt.close('all')

    except:
        print(f'No se encontró {measure_path}')
