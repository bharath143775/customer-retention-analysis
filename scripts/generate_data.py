# 📜 scripts/generate_data.py
import pandas as pd
import numpy as np
import os

def generate_customer_data(seed=42, n=300, save_path="../data/processed/customer_data.csv"):
    np.random.seed(seed)

    # Simulate basic customer data
    data = pd.DataFrame({
        "CustomerID": np.arange(1, n+1),
        "TotalOrders": np.random.poisson(lam=2.5, size=n),
        "AvgOrderValue": np.random.normal(loc=600, scale=100, size=n).round(2),
        "DaysSinceLastPurchase": np.random.randint(10, 180, size=n)
    })

    # Define churn: Customers with <3 orders & 90+ days since last purchase
    data["IsChurned"] = ((data["DaysSinceLastPurchase"] > 90) & (data["TotalOrders"] < 3)).astype(int)

    # Create folder if it doesn't exist
    os.makedirs(os.path.dirname(save_path), exist_ok=True)

    # Save CSV
    data.to_csv(save_path, index=False)
    print(f"✅ Customer data saved to {save_path}")

if __name__ == "__main__":
    generate_customer_data()
