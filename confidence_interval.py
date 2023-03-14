"""
confidence_interval

An electric scale gives a reading equal to the true weight plus a random error 
that is normally distributed with mean 0 and standard deviation σ = 0.1 mg. 
Suppose that the results of five successive weighings of the same object are as follows
: 3.142, 3.163, 3.155, 3.150, 3.141.

The sample standard deviation:
s = √((Σ(xi - x̄)²) / (n-1))

z-score:
z = (x - μ) / (σ / √n)
"""

import numpy as np
import scipy.stats as stats

weight = np.array([3.142, 3.163, 3.155, 3.150, 3.141])

def confidence_interval(data, confidence=0.95):
    # Determine the confidence interval estimate of the true weight.
    #
    mean = np.mean(data)
    # z-score * standard deviation / sqrt(n)
    confidence_interval = stats.norm.ppf(1 - (1 - confidence) / 2) * np.std(data) / np.sqrt(len(data))
    confidence_interval_lower = mean - confidence_interval
    confidence_interval_upper = mean + confidence_interval
    
    return mean, confidence_interval_lower, confidence_interval_upper

def main():
    for i in (0.95, 0.99):
        mean, lower, upper = confidence_interval(weight, confidence=i)
        print(f"Confidence interval for {i*100}%")
        print(f"Mean: {mean}")
        print(f"Lower: {lower}")
        print(f"Upper: {upper}")
        print("")

if __name__ == "__main__":
    main()