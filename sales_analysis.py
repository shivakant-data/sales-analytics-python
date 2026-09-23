import pandas as pd

# ==========================================
# 1. Load Dataset
# ==========================================

df = pd.read_csv("sales_data.csv")

print("Dataset Shape:")
print(df.shape)

print("\nMissing Values:")
print(df.isnull().sum())

print("\nDuplicate Rows:")
print(df.duplicated().sum())


# ==========================================
# 2. Basic Sales KPIs
# ==========================================

total_sales = df["Sales"].sum()
total_profit = df["Profit"].sum()
avg_sales = df["Sales"].mean()
avg_profit = df["Profit"].mean()
median_sales = df["Sales"].median()

profit_margin = (total_profit / total_sales) * 100

print("\n========== SALES KPIs ==========")
print("Total Sales:", total_sales)
print("Total Profit:", total_profit)
print("Average Sales:", round(avg_sales, 2))
print("Average Profit:", round(avg_profit, 2))
print("Median Sales:", median_sales)
print("Overall Profit Margin:", round(profit_margin, 2), "%")


# ==========================================
# 3. Product Analysis
# ==========================================

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

print("\n========== PRODUCT ANALYSIS ==========")
print(product_analysis.round(2))


# ==========================================
# 4. City Analysis
# ==========================================

city_analysis = df.groupby("City").agg(
    Sales=("Sales", "sum"),
    Profit=("Profit", "sum"),
    Quantity=("Quantity", "sum"),
    Orders=("Order_ID", "count")
).sort_values("Sales", ascending=False)

city_analysis["Profit_Margin"] = (
    city_analysis["Profit"] /
    city_analysis["Sales"] * 100
)

print("\n========== CITY ANALYSIS ==========")
print(city_analysis.round(2))


# ==========================================
# 5. Customer Analysis
# ==========================================

customer_analysis = df.groupby("Customer").agg(
    Sales=("Sales", "sum"),
    Profit=("Profit", "sum"),
    Orders=("Order_ID", "count"),
    Quantity=("Quantity", "sum")
).sort_values("Sales", ascending=False)

customer_analysis["AOV"] = (
    customer_analysis["Sales"] /
    customer_analysis["Orders"]
)

print("\n========== CUSTOMER ANALYSIS ==========")
print(customer_analysis.round(2))


# ==========================================
# 6. Monthly Analysis
# ==========================================

df["Order_Date"] = pd.to_datetime(df["Order_Date"])

monthly_analysis = df.groupby(
    df["Order_Date"].dt.month_name()
).agg(
    Sales=("Sales", "sum"),
    Profit=("Profit", "sum"),
    Orders=("Order_ID", "count"),
    Quantity=("Quantity", "sum")
)

monthly_analysis["Profit_Margin"] = (
    monthly_analysis["Profit"] /
    monthly_analysis["Sales"] * 100
)

print("\n========== MONTHLY ANALYSIS ==========")
print(monthly_analysis.round(2))


# ==========================================
# 7. Top 5 Sales Orders
# ==========================================

top_orders = df.sort_values(
    "Sales",
    ascending=False
).head(5)

print("\n========== TOP 5 SALES ORDERS ==========")

print(
    top_orders[
        ["Order_ID", "Customer", "Product", "Sales", "Profit"]
    ]
)


# ==========================================
# 8. Top 5 Profit Orders
# ==========================================

top_profit_orders = df.sort_values(
    "Profit",
    ascending=False
).head(5)

print("\n========== TOP 5 PROFIT ORDERS ==========")

print(
    top_profit_orders[
        ["Order_ID", "Customer", "Product", "Sales", "Profit"]
    ]
)


# ==========================================
# 9. High-Value Orders
# ==========================================

high_value_orders = df[
    (df["Sales"] >= 50000) &
    (df["Profit"] >= 7000)
]

print("\n========== HIGH-VALUE ORDERS ==========")
print("Number of High-Value Orders:", len(high_value_orders))

print(
    high_value_orders[
        ["Order_ID", "Customer", "Product", "Sales", "Profit"]
    ]
)
