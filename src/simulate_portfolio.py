import numpy as np

def simulate_portfolio(returns: np.ndarray, initial_investment: float = 1000) -> np.ndarray:
    """
    Simulate the portfolio value over time based on returns.

    Parameters:
    - returns (np.ndarray): Array of simulated returns (days x portfolios).
    - initial_investment (float): Starting value of the portfolio.

    Returns:
    - np.ndarray: Simulated portfolio values over time.
    """
    cumulative_returns = (1 + returns).cumprod(axis=0)
    portfolio_values = initial_investment * cumulative_returns
    return portfolio_values
