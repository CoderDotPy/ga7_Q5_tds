# chart.py
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Set Seaborn style for professional look
sns.set_style("whitegrid")
sns.set_context("talk")

# Generate synthetic data: seasonal revenue patterns
np.random.seed(42)
months = pd.date_range("2024-01-01", periods=12, freq="M").strftime("%b")
revenue = (
    50000
    + 15000 * np.sin(np.linspace(0, 2 * np.pi, 12))  # seasonal pattern
    + np.random.normal(0, 3000, 12)  # random noise
)

# Create DataFrame
df = pd.DataFrame({"Month": months, "Revenue": revenue})

# Create lineplot
plt.figure(figsize=(8, 8))  # ensures 512x512 at dpi=64
sns.lineplot(
    data=df,
    x="Month",
    y="Revenue",
    marker="o",
    linewidth=2.5,
    palette="deep",
    color="seagreen"
)

# Customize chart
plt.title("Monthly Revenue Trends (Synthetic Data)", fontsize=16, pad=15)
plt.xlabel("Month", fontsize=12)
plt.ylabel("Revenue (USD)", fontsize=12)
plt.xticks(rotation=45)

# Save chart as 512x512 PNG
plt.savefig("chart.png", dpi=64, bbox_inches="tight")
plt.close()
