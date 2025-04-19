import matplotlib
import numpy
from src.generate_returns import generate_returns
from src.monte_carlo_simulation import monte_carlo_simulation
from src.visualization import plot_simulated_portfolios, plot_final_distribution
from src.risk_metrics import calculate_var, calculate_cvar
matplotlib.use('TkAgg')


# Parameters
initial_investment = 10000
days = 252  # One trading year
simulations = 500
mu = 0.07  # expected annual return ~7%
sigma = 0.15  # expected annual volatility ~15%

# Generate returns
daily_returns = generate_returns(mu, sigma, days, simulations)

# Run Monte Carlo simulation
simulated_values = monte_carlo_simulation(initial_investment, daily_returns)

# Plot results
plot_simulated_portfolios(simulated_values)
plot_final_distribution(simulated_values)
# Calculate risk metrics
var_95 = calculate_var(simulated_values, confidence_level=0.95)
cvar_95 = calculate_cvar(simulated_values, confidence_level=0.95)

# Print results
print(f"Value at Risk (95% confidence): ${var_95:.2f}")
print(f"Conditional Value at Risk (95% confidence): ${cvar_95:.2f}")
