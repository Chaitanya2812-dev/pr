# Molecular Docking and Virtual Screening

import pandas as pd8

# 1. Create sample docking results
data = {
    "Ligand": ["Ligand A", "Ligand B", "Ligand C", "Ligand D"],
    "Binding Score": [-8.5, -7.2, -9.1, -6.8],
    "Hydrogen Bonds": [4, 2, 5, 1],
    "Hydrophobic Contacts": [8, 6, 10, 4]
}

df = pd.DataFrame(data)

print("Molecular Docking Results:")
print(df)

# 2. Rank ligands by binding score
# Lower (more negative) score is better
df = df.sort_values(by="Binding Score")

df["Rank"] = range(1, len(df) + 1)

# 3. Display ranked results
print("\nRanked Ligands:")
print(df)

# 4. Identify the best ligand
best = df.iloc[0]

print("\nBest Ligand:", best["Ligand"])
print("Binding Score:", best["Binding Score"])
print("Hydrogen Bonds:", best["Hydrogen Bonds"])
print("Hydrophobic Contacts:", best["Hydrophobic Contacts"])

# 5. Interpretation
print("\nBiological Interpretation:")
print(best["Ligand"],
      "has the most favorable binding score in this sample.")

print("Docking results are predictions and require experimental validation.")