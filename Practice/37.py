import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Dataset URL
url = "https://archive.ics.uci.edu/ml/machine-learning-databases/wine/wine.data"

# Column names
column_names = [
    "Class",
    "Alcohol",
    "Malic acid",
    "Ash",
    "Alcalinity of ash",
    "Magnesium",
    "Total phenols",
    "Flavanoids",
    "Nonflavanoid phenols",
    "Proanthocyanins",
    "Color intensity",
    "Hue",
    "OD280/OD315 of diluted wines",
    "Proline",
]

# Load the dataset
wine_data = pd.read_csv(url, names=column_names)
print(wine_data.head())

# Map class labels (optional)
class_mapping = {1: "class_0", 2: "class_1", 3: "class_2"}
wine_data["Class"] = wine_data["Class"].map(class_mapping)

# Display the head of the dataset
print("Head of the dataset:")
print(wine_data.head())

# -------------------- Histogram Creation --------------------
print("\n--- Histogram Creation ---")
# List of features (excluding the class label)
features = wine_data.columns.drop('Class')

# Display histograms for each feature
wine_data[features].hist(figsize=(12, 10))
plt.suptitle("Histograms of Each Feature", fontsize=16)
plt.tight_layout(rect=[0, 0.03, 1, 0.95])
plt.show()

# Display histograms by wine class
for feature in features:
    plt.figure(figsize=(8, 6))
    sns.histplot(data=wine_data, x=feature, hue='Class', kde=True)
    plt.title(f'Histogram of {feature} (by Wine Class)')
    plt.xlabel(feature)
    plt.ylabel('Frequency')
    plt.show()

# -------------------- Heatmap Creation --------------------
print("\n--- Heatmap Creation ---")
# Calculate the correlation matrix
correlation_matrix = wine_data[features].corr()

# Display the heatmap
plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f")
plt.title("Correlation Heatmap of Features")
plt.show()

# Display heatmaps by wine class
for wine_class in wine_data['Class'].unique():
    subset_data = wine_data[wine_data['Class'] == wine_class]
    correlation_matrix_subset = subset_data[features].corr()

    plt.figure(figsize=(10, 8))
    sns.heatmap(correlation_matrix_subset, annot=True, cmap='coolwarm', fmt=".2f")
    plt.title(f"Correlation Heatmap of Features for {wine_class}")
    plt.show()
