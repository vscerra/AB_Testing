# -*- coding: utf-8 -*-
"""
Created on Wed Feb 26 11:38:50 2025

@author: vscerra

Load and preprocess AB testing data
""" 
import os
import pandas as pd

def load_data(filename = "ab_test_data.csv"):
    """
    Loads A/B testing dataset from the 'data' folder. 
    If the file is not found, raises an error.
    """
    try:
        base_path = os.path.dirname(os.path.abspath(__file__))  # Running as a script
    except NameError:
        base_path = os.getcwd() # running in Jupyter notebook
      
      
    data_path = os.path.join(os.path.dirname(base_path), "data", filename) # construct full path
    
    if not os.path.exists(data_path):
        raise FileNotFoundError(f"Dataset not found at {data_path}. Please check the file location")
        
    df = pd.read_csv(data_path)
    
    return df