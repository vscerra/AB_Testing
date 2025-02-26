# -*- coding: utf-8 -*-
"""
Created on Wed Feb 26 12:17:03 2025

@author: vscerra
"""
import numpy as np
from scipy.stats import beta

def bayesian_ab_test(df):
    """
      Implements a Bayesian A/B testing approach where we assume each group's conversion 
      rate follows a beta distribution. We assume uniform weak initial priors (beta(1,1))
      
      The observed data updates our belief about the conversion rates using Bayes' Theorem
      
      After updating with observed conversions, we derive the posterior 
      distributions of conversion rates for both groups
      
      Parameters:
      df (pd.DataFrame): A/B test dataset containing 'group' and 'converted' columns
      
      Returns: 
      float: Final probability that group B has better conversion rates than group A
    """
    conversions_A = df[df['group'] == 'A']['converted'].sum()
    conversions_B = df[df['group'] == 'B']['converted'].sum()
    trials_A = len(df[df['group'] == 'A'])
    trials_B = len(df[df['group'] == 'B'])
    
    alpha_prior, beta_prior = 1, 1
    posterior_A = beta(alpha_prior + conversions_A, beta_prior + trials_A - conversions_A)
    posterior_B = beta(alpha_prior + conversions_B, beta_prior + trials_B - conversions_B)
    
    samples_A = posterior_A.rvs(10000)
    samples_B = posterior_B.rvs(10000)
    prob_B_better_A = np.mean(samples_B > samples_A)
    
    print(f"\nBayesian A/B Test Results: P(B > A): {prob_B_better_A:.4f}")
    
    return prob_B_better_A