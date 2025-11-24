import pandas as pd
import matplotlib.pyplot as plt
import os


os.chdir("C:/Users/AlexLaptop/Documents/Thesis/Chapter1/Data/")

data = pd.read_csv("data_combined_FINAL_v2.csv")

print(data.columns)

print(data['height_cm'].describe())

print(data['diameter_mm'].mean())

# Plotting
plt.figure(figsize=(10, 6))
plt.bar(data['site'], data['b'])
plt.title("Biomass")
plt.xlabel("Site")
plt.ylabel("Biomass")


plt.savefig("C:/Users/AlexLaptop/Desktop/biomass_plot.png")
