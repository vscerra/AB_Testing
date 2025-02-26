# -*- coding: utf-8 -*-
"""
Created on Wed Feb 26 12:03:58 2025

@author: vscerra

Frequentist hypothesis testing of AB testing data (conversion and revenue data)
"""

import pandas as pd
import scipy.stats as stats
import numpy as np

def chi_square_test(df):
    contingency_table = pd.crosstab(df['group'], df['converted'])
    chi2, chi2_p, _, _ = stats.chi2_contingency(contingency_table)
    print(f"\nChi-Square Test for Conversion Rate: Chi2: {chi2}, p-value: {chi2_p}")
    return chi2, chi2_p
  
def t_test_revenue(df):
    revenue_A = df[df['group'] == 'A']['revenue']
    revenue_B = df[df['group'] == 'B']['revenue']
    t_stat, t_test_p = stats.ttest_ind(revenue_A, revenue_B, equal_var = False)
    print(f"\nT-Test for Revenue: T-stat: {t_stat}, p-value: {t_test_p}")
    return t_stat, t_test_p
  
def cohen_d(df):
    revenue_A = df[df['group'] == 'A']['revenue']
    revenue_B = df[df['group'] == 'B']['revenue']
    mean_A, mean_B = revenue_A.mean(), revenue_B.mean()
    std_A, std_B = revenue_A.std(), revenue_B.std()
    pooled_std = np.sqrt(((std_A**2 + std_B**2) / 2))
    d = (mean_B - mean_A) / pooled_std
    print(f"\nEffect Size (Cohen's d): {d}")
    return d
  
  