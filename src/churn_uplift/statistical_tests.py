import numpy as np

def smd_independent(group_1, group_2):
    """
    We use the Cohen's D (Standardized Mean Differences) in order to 
    evaluate coefficient balance. 
    
    Note that:
    If D < .1 -> The groups are well balanced.
    If .1 < D < .25 -> The groups are moderately imbalanced.
    If D > .25 -> The groups are severely imbalanced.

    """
    mean_1, mean_2 = np.mean(group_1)
    var_1 , var_2 = np.mean(group_2), np.var(group_1, ddof=1), np.var(group_2, ddof=1)
    return (mean_1 + mean_2) / np.sqrt((var_1 + var_2) / 2 )