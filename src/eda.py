# -*- coding: utf-8 -*-
"""
Created on Wed Feb 26 12:00:14 2025

@author: vscerra
"""
import pandas as pd

def exploratory_analysis(df):
    summary = df.groupby('group').agg(
      click_rate = ('click', 'mean'),
      conversion_rate = ('converted', 'mean'),
      avg_revenue = ('revenue', 'mean')
      )
    
    print("Summary Statistics: \n", summary)
    
    return summary