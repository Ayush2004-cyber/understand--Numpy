import pandas as pd
import numpy as np
import streamlit as st
import matplotlib.pyplot as plt

st.set_page_config(page_title="Pandas Real-Life Examples", layout="wide")
st.title("📊 Pandas Real-Life Examples Visualizer")

# Example 1: Labeled data + automatic alignment
st.subheader("1️⃣ Labeled Data + Automatic Alignment")
st.markdown("Pandas automatically aligns data based on labels (indices) when performing arithmetic operations.")
sales1 = pd.Series([100, 200], index=["Delhi", "Mumbai"], name="Sales Q1")
sales2 = pd.Series([150, 120], index=["Delhi", "Bangalore"], name="Sales Q2")
result1 = sales1 + sales2
st.write("Sales Q1:", sales1)
st.write("Sales Q2:", sales2)
st.write("Aligned Result (Sum of Sales):", result1)

fig1, ax1 = plt.subplots(figsize=(8, 4))
result1.plot(kind='bar', ax=ax1, color='skyblue')
ax1.set_title("Automatic Alignment of Labels (Sum of Sales)", fontsize=14)
ax1.set_ylabel("Total Sales", fontsize=12)
ax1.set_xlabel("City", fontsize=12)
ax1.tick_params(axis='x', rotation=0)
st.pyplot(fig1)
plt.close(fig1) # Close figure to free up memory

# Example 2: Time series & non-time series
st.subheader("2️⃣ Time Series & Non-Time Series")
st.markdown("Pandas handles **time series data** with specialized functionalities, while also working seamlessly with non-time series data.")
dates = pd.date_range("2023-01-01", periods=7, freq='D') # Changed periods to 7 for more data
stock_prices = pd.Series(np.random.randint(100, 200, 7), index=dates, name="Stock Price")
products = pd.Series(["Shampoo", "Soap", "Toothpaste", "Brush", "Lotion"], name="Products") # Added more products
st.write("Time Series Data (Daily Stock Prices):", stock_prices)
st.write("Non-Time Series Data (Product List):", products)

fig2, ax2 = plt.subplots(figsize=(10, 5))
stock_prices.plot(ax=ax2, marker='o', linestyle='-', color='purple')
ax2.set_title("Stock Prices Over Time", fontsize=14)
ax2.set_ylabel("Price ($)", fontsize=12)
ax2.set_xlabel("Date", fontsize=12)
ax2.grid(True, linestyle='--', alpha=0.7)
st.pyplot(fig2)
plt.close(fig2) # Close figure

# Example 3: Arithmetic with metadata preserved
st.subheader("3️⃣ Arithmetic & Aggregation with Metadata")
st.markdown("Metadata (like index names) is often preserved during arithmetic operations and aggregations.")
players = pd.Series({"Virat": 45, "Rohit": 50, "Rahul": 38, "Dhoni": 60, "Sachin": 75}, name="Player Scores")
st.write("Players Scores:", players)
st.write("Average Score:", players.mean())
st.write("Maximum Score:", players.max())
st.write("Scores + 5 Bonus Runs:", players + 5)

# Example 4: Missing data handling
st.subheader("4️⃣ Missing Data Handling")
st.markdown("Pandas provides robust methods to **handle missing data** (`NaN` values), which is crucial for data cleaning.")
data_with_nan = pd.Series([25, np.nan, 30, np.nan, 40, 50, np.nan], index=["P1", "P2", "P3", "P4", "P5", "P6", "P7"], name="Sample Data")
st.write("Original Data with Missing Values:", data_with_nan)
st.write("Fill Missing with Average:", data_with_nan.fillna(data_with_nan.mean()))
st.write("Drop Missing:", data_with_nan.dropna())
st.write("Fill Missing with 0:", data_with_nan.fillna(0))
st.write("Forward Fill Missing (fills with previous valid observation):", data_with_nan.ffill())
st.write("Backward Fill Missing (fills with next valid observation):", data_with_nan.bfill())


# Example 5: Merge/Join like SQL
st.subheader("5️⃣ Merge/Join Like SQL")
st.markdown("Combine DataFrames using various **join types** (like `INNER`, `LEFT`, `RIGHT`, `OUTER`) similar to SQL operations.")
cust_data = pd.DataFrame({"CustID": [1, 2, 3, 5], "Name": ["Amit", "Neha", "Raj", "Priya"], "City": ["Delhi", "Mumbai", "Pune", "Chennai"]})
order_data = pd.DataFrame({"CustID": [1, 2, 4, 3], "Orders": [5, 3, 2, 7], "Product": ["Laptop", "Mouse", "Keyboard", "Monitor"]})
st.write("Customer Data:", cust_data)
st.write("Order Data:", order_data)

st.markdown("---")
st.markdown("**Outer Merge** (Union of keys, `NaN` where no match):")
merged_outer = pd.merge(cust_data, order_data, on="CustID", how="outer")
st.write(merged_outer)

st.markdown("---")
st.markdown("**Inner Merge** (Intersection of keys):")
merged_inner = pd.merge(cust_data, order_data, on="CustID", how="inner")
st.write(merged_inner)

st.markdown("---")
st.markdown("**Left Merge** (All keys from left, matching from right):")
merged_left = pd.merge(cust_data, order_data, on="CustID", how="left")
st.write(merged_left)


# Example 6: All in one place (Data Cleaning & Preparation)
st.subheader("6️⃣ Data Cleaning & Preparation Pipeline")
st.markdown("A combined example demonstrating data generation, missing value imputation, and visualization.")
full_data = pd.DataFrame({
    "Date": pd.date_range("2023-01-01", periods=10, freq='W'), # More data points
    "Sales": [200, np.nan, 250, 300, np.nan, 320, 280, np.nan, 350, 400],
    "City": ["Delhi", "Mumbai", "Bangalore", "Chennai", "Kolkata", "Delhi", "Mumbai", "Bangalore", "Chennai", "Kolkata"],
    "Region": ["North", "West", "South", "South", "East", "North", "West", "South", "South", "East"]
})
st.write("Original Raw Data:", full_data)

st.markdown("---")
st.markdown("**Step 1: Fill Missing Sales with Mean**")
full_data["Sales"] = full_data["Sales"].fillna(full_data["Sales"].mean())
st.write("Data After Imputing Missing Sales:", full_data)

fig6, ax6 = plt.subplots(figsize=(10, 5))
full_data.plot(x="Date", y="Sales", kind="line", marker='o', ax=ax6, color='teal')
ax6.set_title("Sales Over Time (Cleaned Data)", fontsize=14)
ax6.set_ylabel("Sales Amount", fontsize=12)
ax6.set_xlabel("Date", fontsize=12)
ax6.grid(True, linestyle=':', alpha=0.6)
st.pyplot(fig6)
plt.close(fig6) # Close figure

st.markdown("---")
# New Example 7: Groupby and Aggregation
st.subheader("7️⃣ Groupby and Aggregation")
st.markdown("Group data by one or more columns and apply aggregation functions (e.g., sum, mean, count) to analyze patterns.")
st.write("Original Data for Groupby:", full_data)
st.markdown("---")

st.markdown("**Sales by City:**")
sales_by_city = full_data.groupby("City")["Sales"].sum().reset_index()
st.write(sales_by_city)

fig7_1, ax7_1 = plt.subplots(figsize=(8, 5))
sales_by_city.plot(kind='bar', x='City', y='Sales', ax=ax7_1, color='lightcoral')
ax7_1.set_title("Total Sales by City", fontsize=14)
ax7_1.set_ylabel("Total Sales", fontsize=12)
ax7_1.set_xlabel("City", fontsize=12)
ax7_1.tick_params(axis='x', rotation=45)
st.pyplot(fig7_1)
plt.close(fig7_1)

st.markdown("---")
st.markdown("**Average Sales by Region:**")
avg_sales_by_region = full_data.groupby("Region")["Sales"].mean().reset_index()
st.write(avg_sales_by_region)

fig7_2, ax7_2 = plt.subplots(figsize=(8, 5))
avg_sales_by_region.plot(kind='bar', x='Region', y='Sales', ax=ax7_2, color='mediumseagreen')
ax7_2.set_title("Average Sales by Region", fontsize=14)
ax7_2.set_ylabel("Average Sales", fontsize=12)
ax7_2.set_xlabel("Region", fontsize=12)
ax7_2.tick_params(axis='x', rotation=0)
st.pyplot(fig7_2)
plt.close(fig7_2)

st.markdown("---")
# New Example 8: Applying a Custom Function
st.subheader("8️⃣ Applying Custom Functions")
st.markdown("Use `.apply()` to execute a custom function row-wise or column-wise on your Series or DataFrame.")

def categorize_sales(sales_amount):
    if sales_amount > 300:
        return "High"
    elif 250 <= sales_amount <= 300:
        return "Medium"
    else:
        return "Low"

full_data["Sales_Category"] = full_data["Sales"].apply(categorize_sales)
st.write("Data with New Sales Category Column:", full_data)

st.markdown("---")
# New Example 9: Sorting Data
st.subheader("9️⃣ Sorting Data")
st.markdown("Sort your DataFrame or Series by values in one or more columns.")

st.markdown("**Sorted by Sales (Ascending):**")
sorted_by_sales_asc = full_data.sort_values(by="Sales", ascending=True)
st.write(sorted_by_sales_asc)

st.markdown("---")
st.markdown("**Sorted by Date (Descending):**")
sorted_by_date_desc = full_data.sort_values(by="Date", ascending=False)
st.write(sorted_by_date_desc)
