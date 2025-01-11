import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.cluster import KMeans
import pandas as pd

# 1. Load the Iris dataset
iris = load_iris()
X = iris.data
y = iris.target

# Check the data
df_data = pd.DataFrame(iris.data, columns=iris.feature_names)
print(df_data.head())

# 2. Perform K-Means clustering
n_clusters = 3
kmeans = KMeans(n_clusters=n_clusters, random_state=0, n_init=10) # n_init: Number of time the k-means algorithm will be run with different centroid seeds.
kmeans.fit(X)
labels = kmeans.labels_
centers = kmeans.cluster_centers_

# 3. Visualize the clustering results
# Use the first two dimensions of the features for plotting
plt.figure(figsize=(8, 6))

# Plot the data points, colored by cluster
for i in range(n_clusters):
    plt.scatter(X[labels == i, 0], [X[labels == i, 1]], label=f'Cluster {i+1}')

# Plot the cluster centroids
plt.scatter(centers[:, 0], centers[:, 1], marker='x', s=200, color='red', label='Centroids')

plt.xlabel(iris.feature_names[0])
plt.ylabel(iris.feature_names[1])
plt.title('K-means Clustering of Iris Dataset')
plt.legend()
plt.show()

# Simple evaluation of the clustering results (optional)
# See the correspondence between actual species and clusters
import pandas as pd
df = pd.DataFrame({'Actual': iris.target_names[y], 'Predicted': labels})
print('\nSimple evaluation of the clustering results')
print(pd.crosstab(df['Actual'], df['Predicted'], rownames=['Actual'], colnames=['Predicted']))
