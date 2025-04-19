import numpy as np

def generate_returns(mu, sigma, days, simulations, seed=42):
    """
    Generate simulated daily returns based on expected annual return and volatility.

    Args:
    - mu (float): expected annual return
    - sigma (float): expected annual volatility
    - days (int): number of days to simulate
    - simulations (int): number of simulations to generate
    - seed (int): random seed for reproducibility (default 42)

    Returns:
    - numpy.ndarray: matrix of simulated daily returns (days x simulations)
    """
    np.random.seed(seed)
    daily_return_mean = mu / 252  # 252 trading days
    daily_return_std = sigma / np.sqrt(252)

    return np.random.normal(daily_return_mean, daily_return_std, size=(days, simulations))
