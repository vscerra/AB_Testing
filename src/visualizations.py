# -*- coding: utf-8 -*-
"""
Created on Wed Feb 26 13:14:56 2025

@author: vscerra
"""
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from scipy.stats import beta
from sequential_ab_test import sequential_ab_test


def plot_conversion_rates(df):
    """Charts conversion rates by group"""
    fig, ax = plt.subplots()
    df.groupby('group')['converted'].mean().plot(kind = 'bar', ax=ax, color = ['goldenrod', 'lightseagreen'])
    ax.set_title("Conversion Rate by Group")
    ax.set_ylabel("conversion rate")
    ax.set_xticklabels(ax.get_xticklabels(), rotation=30)  # Rotate x-axis labels
    plt.show()
    
    
def plot_posterior_distributions(df):
    """ plots the posterior distributions for Bayesian A/B testing"""
    conversions_A = df[df['group'] == 'A']['converted'].sum()
    conversions_B = df[df['group'] == 'B']['converted'].sum()
    trials_A = len(df[df['group'] == 'A'])
    trials_B = len(df[df['group'] == 'B'])
    
    posterior_A = beta(1 + conversions_A, 1 + trials_A - conversions_A)
    posterior_B = beta(1 + conversions_B, 1 + trials_B - conversions_B)
    
    samples_A = posterior_A.rvs(10000)
    samples_B = posterior_B.rvs(10000)
    
    plt.figure(figsize = (10, 5))
    plt.hist(samples_A, bins=50, alpha=0.5, label='Group A', density=True, color='goldenrod')
    plt.hist(samples_B, bins=50, alpha=0.5, label='Group B', density=True, color='lightseagreen')
    plt.axvline(samples_A.mean(), color='goldenrod', linestyle= '--', label=f"A mean: {samples_A.mean():3f}")
    plt.axvline(samples_B.mean(), color='lightseagreen', linestyle= '--', label=f"B mean: {samples_B.mean():3f}")

    plt.legend()
    plt.title("Posterior Distributions of Conversion Rates")
    plt.show()
    
def plot_sequential_p_values(df, alpha=0.05):
    """ plots p-values over time for sequential A/B testing"""
    p_values, stopping_point = sequential_ab_test(df)
    plt.figure(figsize=(10,5))
    plt.plot(range(len(p_values)), p_values, label='p-values')
    plt.axhline(y=alpha, color='red', linestyle='--', label='alpha threshold')
    if stopping_point is not None:
        plt.axvline(x=stopping_point, color='blue', linestyle='--', label=f"stopping point ({stopping_point})")
    plt.xlabel('sample number')
    plt.ylabel('p-value')
    plt.title("Sequential A/B Test p-Values Over Time")
    plt.legend()
    plt.show()
    
def generate_visualizations(df=None, alpha=0.05, plot_conversion=True, plot_posterior=True, plot_sequential=True):
    """ Generates selected visualizations based on control variables """
    if plot_conversion and df is not None: 
        plot_conversion_rates(df)
    if plot_posterior and df is not None:
        plot_posterior_distributions(df)
    if plot_sequential and df is not None:
        plot_sequential_p_values(df, alpha)
        
      
        
        
    