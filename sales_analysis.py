import pandas as pd

# Load dataset
df = pd.read_csv("sales_data.csv")

# -----------------------------
# 1. Data Overview
# -----------------------------

print("Dataset Shape:")
print(df.shape)

print("\nMissing Values:")
print(df.isnull().sum())

print("\nDuplicate Rows:")
print(df.duplicated().sum())


# -----------------------------
# 2. Basic KPIs
# -----------------------------

total_sales = df["Sales"].sum()
total_profit = df["Profit"].sum()
avg_sales = df["Sales"].mean()
avg_profit = df["Profit"].mean()
median_sales = df["Sales"].median()

profit_margin = (total_profit / total_sales) * 100

print("\n--- Sales KPIs ---")
print("Total Sales:", total_sales)
print("Total Profit:", total_profit)
print("Average Sales:", avg_sales)
print("Average Profit:", avg_profit)
print("Median Sales:", median_sales)
print("Profit Margin:", profit_margin)


# -----------------------------
# 3. Product Analysis
# -----------------------------

product_analysis = df.groupby("Product").agg(
    Sales=("Sales", "sum"),
    Profit=("Profit", "sum"),
    Quantity=("Quantity", "sum"),
    Orders=("Order_ID", "count")
).sort_values("Sales", ascending=False)

product_analysis["Profit_Margin"] = (
    product_analysis["Profit"] /
    product_analysis["Sales"] * 100
)

print("\n--- Product Analysis ---")
print(product_analysis)


# -----------------------------
# 4. City Analysis
# -----------------------------

city_analysis = df.groupby("City").agg(
    Sales=("Sales", "sum"),
    Profit=("Profit", "sum"),
    Quantity=("Quantity", "sum"),
    Orders=("Order_ID", "count")
).sort_values("Sales", ascending=False)

print("\n--- City Analysis ---")
print(city_analysis)


# -----------------------------
# 5. Monthly Analysis
# -----------------------------

df["Order_Date"] = pd.to_datetime(df["Order_Date"])

monthly_analysis = df.groupby(
    df["Order_Date"].dt.month_name()
).agg(
    Sales=("Sales", "sum"),
    Profit=("Profit", "sum")
)

print("\n--- Monthly Analysis ---")
print(monthly_analysis)


# -----------------------------
# 6. Payment Method Analysis
# -----------------------------

payment_analysis = df.groupby("Payment_Method").agg(
    Orders=("Order_ID", "count"),
    Sales=("Sales", "sum"),
    Profit=("Profit", "sum")
)

print("\n--- Payment Method Analysis ---")
print(payment_analysis)


# -----------------------------
# 7. Top Orders
# -----------------------------

top_orders = df.sort_values(
    "Sales",
    ascending=False
).head(5)

print("\n--- Top 5 Orders ---")
print(top_orders[
    ["Order_ID", "Customer", "Product", "Sales", "Profit"]
])
