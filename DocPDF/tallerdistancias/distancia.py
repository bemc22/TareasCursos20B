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

pd.option_context('display.max_rows', None, 'display.max_columns', None)

# load reference data

reference_path = Path('datos/Datos Estaciones AMB.xlsx')
reference_data = pd.read_excel(reference_path, sheet_name="Normal", skiprows=[1], index_col='Date&Time',
                               usecols=['Date&Time', 'PM2.5'])
reference_data['PM2.5'] = reference_data['PM2.5'].apply(lambda x: pd.to_numeric(x, errors='coerce')).dropna()
reference_data.index.name = 'DateTime'
reference_data = reference_data.rename(columns={'PM2.5': 'reference'})

# load measure data

main_measure_path = Path('datos/mediciones')
measure_paths = [main_measure_path / f for f in listdir(main_measure_path) if isfile(join(main_measure_path, f))]

measure_data = []
for measure_path in measure_paths:
    try:
        measure_subdata = pd.read_csv(measure_path, index_col='fecha_hora_med', usecols=['fecha_hora_med', 'valor'])
        measure_subdata.index = pd.to_datetime(measure_subdata.index, format='%Y-%m-%dT%H:%M:%S.%fZ')
        measure_subdata.index = measure_subdata.index.map(lambda t: t.replace(microsecond=0))
        measure_subdata['valor'] = measure_subdata['valor'].apply(lambda x: pd.to_numeric(x, errors='coerce')).dropna()
        measure_subdata.index.name = 'DateTime'
        measure_subdata = measure_subdata.rename(columns={'valor': 'measure'})
        measure_data.append(measure_subdata)
    except:
        print(f'There is not data in {measure_path}')

measure_data = pd.concat(measure_data)

# plot data

ax = measure_data.plot()
reference_data.plot(ax=ax)


# define distance function

def distance(reference, measure):
    return np.sqrt(np.sum((reference - measure) ** 2))


# moving averaging

window = 50
reference_rolling = reference_data.rolling(window=window).mean()
measure_rolling = measure_data.rolling(window=window).mean()

reference_rolling = reference_rolling[-len(measure_rolling):]

ax1 = measure_rolling.plot()
reference_rolling.plot(ax=ax1)

# compute distance

reference_rolling_numpy = reference_rolling.to_numpy()
measure_rolling_numpy = measure_rolling.to_numpy()

reference_rolling_numpy = np.nan_to_num(reference_rolling_numpy)
measure_rolling_numpy = np.nan_to_num(measure_rolling_numpy)

error = distance(reference_rolling_numpy, measure_rolling_numpy)
print(error)

print('Final feliz')
