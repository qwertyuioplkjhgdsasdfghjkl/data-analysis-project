import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Generate Random Sales Data using NumPy
np.random.seed(42)  # Seed for reproducibility

months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
products = ["Product_A", "Product_B", "Product_C"]

sales_data = np.random.randint(100, 500, size=(12, 3))  # Random sales numbers

# Convert to DataFrame
df = pd.DataFrame(sales_data, columns=products)
df.insert(0, "Month", months)

# Step 2: Save to CSV
csv_filename = "sales_data.csv"
df.to_csv(csv_filename, index=False)
print(f"CSV File '{csv_filename}' successfully created!")

# Step 3: Read CSV and Perform Analysis
df_read = pd.read_csv(csv_filename)
print("\n📊 Sales Data (First 5 Rows):")
print(df_read.head())

# Step 4: Data Visualization
plt.figure(figsize=(10, 5))
for product in products:
    plt.plot(df_read["Month"], df_read[product], marker="o", label=product)

plt.xlabel("Months")
plt.ylabel("Sales")
plt.title("Monthly Sales Data")
plt.legend()
plt.grid()
plt.xticks(rotation=45)
plt.show()
plt.close("all")
