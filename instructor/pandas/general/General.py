import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

def exec_load_data_fechas():
  df_fechas = None

  dict_fechas = {
    'fecha1':  ['1980-10-10', '1990-10-11', '2000-10-12'],
    'fecha2':  ['2022-10-10', '2022-10-11', '2022-10-12']
  }

  df_fechas = pd.DataFrame(dict_fechas)

  df_fechas['dias'] = pd.to_datetime(df_fechas['fecha2']) - pd.to_datetime(df_fechas['fecha1'])

  print(df_fechas[['dias','fecha1','fecha2']])


#exec_load_data_fechas()