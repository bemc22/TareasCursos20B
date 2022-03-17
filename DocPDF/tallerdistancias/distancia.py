# import libraries

import os
from pathlib import Path

import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

# load data

reference_path = Path('datos/Datos Estaciones AMB.xlsx')
reference_data = pd.read_excel(reference_path, sheet_name="Normal", skiprows=[1])
reference_pm25 = reference_data["PM2.5"]
reference_pm25 = reference_pm25.apply(lambda x: pd.to_numeric(x, errors='coerce')).dropna()

measure_path = Path('datos/mediciones_clg_normalsup_pm25_a_2018-11-01T00_00_00_2018-11-30T23_59_59.csv')
measure_data = pd.read_csv(measure_path)
measure_data = measure_data.sort_values(by='fecha_hora_med', ascending=True)
measure_pm25 = measure_data['valor']
measure_pm25 = measure_pm25.apply(lambda x: pd.to_numeric(x, errors='coerce')).dropna()

# first computation

reference_rolling = reference_pm25.rolling(window=1000).mean()
reference_rolling.plot(), plt.title('reference moving average'), plt.show()
measure_rolling = measure_pm25.rolling(window=1000).mean()
measure_rolling.plot(), plt.title('measure moving average'), plt.show()

interleave_pm25 = pd.concat([reference_pm25, measure_pm25])


print(reference_data["PM2.5"])
