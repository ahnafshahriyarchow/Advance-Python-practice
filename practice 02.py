
import numpy as np

def check_run_length(trial_sequence, required_length):
    run_count = 0
    for outcome in trial_sequence:
        if outcome == 1:
            run_count += 1
            if run_count >= required_length:
                return True
        else:
            run_count = 0
    return False

def run_prob(expts, n, k, p):
    trials_matrix = np.random.choice([0, 1], (expts, n), p=(1 - p, p))
    successful_experiments = sum(check_run_length(trial_seq, k) for trial_seq in trials_matrix)
    estimated_probability = successful_experiments / expts
    return estimated_probability