import matplotlib.pyplot as plt
import numpy as np
import os

# Create directories if they don't exist
os.makedirs("../outputs/plots", exist_ok=True)

def plot_simulated_portfolios(portfolio_values: np.ndarray):
    """
    Plot simulated portfolio paths over time.
    """
    plt.figure(figsize=(12, 6))
    plt.plot(portfolio_values)
    plt.title("Simulated Portfolio Value Over Time")
    plt.xlabel("Days")
    plt.ylabel("Portfolio Value")
    plt.grid(True)
    plt.tight_layout()
    plt.savefig("../outputs/plots/simulated_portfolios.png")  # Save instead of show
    plt.close()  # Close figure

def plot_final_distribution(portfolio_values: np.ndarray):
    """
    Plot the distribution of final portfolio values.
    """
    final_values = portfolio_values
    plt.figure(figsize=(10, 5))
    plt.hist(final_values, bins=50, edgecolor='black')
    plt.title("Distribution of Final Portfolio Values")
    plt.xlabel("Final Portfolio Value")
    plt.ylabel("Frequency")
    plt.grid(True)
    plt.tight_layout()
    plt.savefig("../outputs/plots/final_distribution.png")  # Save instead of show
    plt.close()  # Close figure
