
import pandas as pd


df = pd.read_csv("sales_data.csv")

print("=" * 60)
print("SALES DATA ANALYSIS")
print("=" * 60)


print("\nFIRST 5 ROWS:")
print(df.head())

print("\nDATASET INFORMATION:")
print(f"Number of rows    : {df.shape[0]}")
print(f"Number of columns : {df.shape[1]}")

print("\nCOLUMN DATA TYPES:")
print(df.dtypes)


print("\nMISSING VALUES BEFORE CLEANING:")
print(df.isnull().sum())

numeric_columns = df.select_dtypes(include="number").columns

for column in numeric_columns:
    if df[column].isnull().any():
        df[column] = df[column].fillna(df[column].median())

text_columns = df.select_dtypes(include="object").columns

for column in text_columns:
    if df[column].isnull().any():
        df[column] = df[column].fillna(df[column].mode()[0])

duplicates_removed = df.duplicated().sum()
df = df.drop_duplicates()

print("\nDATA CLEANING:")
print(f"Duplicate rows removed: {duplicates_removed}")

print("\nMISSING VALUES AFTER CLEANING:")
print(df.isnull().sum())



total_revenue = df["Total_Sales"].sum()
average_sale = df["Total_Sales"].mean()
highest_sale = df["Total_Sales"].max()
lowest_sale = df["Total_Sales"].min()
total_quantity = df["Quantity"].sum()



product_sales = (
    df.groupby("Product")["Total_Sales"]
    .sum()
    .sort_values(ascending=False)
)

best_product = product_sales.index[0]
best_product_sales = product_sales.iloc[0]


product_analysis = (
    df.groupby("Product")
    .agg(
        Total_Sales=("Total_Sales", "sum"),
        Quantity_Sold=("Quantity", "sum"),
        Transactions=("Product", "count")
    )
    .sort_values("Total_Sales", ascending=False)
)


region_analysis = (
    df.groupby("Region")["Total_Sales"]
    .agg(["sum", "mean", "count"])
    .sort_values("sum", ascending=False)
)


print("\n" + "=" * 60)
print("SALES ANALYSIS REPORT")
print("=" * 60)

print(f"\nTotal Revenue       : {total_revenue:,.2f}")
print(f"Average Sale        : {average_sale:,.2f}")
print(f"Highest Sale        : {highest_sale:,.2f}")
print(f"Lowest Sale         : {lowest_sale:,.2f}")
print(f"Total Quantity Sold : {total_quantity}")

print("\nBEST-SELLING PRODUCT:")
print(f"Product             : {best_product}")
print(f"Total Sales         : {best_product_sales:,.2f}")

print("\nPRODUCT PERFORMANCE:")
print(product_analysis.to_string())

print("\nREGION PERFORMANCE:")
print(region_analysis.to_string())

print("\n" + "=" * 60)
print("ANALYSIS COMPLETED SUCCESSFULLY")
print("=" * 60)
