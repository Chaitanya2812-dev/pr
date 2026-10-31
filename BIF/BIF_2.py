# RNA-Seq Data Analysis

import pandas as pd
import numpy as np

# 1. Load CSV file
df = pd.read_csv("rna_counts.csv")

print("RNA-Seq Dataset:")
print(df)

# 2. Calculate Fold Change
df["Fold Change"] = df["Treatment"] / df["Control"]

# 3. Calculate Log2 Fold Change
df["Log2FC"] = np.log2(df["Fold Change"])

# 4. Identify differentially expressed genes
df["Expression"] = df["Log2FC"].apply(
    lambda x: "Upregulated" if x >= 1
    else ("Downregulated" if x <= -1 else "Unchanged")
)

# 5. Display results
print("\nDifferential Gene Expression Results:")
print(df.round(2))

# 6. Biological interpretation
print("\nBiological Interpretation:")
for i, row in df.iterrows():
    print(row["Gene"], "-", row["Expression"],
          "-", row["Function"])

# 7. Summary
print("\nSummary")
print("Upregulated genes:", sum(df["Expression"] == "Upregulated"))
print("Downregulated genes:", sum(df["Expression"] == "Downregulated"))
print("Unchanged genes:", sum(df["Expression"] == "Unchanged"))