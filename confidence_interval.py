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

weight = np.array([3.142, 3.163, 3.155, 3.150, 3.141])

def confidence_interval(data, confidence=0.95):
    # confidence_interval = margin of error
    # margin of error = z-score * standard deviation / sqrt(n)
    # z-score = 1.96 for 95% confidence
    # z-score = 2.58 for 99% confidence
    
    mean = np.mean(data)
    std = 0.1   # standard deviation for population
    z_score = 1.96 if confidence == 0.95 else 2.58
    confidence_interval = z_score * std / np.sqrt(len(data))
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