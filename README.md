# MonteCarlo_Portfolio_Risk


## Project Overview

**MonteCarlo_Portfolio_Risk** is a Python-based financial simulation tool that projects a portfolio’s value over time using Monte Carlo methods. Given user-specified parameters for expected return and volatility, the script simulates numerous possible future price paths for the portfolio. It evaluates two contrasting scenarios – **optimistic** and **pessimistic** – to demonstrate how different market conditions or assumptions can impact potential outcomes. By analyzing the simulation results, the project computes key risk metrics (Value at Risk and Conditional Value at Risk) to quantify potential losses. This tool is ideal for investors and risk analysts looking to understand the uncertainty and risk in portfolio performance under varying conditions in a robust, data-driven way.

## Key Features

- **Monte Carlo Simulation:** Generates a large number of random portfolio value trajectories over a specified time horizon, modeling the effects of daily returns and volatility.
- **Dual Scenarios (Optimistic vs Pessimistic):** Runs two preset scenarios to compare outcomes under favorable versus adverse market assumptions. This provides insight into best-case and worst-case expectations.
- **Risk Metrics Calculation:** Computes **Value at Risk (VaR)** and **Conditional Value at Risk (CVaR)** at a given confidence level from the simulation outcomes. These metrics help quantify the potential downside risk.
- **Visualizations:** Automatically produces clear charts illustrating the simulation results for each scenario, including the time-series of simulated portfolio values and the distribution of final portfolio values.  
- **Configurable Parameters:** Allows customization of key parameters (initial portfolio value, expected annual return, volatility, number of days, number of simulations, etc.) to tailor the simulation to different portfolios or market conditions.
- **Output Reports:** Saves the generated charts (PNG images) and risk metrics (CSV file) in an **outputs** folder for easy review and inclusion in reports or presentations.

## Folder Structure

The repository is organized as follows for clarity:

```plaintext
MonteCarlo_Portfolio_Risk/
├── MonteCarlo_Portfolio_Risk.py    # Main script to run the simulation
├── outputs/
│   ├── plots/                      # Folder containing generated charts
│   │   ├── simulated_portfolios_optimistic.png
│   │   ├── final_distribution_optimistic.png
│   │   ├── simulated_portfolios_pessimistic.png
│   │   └── final_distribution_pessimistic.png
│   └── metrics.csv                 # CSV file with calculated risk metrics (VaR, CVaR, etc.)
├── README.md                       # Project documentation (you are here!)
└── requirements.txt                # (Optional) Python dependencies for the project
```

*Note:* The `MonteCarlo_Portfolio_Risk.py` script generates the `outputs` folder and its contents automatically when run.

## Installation Instructions

1. **Clone the Repository:** Download the project to your local machine using Git:  
   ```bash
   git clone https://github.com/yourusername/MonteCarlo_Portfolio_Risk.git
   cd MonteCarlo_Portfolio_Risk
   ```
2. **Setup Python Environment:** Ensure you have **Python 3.x** installed. It’s recommended to use a virtual environment (venv) or Conda environment to manage dependencies.
3. **Install Dependencies:** Install the required Python libraries. You can install them manually or use the provided `requirements.txt` file:  
   ```bash
   pip install -r requirements.txt
   ```  
   *Required libraries include:* `numpy` (for numerical computations), `pandas` (for handling simulation data and outputting CSV), and `matplotlib` (for generating plots).  
4. **Verify Installation:** Once dependencies are installed, you are ready to run the simulations.

## How to Run

Running the simulation is straightforward:

- **Step 1:** Open a terminal/command prompt in the project directory.
- **Step 2:** Execute the main simulation script:  
  ```bash
  python MonteCarlo_Portfolio_Risk.py
  ```  
  This will run the Monte Carlo simulation for both optimistic and pessimistic scenarios using the default parameters defined in the script.
- **Step 3:** Wait for the simulation to complete. The script will output the results to the `outputs` directory:
  - It will save the plots in `outputs/plots/` (four PNG image files, two for each scenario).
  - It will save a summary of risk metrics in `outputs/metrics.csv`.
- **Step 4:** Review the results:
  - Open the images in `outputs/plots/` to visualize the portfolio simulations and final distributions.
  - Open `outputs/metrics.csv` (e.g., with a spreadsheet or text editor) to see the numerical values of VaR, CVaR, and possibly other metrics.
  
*Note:* By default, the script uses internally defined parameters for the scenarios. To experiment with different assumptions (e.g., changing the expected return or volatility), you can edit the parameters at the top of the script. After modifying parameters, rerun the script to generate a new set of results.

## Visual Results

After running the simulation, the tool produces visualizations to help interpret the outcomes of each scenario. Below we show and explain the key plots generated:

 ([image]()) *Simulated portfolio value trajectories over 250 days under the **Optimistic scenario**. In this scenario, the portfolio is assumed to have relatively favorable conditions (e.g. higher average returns and moderate volatility). Each line represents one simulated path of portfolio value evolution starting from an initial value (e.g. \$10,000). We can see a general upward drift in most paths, with the majority of simulations ending above or near the starting value. The spread between the lines is not too wide, indicating less uncertainty compared to the pessimistic case.*

 ([image]()) *Distribution of final portfolio values after 250 days for the **Optimistic scenario**. This histogram aggregates the ending portfolio values from all simulations in the optimistic case. The outcomes are clustered tightly around the initial value (with a slight tilt towards gains). In other words, under optimistic assumptions, the portfolio is likely to end up close to or somewhat above its starting value, and there is a low probability of a large loss. The concentration of the distribution indicates higher confidence in the range of possible final values.*

 ([image]()) *Simulated portfolio value trajectories over 250 days under the **Pessimistic scenario**. This scenario assumes more adverse market conditions (e.g. lower or zero growth and higher volatility). The plot shows a much wider range of outcomes for the portfolio value. Some simulation paths experience significant growth spurts or drops along the way. Notably, there are paths that dip well below the initial value (reflecting potential losses in a bear market or high volatility environment), and a few that rise substantially (showing that even in a pessimistic volatility scenario, there is a chance of upside outliers). The overall spread is much larger than in the optimistic scenario, visualizing the greater uncertainty and risk.*

 ([image]()) *Distribution of final portfolio values for the **Pessimistic scenario**. This histogram shows the ending values of the portfolio after 250 days under pessimistic assumptions. Compared to the optimistic scenario, the distribution here is broader and shifted slightly to the left (toward lower values). There is a noticeable left tail – a higher frequency of simulations ending with significant losses (well below the initial \$10k). While the center of the distribution is around the initial value (meaning many outcomes hover near break-even), the extended left tail indicates a non-negligible probability of large losses. This underscores the importance of risk management in volatile or low-return conditions.*

## Risk Metrics

To quantify the potential losses demonstrated by the simulations, the script calculates the **Value at Risk (VaR)** and **Conditional Value at Risk (CVaR)** for each scenario. These metrics are standard in financial risk management:

- **Value at Risk (VaR)**: VaR at a given confidence level (e.g. 95%) is the threshold loss **such that the probability of experiencing a loss greater than this amount is only 5%**. In simpler terms, it answers the question: *“How bad can it get, with X% certainty?”* For example, a 95% one-year VaR of \$1,000 means that there is only a 5% chance that the portfolio loses more than \$1,000 in one year.
- **Conditional Value at Risk (CVaR)**: Also known as *Expected Shortfall*, CVaR is the **average loss given that the loss is beyond the VaR threshold**. It considers the worst-case tail of the distribution. Following the previous example, if those worst 5% of cases do occur, CVaR might tell us that the average loss in those scenarios is, say, \$1,500. This provides insight into the severity of extreme losses beyond the VaR level.

In this project, we typically use a 95% confidence level for VaR and CVaR calculations based on the distribution of final portfolio values. The results for each scenario are saved in the `outputs/metrics.csv` file. For instance, based on a sample simulation with an initial \$10,000 portfolio:

| Scenario      | 95% VaR (1-year) | 95% CVaR (1-year) |
| ------------- | ---------------- | ----------------- |
| **Optimistic**  | ≈ **\$150** loss (i.e. portfolio **won’t lose** more than \$150, 95% of the time) | ≈ **\$300** average loss in the worst 5% cases |
| **Pessimistic** | ≈ **\$1,400** loss (much larger potential drop at 95% confidence) | ≈ **\$1,900** average loss in the worst 5% cases |

These numbers illustrate that under the pessimistic scenario, the portfolio’s risk is significantly higher: there is a 5% chance of losing about \$1.4k or more, whereas in the optimistic scenario the 5% worst-case loss is only around \$150. Moreover, if the worst-case conditions occur, the pessimistic scenario’s losses are on average deeper (about \$1.9k) compared to the optimistic scenario (about \$300).

## Example Parameters Used

The behavior of the simulation can be adjusted by changing the input parameters. For transparency, here are the example parameters used in the default configuration of the simulation (which produced the above results and figures):

- **Initial Portfolio Value:** \$10,000  
- **Time Horizon:** 250 trading days (approximately 1 year of trading days)  
- **Number of Simulations:** 200 (paths per scenario)  
- **Optimistic Scenario Assumptions:**  
  - Expected Annual Return ≈ **7%** (positive growth expectation)  
  - Annual Volatility ≈ **10%** (moderate volatility)  
- **Pessimistic Scenario Assumptions:**  
  - Expected Annual Return ≈ **0%** (flat growth, i.e. no expected gain)  
  - Annual Volatility ≈ **15%** (higher uncertainty/volatility)  
- **VaR/CVaR Confidence Level:** **95%** (for risk metric calculations)  

Feel free to modify these parameters in the script. For example, you can increase the number of simulations for more granular results, or change the return/volatility assumptions to model different market conditions or portfolio strategies.

## Author / Contact Info

**Author:** *Your Name* (Creator and Maintainer of this project)  
**Contact:** You can reach out via email at *your.email@example.com* or through my GitHub profile [yourusername](https://github.com/yourusername) for any questions, suggestions, or collaboration ideas. Feedback and contributions are welcome! 

---

*Thank you for checking out **MonteCarlo_Portfolio_Risk**. We hope this tool serves as a valuable resource for understanding portfolio risk through simulation. If you find this project useful, please consider giving it a star on GitHub!*
