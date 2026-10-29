# Monte-Carlo-Simulation
Monte Carlo European Option Pricing Model

Overview

This project implements a Monte Carlo simulation in Python to estimate the theoretical price of a European call option. The simulation uses a geometric Brownian motion model to generate possible future stock prices and estimates the option's value by averaging discounted payoffs across simulated outcomes.

To evaluate the simulation, I compare its estimated prices against the analytical Black–Scholes option-pricing model. I also investigate how simulation size affects estimation error and confidence intervals, and how changes in model parameters affect option prices.

Objectives

Implement a Monte Carlo simulation to estimate European call option prices.

Validate simulated estimates against the analytical Black–Scholes model.

Investigate the relationship between simulation size and pricing uncertainty.

Construct 95% confidence intervals to quantify estimation uncertainty.

Conduct sensitivity analysis to examine how model parameters affect option valuations.

Technologies Used

Python — Core programming language

NumPy — Numerical calculations and random simulations

SciPy — Statistical functions and probability distributions

Matplotlib — Data visualization

Methodology

1. Simulating Future Stock Prices

The model simulates possible future stock prices using geometric Brownian motion under the risk-neutral measure:

[
S_T = S_0 \exp\left[\left(r-\frac{\sigma^2}{2}\right)T+\sigma\sqrt{T}Z\right]
]

Where:

(S_T) = simulated stock price at expiration

(S_0) = initial stock price

(r) = continuously compounded risk-free interest rate

(\sigma) = annualized volatility

(T) = time to expiration in years

(Z) = random draw from a standard normal distribution

2. Calculating the Option Price

For each simulated terminal stock price, the European call option payoff is:

[
\text{Payoff}=\max(S_T-K,0)
]

Where (K) is the strike price.

The Monte Carlo estimate discounts the average simulated payoff to the present:

[
\hat{C}=e^{-rT}\frac{1}{N}\sum_{i=1}^{N}\max(S_T^{(i)}-K,0)
]

Where:

(\hat{C}) = estimated call option price

(N) = number of simulations

(e^{-rT}) = discount factor

3. Validating Against Black–Scholes

I calculate the analytical European call option price using the Black–Scholes model and compare it with the Monte Carlo estimate.

The absolute percentage error is calculated as:

[
\text{Percentage Error}=
\frac{|\hat{C}-C_{BS}|}{C_{BS}}\times100
]

Where (C_{BS}) is the Black–Scholes price.

This comparison provides a benchmark for evaluating the accuracy of the simulation.

4. Confidence Interval Analysis

I estimate the standard error of the Monte Carlo price using the sample standard deviation of the discounted payoffs:

[
SE(\hat{C})=\frac{s_X}{\sqrt{N}}
]

Where (s_X) is the sample standard deviation of the discounted payoffs.

An approximate 95% confidence interval is then constructed as:

[
\hat{C}\pm1.96SE(\hat{C})
]

I examine how the confidence interval width changes as the number of simulations increases.

5. Sensitivity Analysis

I investigate how changes in model parameters affect theoretical option prices. This helps illustrate how inputs such as volatility, the risk-free interest rate, and time to expiration influence option valuation.

Results and Analysis

The project examines the relationship between simulation size and estimation uncertainty.

The analysis focuses on:

Pricing accuracy: Comparing Monte Carlo estimates against the analytical Black–Scholes price.

Simulation size: Investigating how the number of simulated outcomes affects estimation error.

Confidence intervals: Examining how estimated uncertainty changes as simulation size increases.

Parameter sensitivity: Evaluating how changes in model assumptions affect theoretical option values.

The results illustrate how Monte Carlo simulation can approximate an analytical option price and how increasing the number of simulations generally improves estimation precision.

Numerical results and plots will be added here.

Model Assumptions and Limitations

The model makes several simplifying assumptions:

The underlying stock follows geometric Brownian motion.

The risk-free interest rate and volatility remain constant over the option's life.

The option is European-style and can only be exercised at expiration.

The model uses a risk-neutral pricing framework.

The simulation estimates theoretical value under the specified assumptions; it does not predict actual market prices or guarantee trading profits.

These assumptions limit how directly the model can represent real financial markets.

How to Run

Requirements

Python 3 and the following libraries:

NumPy

SciPy

Matplotlib

Installation

Install the required libraries using:

pip install numpy scipy matplotlib

Execution

Clone or download this repository.

Open the project in a Python environment.

Run the Python script.

Review the printed results and generated plots.

Key Takeaways

Through this project, I developed practical experience with:

Implementing Monte Carlo simulation in Python.

Applying probability distributions and numerical methods to financial modeling.

Comparing simulation-based estimates with analytical solutions.

Evaluating estimation error and confidence intervals.

Visualizing the relationship between simulation size and estimation uncertainty.

Future Improvements

Potential extensions include:

Comparing Monte Carlo estimates across repeated trials and different simulation sizes.

Investigating variance-reduction techniques, such as antithetic variates.

Extending the model to price additional types of options.

Exploring more realistic assumptions about volatility and interest rates.
