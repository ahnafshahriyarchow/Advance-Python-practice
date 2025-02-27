"""
Group Members:
1. SYED ALI JAVED
2. SAMEER UL HAQ
3. AHNAF SHAHRIYAR CHOWDHURY
"""

# My code here

import numpy as np
from collections import defaultdict

def countRuns(trials):
    run_counts = defaultdict(int)
    run_length = 0
    
    for trial in trials:
        if trial == 1:
            run_length += 1
        else:
            if run_length:
                run_counts[run_length] += 1
                run_length = 0
    
    # Checking for any remaining run length after the loop
    if run_length:
        run_counts[run_length] += 1
    
    return dict(run_counts)