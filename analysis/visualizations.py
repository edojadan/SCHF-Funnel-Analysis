import pandas as pd
import matplotlib.pyplot as plt

# Load processed data
df = pd.read_csv("../data/schf_funnel_data.csv")

# Plot funnel drop-off visualization
plt.figure(figsize=(8, 5))
plt.bar(df["Stage"], df["Users"], color="green", alpha=0.7)
plt.xlabel("Funnel Stage")
plt.ylabel("Number of Users")
plt.title("SCHF Funnel Analysis")
plt.show()

# Plot drop-off rates
plt.figure(figsize=(8, 5))
plt.plot(df["Stage"], df["Dropoff Rate (%)"], marker="o", linestyle="-", color="red")
plt.xlabel("Funnel Stage")
plt.ylabel("Dropoff Rate (%)")
plt.title("Dropoff Rate Across SCHF Funnel Stages")
plt.grid(True)
plt.show()
