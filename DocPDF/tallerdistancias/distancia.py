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

measure_path = Path('datos/mediciones/mediciones_clg_normalsup_pm25_a_2018-11-01T00_00_00_2018-11-30T23_59_59.csv')
measure_data = pd.read_csv(measure_path, index_col='fecha_hora_med', usecols=['fecha_hora_med', 'valor'])
measure_data.index = pd.to_datetime(measure_data.index, format='%Y-%m-%dT%H:%M:%S.%fZ')
measure_data['valor'] = measure_data['valor'].apply(lambda x: pd.to_numeric(x, errors='coerce')).dropna()
measure_data.index.name = 'DateTime'
measure_data = measure_data.rename(columns={'valor': 'measure'})

# interleave data

interleave_data = pd.concat([reference_data, measure_data])
interleave_data = interleave_data.sort_index()

interleave_data.plot(), plt.show()

print('Final feliz')
