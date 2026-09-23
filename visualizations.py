import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("sales_data.csv")

# Convert date
df["Order_Date"] = pd.to_datetime(df["Order_Date"])


# ==========================================
# 1. Sales by Product
# ==========================================

product_sales = (
    df.groupby("Product")["Sales"]
    .sum()
    .sort_values(ascending=False)
)

plt.figure(figsize=(10, 6))
product_sales.plot(kind="bar")

plt.title("Sales by Product")
plt.xlabel("Product")
plt.ylabel("Sales")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


# ==========================================
# 2. Monthly Sales Trend
# ==========================================

monthly_sales = (
    df.groupby(df["Order_Date"].dt.month_name())["Sales"]
    .sum()
)

month_order = ["January", "February", "March"]
monthly_sales = monthly_sales.reindex(month_order)

plt.figure(figsize=(8, 5))
monthly_sales.plot(kind="line", marker="o")

plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.tight_layout()
plt.show()


# ==========================================
# 3. Sales by City
# ==========================================

city_sales = (
    df.groupby("City")["Sales"]
    .sum()
    .sort_values(ascending=False)
)

plt.figure(figsize=(8, 5))
sns.barplot(
    x=city_sales.index,
    y=city_sales.values
)

plt.title("Sales by City")
plt.xlabel("City")
plt.ylabel("Sales")
plt.tight_layout()
plt.show()


# ==========================================
# 4. Sales vs Profit
# ==========================================

plt.figure(figsize=(8, 5))

sns.scatterplot(
    data=df,
    x="Sales",
    y="Profit"
)

plt.title("Sales vs Profit")
plt.xlabel("Sales")
plt.ylabel("Profit")
plt.tight_layout()
plt.show()