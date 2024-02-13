# -*- coding: utf-8 -*-
"""
Created on Mon Jan 29 18:37:59 2024

@author: d_mel
"""
import pandas as pd
import csv
import os
import mplfinance as mpf
import matplotlib.pyplot as plt

def read_dict (folder_path):
    diccionario = {}
    
    for archivo in os.listdir(folder_path):
        nombre_archivo = os.path.basename(archivo)

        ticker = nombre_archivo.split(".")[0]

        with open(os.path.join(folder_path, archivo), "r") as csvfile:
            lector = pd.read_csv(csvfile).set_index("m_date")

            diccionario[ticker] = lector
    return(diccionario)

def custom_ploting(df_dict, 
                   title= "Gráfica de velas, RSI y MAV", 
                   save_plot= False, 
                   filename= "default_plot.png"):
    db_dict = {
        'c_adjusted_open': 'Open',
        'c_adjusted_high': 'High',
        'c_adjusted_low': 'Low',
        'm_adjusted_close': 'Close',
        'm_volume': 'Volume',
        'm_close': 'Adj Close'
    }
    DF = df_dict.copy().rename(columns = db_dict)
    DF.index = pd.to_datetime(DF.index)
    output_path= "Output/" + filename
    Plot= mpf.plot(DF,
                 volume=True, 
                 title= title, 
                 figsize= (12,6), 
                 mav=(21, 63, 252),
                 addplot= mpf.make_addplot(DF["c_relative_strength_index_14d"], 
                                           panel=2,
                                           ylabel='RSI'),
                 style="mike",
                 savefig= output_path if save_plot else None)
    return Plot
    