# 1. Import required libraries
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

# 2. Load dataset
df = pd.read_csv("Iris.csv")

print(df.head())

# 3. Select numerical features
X = df.drop(["Id", "Species"], axis=1)

# 4. Find optimal number of clusters using Elbow Method
wcss = []

for i in range(1, 11):
    kmeans = KMeans(n_clusters=i, random_state=42, n_init=10)
    kmeans.fit(X)
    wcss.append(kmeans.inertia_)

# Plot Elbow Graph
plt.plot(range(1, 11), wcss, marker='o')
plt.xlabel("Number of Clusters")
plt.ylabel("WCSS")
plt.title("Elbow Method")
plt.show()

# 5. Apply K-Means with 3 clusters
kmeans = KMeans(n_clusters=3, random_state=42, n_init=10)
df["Cluster"] = kmeans.fit_predict(X)

print("\nCluster Assignments:")
print(df[["Species", "Cluster"]].head(10))

# 6. Visualize clusters
plt.scatter(X["PetalLengthCm"], X["PetalWidthCm"],
            c=df["Cluster"], cmap="rainbow")

plt.xlabel("Petal Length")
plt.ylabel("Petal Width")
plt.title("K-Means Clustering on Iris Dataset")
plt.show()