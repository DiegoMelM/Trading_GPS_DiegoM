# -*- coding: utf-8 -*-
"""
Created on Mon Jan 29 18:49:15 2024

@author: d_mel
"""
import Src.Modules.custom_functions as cf

dictionary = cf.read_dict("Input/Data_and_Features")
cf.custom_ploting(dictionary["TSLA"], save_plot= True)

