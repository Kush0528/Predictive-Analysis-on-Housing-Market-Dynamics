import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import os

# Paths
data_path = "./data/processed/updated_processed_data.csv"

# Read the data
data = pd.read_csv(data_path)

# Filter data to include only rows after 2010-01-01
data_timeseries = data[data["Date"] > '2010-01-01']

# Plot time series of median sale price
plt.figure(figsize=(14, 6))
sns.lineplot(data=data_timeseries, x="Date", y="median_sale_price_all_homes", ci=None)
plt.title("Median Sale Price Over Time (Post-2008)")
plt.xlabel("Date")
plt.ylabel("Median Sale Price")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Plot distribution of market_heat_index
key_features = ["market_heat_index"]
for feature in key_features:
    plt.figure(figsize=(10, 5))
    sns.histplot(data[feature], kde=True, bins=30)
    plt.title(f"Distribution of {feature}")
    plt.xlabel(feature)
    plt.ylabel("Frequency")
    plt.show()

# Plot the distribution of 'percent_sold_above_list_all_homes'
plt.figure(figsize=(10, 5))
sns.histplot(data['percent_sold_above_list_all_homes'], kde=True, bins=30)
plt.title("Distribution of Percent Sold Above List (All Homes)")
plt.xlabel("Percent Sold Above List")
plt.ylabel("Frequency")
plt.tight_layout()
plt.show()

# Correlation Matrix - Heatmap
# Specify the columns you want to include in the correlation heatmap
selected_columns = [
    "median_sale_price_all_homes",
    "City_Housing_Starts",
    "market_heat_index",
    "percent_sold_above_list_all_homes",
    "percent_sold_below_list_all_homes",
    "sales_count_nowcast"
]

# Filter the numeric data to include only the selected columns
selected_data = data[selected_columns]

# Compute the correlation matrix
correlation = selected_data.corr()

# Plot the heatmap
plt.figure(figsize=(12, 8))
sns.heatmap(correlation, annot=True, fmt=".2f", cmap="coolwarm")
plt.title("Correlation Heatmap (Selected Columns)")
plt.tight_layout()
plt.show()
