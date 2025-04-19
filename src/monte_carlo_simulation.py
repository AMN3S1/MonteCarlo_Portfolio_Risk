import numpy as np

def monte_carlo_simulation(initial_investment, daily_returns):
    """
    Perform Monte Carlo simulation for portfolio returns.

    Args:
    - initial_investment (float): starting amount
    - daily_returns (numpy.ndarray): array of simulated daily returns (days x simulations)

    Returns:
    - numpy.ndarray: array of simulated portfolio values over time
    """
    cumulative_returns = (1 + daily_returns).cumprod(axis=0)
    portfolio_values = initial_investment * cumulative_returns
    return portfolio_values
