import numpy as np


def calculate_var(portfolio_values: np.ndarray, confidence_level: float = 0.95) -> float:
    """
    Calculate Value at Risk (VaR) at a specified confidence level.

    Args:
    - portfolio_values (np.ndarray): Final portfolio values.
    - confidence_level (float): Confidence level for VaR (default 95%).

    Returns:
    - VaR value.
    """
    percentile = np.percentile(portfolio_values, (1 - confidence_level) * 100)
    return portfolio_values.mean() - percentile


def calculate_cvar(portfolio_values: np.ndarray, confidence_level: float = 0.95) -> float:
    """
    Calculate Conditional Value at Risk (CVaR) (Expected Shortfall).

    Args:
    - portfolio_values (np.ndarray): Final portfolio values.
    - confidence_level (float): Confidence level for CVaR (default 95%).

    Returns:
    - CVaR value.
    """
    var_threshold = np.percentile(portfolio_values, (1 - confidence_level) * 100)
    losses = portfolio_values[portfolio_values <= var_threshold]
    return portfolio_values.mean() - losses.mean()
