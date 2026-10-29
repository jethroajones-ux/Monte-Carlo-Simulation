import numpy as np
import scipy.stats as si
import matplotlib.pyplot as plt
import scipy.stats as st

S0 = 100
r = 0.05
sigma = 0.20
T = 2
K = 100


def monteCarlo(size_exp):
    z = np.random.normal(loc=0.0, scale=1.0, size=size_exp)
    drift = (r - 1/2 * sigma**2) * T

    ran_com = sigma*np.sqrt(T)*z

    ST = S0 * np.exp(drift+ran_com)

    payoff = np.maximum(ST-K, 0)

    discounted_payoffs = np.exp(-r*T) * payoff

    payoff_std = np.std(discounted_payoffs, ddof=1)

    standard_error = payoff_std / np.sqrt(size_exp)

    CMC = np.exp(-r*T) * np.mean(payoff)

    return CMC, standard_error


def blackScholes():
    d1 = (np.log(S0/K) + (r+1/2*sigma**2) * T)/(sigma*np.sqrt(T))
    d2 = d1 - sigma*np.sqrt(T)

    cdf1 = si.norm.cdf(d1)
    cdf2 = si.norm.cdf(d2)

    CBS = S0*cdf1 - K*np.exp(-r*T)*cdf2
    return CBS


def percentError(size):

    errorsList = []
    CMClist = []
    CBS = blackScholes()
    for i in range(251):
        CMC, standard_error = monteCarlo(size)
        CMClist.append(CMC)
        percErr = (abs(CMC - CBS))/CBS * 100
        errorsList.append(percErr)

    
    STDCMC = np.std(CMClist, ddof=1)
    CMCmean = np.mean(CMClist)
    standard_error = STDCMC / np.sqrt(len(CMClist))
    errorsMean = np.mean(errorsList)
    print(f"Mean: {CMCmean} and Standard Deviation: {STDCMC}")
    print(f"Standard Error: {standard_error}")
    absPercentError = len(errorsList) / len(CMClist)
    max_error = max(errorsList)
    std_dev = np.std(errorsList, ddof=1)
    print(f"Max percent error is {max_error} for sample size {size}")
    print(f"Standard deviation is {std_dev}\n")
    return CMClist


sizes = [100, 1000, 10000, 100000]
ci_widths = []

for size in sizes:
    CMC, standard_error = monteCarlo(size)
    ci = (CMC - 1.96 * standard_error, CMC + 1.96 * standard_error)
    first_val, second_val = ci
    width = second_val - first_val
    print(f"CMC: {CMC}, Sample Size: {size}, 95% Confidence Interval: {ci}, Width: {width}")
    ci_widths.append(width)

plt.plot(sizes, ci_widths, marker='o')

plt.xscale('log')
plt.yscale('log')
plt.xlabel("Sample Size (number of simulations)")
plt.ylabel("95% Confidence Interval Width ($)")
plt.title("Monte Carlo Confidence Interval Width vs. Simulation Count ")
plt.tight_layout()
plt.show()


