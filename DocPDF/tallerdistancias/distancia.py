import os 
import pandas as pd



data_folder = ".\datos"

data_path = os.path.join(data_folder, "Datos Estaciones AMB.xlsx")

df = pd.read_excel (data_path, sheet_name="Normal")
print (df)