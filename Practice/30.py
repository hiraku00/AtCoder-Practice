import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split, cross_val_score, KFold
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.preprocessing import StandardScaler

# Wine recognition datasetの読み込み
# https://scikit-learn.org/stable/datasets/toy_dataset.html#wine-recognition-dataset
url = "https://archive.ics.uci.edu/ml/machine-learning-databases/wine/wine.data"
df = pd.read_csv(url, header=None)
df.columns = ['class', 'Alcohol', 'Malic acid', 'Ash', 'Alcalinity of ash', 'Magnesium', 'Total phenols', 'Flavanoids', 'Nonflavanoid phenols', 'Proanthocyanins', 'Color intensity', 'Hue', 'OD280/OD315 of diluted wines', 'Proline']

# データの先頭5行を表示して確認
print(df.head())

# 特徴量と目的変数の分離
X = df.drop('class', axis=1)
y = df['class']

# 分類モデルの選択 (例: ランダムフォレスト)
model = RandomForestClassifier(random_state=42)

# 交差検証の実行 (KFold)
kf = KFold(n_splits=5, shuffle=True, random_state=42)  # 5分割交差検証
cv_scores = cross_val_score(model, X, y, cv=kf, scoring='accuracy')

# 交差検証の結果表示
print("各分割の正解率:", cv_scores)
print("平均正解率:", cv_scores.mean())

# オプション: データセットを訓練データとテストデータに分割して最終評価
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# モデルの学習
model.fit(X_train, y_train)

# テストデータでの予測
y_pred = model.predict(X_test)

# テストデータの正解率
test_accuracy = accuracy_score(y_test, y_pred)
print("テストデータの正解率:", test_accuracy)

# 混同行列の表示
cm = confusion_matrix(y_test, y_pred)
plt.figure(figsize=(8, 6))
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues',
            xticklabels=df['class'].unique(),
            yticklabels=df['class'].unique())
plt.xlabel('Predicted Label')
plt.ylabel('True Label')
plt.title('Confusion Matrix')
plt.show()

# 特徴量の重要度
feature_importances = model.feature_importances_
feature_names = X.columns
indices = sorted(range(len(feature_importances)), key=lambda k: feature_importances[k], reverse=True)

plt.figure(figsize=(10, 6))
plt.bar(range(len(feature_importances)), feature_importances[indices], align='center')
plt.xticks(range(len(feature_importances)), [feature_names[i] for i in indices], rotation=45, ha='right')
plt.xlabel('Feature')
plt.ylabel('Importance')
plt.title('Feature Importance')
plt.tight_layout()
plt.show()

# # 特徴量ごとの分布 (クラスごとに色分け)
# for column in X.columns:
#     plt.figure(figsize=(8, 6))
#     sns.histplot(data=df, x=column, hue='class', kde=True, palette='viridis')
#     plt.title(f'Distribution of {column} by Class')
#     plt.show()

# # (オプション) 特徴量間の散布図行列
# sns.pairplot(df, hue='class', palette='viridis')
# plt.show()
