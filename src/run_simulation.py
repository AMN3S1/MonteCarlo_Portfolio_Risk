import numpy as np
import matplotlib.pyplot as plt
import os
import pandas as pd

from src.generate_returns import generate_returns
from src.monte_carlo_simulation import monte_carlo_simulation
from src.visualization import plot_simulated_portfolios, plot_final_distribution
from src.risk_metrics import calculate_var, calculate_cvar

# Force matplotlib backend for saving figures
plt.switch_backend('Agg')

# Create output folders if they don't exist
os.makedirs("../outputs/plots", exist_ok=True)

# Common Parameters
initial_investment = 10000
days = 252  # One trading year
simulations = 500

# Define two scenarios
scenarios = {
    "optimistic": {"mu": 0.10, "sigma": 0.10},
    "pessimistic": {"mu": 0.03, "sigma": 0.25}
}

# Initialize list to collect metrics
metrics_list = []

# Loop over scenarios
for scenario_name, params in scenarios.items():
    mu = params["mu"]
    sigma = params["sigma"]

    # 1. Generate returns
    daily_returns = generate_returns(mu, sigma, days, simulations)

    # 2. Run Monte Carlo simulation
    simulated_values = monte_carlo_simulation(initial_investment, daily_returns)

    # 3. Calculate risk metrics
    var = calculate_var(simulated_values[:, -1], confidence_level=0.95)
    cvar = calculate_cvar(simulated_values[:, -1], confidence_level=0.95)

    # 4. Plot and save graphs
    fig1 = plt.figure(figsize=(12, 6))
    plt.plot(simulated_values)
    plt.title(f"Simulated Portfolio Value Over Time ({scenario_name.capitalize()} Scenario)")
    plt.xlabel("Days")
    plt.ylabel("Portfolio Value")
    plt.grid(True)
    plt.tight_layout()
    fig1.savefig(f"../outputs/plots/simulated_portfolios_{scenario_name}.png")
    plt.close(fig1)

    fig2 = plt.figure(figsize=(10, 5))
    final_values = simulated_values[:, -1]
    plt.hist(final_values, bins=50, edgecolor='black')
    plt.title(f"Distribution of Final Portfolio Values ({scenario_name.capitalize()} Scenario)")
    plt.xlabel("Final Portfolio Value")
    plt.ylabel("Frequency")
    plt.grid(True)
    plt.tight_layout()
    fig2.savefig(f"../outputs/plots/final_distribution_{scenario_name}.png")
    plt.close(fig2)

    # 5. Save metrics
    metrics_list.append({
        "scenario": scenario_name,
        "initial_investment": initial_investment,
        "mu": mu,
        "sigma": sigma,
        "days": days,
        "simulations": simulations,
        "VaR_95": var,
        "CVaR_95": cvar
    })

# Save all metrics to a CSV
metrics_df = pd.DataFrame(metrics_list)
metrics_df.to_csv("../outputs/metrics.csv", index=False)

# Print results
print(metrics_df)
