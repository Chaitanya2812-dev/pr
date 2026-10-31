import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("Retail_Sales_Data.csv")
df["TransactionDate"] = pd.to_datetime(df["TransactionDate"])

# Explore dataset
print(df.head())
df.info()

print("Missing Values:")
print(df.isnull().sum())

# Total sales by region
regional_sales = df.groupby("Region")["SalesAmount"].sum()
regional_sales = regional_sales.sort_values(ascending=False)

print("Regional Sales:")
print(regional_sales)
print("\nTotal Sales:", round(regional_sales.sum(), 2))
print("Top Region:", regional_sales.idxmax())

# Bar chart: Sales by region
regional_sales.plot(kind="bar", figsize=(8, 5))
plt.title("Sales by Region")
plt.xlabel("Region")
plt.ylabel("Sales Amount")
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()

# Pie chart: Regional sales share
regional_sales.plot(kind="pie", autopct="%1.1f%%", figsize=(6, 6))
plt.title("Regional Sales Share")
plt.ylabel("")
plt.tight_layout()
plt.show()

# Sales by region and product category
category_sales = df.groupby(
    ["Region", "ProductCategory"]
)["SalesAmount"].sum().unstack(fill_value=0)

print("Sales by Region and Product Category:")
print(category_sales)

# Stacked bar chart
category_sales.plot(kind="bar", stacked=True, figsize=(10, 5))
plt.title("Sales by Region and Category")
plt.xlabel("Region")
plt.ylabel("Sales Amount")
plt.xticks(rotation=0)
plt.legend(title="Category")
plt.tight_layout()
plt.show()

# Grouped bar chart
category_sales.plot(kind="bar", figsize=(10, 5))
plt.title("Product Category Comparison")
plt.xlabel("Region")
plt.ylabel("Sales Amount")
plt.xticks(rotation=0)
plt.legend(title="Category")
plt.tight_layout()
plt.show()
