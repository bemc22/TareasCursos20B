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

for measure_path in measure_paths[1:2]:
    print(f'Evaluating {measure_path}')
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



    interleave_rolling.plot()
    plt.title(f'window: {window}, distance: {D}')
    plt.show()
    
    x = x[:, None]
    y = y[:, None]

    c = (x.T@y)/(x.T @ x)
    c = np.sum(c)

    recta = lambda x: c*x
    
    eje_x = np.linspace( np.min(x), np.max(x), 100)

    x_cal = recta(x)

    error = np.sqrt( ( x_cal - y).T @ ( x_cal - y) )
    error = np.sum(error)


    plt.plot(eje_x, recta(eje_x), color='red', label=r"$f(\epsilon_j) = \alpha \hat{f}(\epsilon_j)$")
    plt.xlabel(r"$\hat{f}(\epsilon_j)$")
    plt.ylabel(r"$f(\epsilon_j)$")
    plt.scatter(x, y, s=4, label=r"$(\hat{f}(\epsilon_j), f(\epsilon_j))$")
    plt.title(r"$\alpha=$" + str(round(c,2)))
    plt.legend()
    plt.savefig(f'{save_path / measure_path}/ajustelineal.png')
    plt.close('all')

    plt.plot(x, label='measure')
    plt.plot(y, label='reference')
    plt.plot(x_cal, label='calibrated')
    plt.title("calibration error: " + str(round(error,2)))
    plt.legend()
    plt.savefig(f'{save_path / measure_path}/calibration.png')

    #plt.savefig(f'{save_path / measure_path}/window={window}.png')
    #plt.close('all')

