# -*- coding: utf-8 -*-
"""
Created on Wed Feb 26 12:27:31 2025

@author: vscerra
"""
import numpy as np
import pandas as pd
from scipy.stats import binom_test

def sequential_ab_test(df, alpha = .05):
    """ Implements a sequential A/B testing approach where significance is monitored over time. 
        The test stops early if a significant difference is detected between groups.
        
        Parameters:
        df (pd.DataFrame): A/B test dataset containing 'group' and 'converted' columns
        alpha (float): Significance level for stopping rule
        
        Returns: 
        int: Stopping point (index where test stopped), or None if no significance was reached
        float: Final p-value at stopping point
    """
    
    df = df.sort_values(by = 'timestamp').reset_index(drop = True)
    conversions_A = df[df['group'] == 'A']['converted'].cumsum()
    conversions_B = df[df['group'] == 'B']['converted'].cumsum()
    trials_A = (df['group'] == 'A').cumsum()
    trials_B = (df['group'] == 'B').cumsum()
    
    p_values = []
    stopping_point = None
    
    for i in range(1, len(df)):
        p_value = binom_test(
          [conversions_A.iloc[i], conversions_B.iloc[i]], 
          [trials_A.iloc[i], trials_B.iloc[i]], 
          alternative = 'two-sided')
        
        p_values.append(p_value)
        if p_value < alpha:
            stopping_point = i
            break
          
    print(f"Sequential test stopped at sample {stopping_point} with p_value {p_values[-1]:4f}")
    
    return p_values, stopping_point