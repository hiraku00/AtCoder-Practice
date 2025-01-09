import numpy as np
from sklearn.datasets import load_files
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.pipeline import Pipeline

# 今回は、事前にダウンロードしたIMDbデータセットをロードします。
# scikit-learnのload_files関数を利用して、フォルダ構造からデータを読み込みます。
reviews_train = load_files('./aclImdb/train', categories=['pos', 'neg'])
text_train, y_train = reviews_train.data, reviews_train.target

reviews_test = load_files('./aclImdb/test', categories=['pos', 'neg'])
text_test, y_test = reviews_test.data, reviews_test.target

# データセットの確認
print(f"訓練データ数: {len(text_train)}")
print(f"テストデータ数: {len(text_test)}")
print(f"クラスラベル (訓練データ): {np.unique(y_train)}")

# テキストデータのベクトル化とモデルの学習をPipelineで組み合わせる
pipeline = Pipeline([
    ('tfidf', TfidfVectorizer(
        stop_words='english',  # ストップワードの除去
        max_df=0.7,           # ドキュメント頻度が最大の70%を超える単語は無視
        min_df=5              # 少なくとも5つのドキュメントに現れる単語のみを考慮
    )),
    ('clf', LogisticRegression(solver='liblinear', random_state=42)) # ロジスティック回帰を使用
])

# モデルの訓練
pipeline.fit(text_train, y_train)

# 訓練データでの予測と評価
y_train_pred = pipeline.predict(text_train)
train_accuracy = accuracy_score(y_train, y_train_pred)
print(f"訓練データの正解率: {train_accuracy:.4f}")

# テストデータでの予測と評価
y_test_pred = pipeline.predict(text_test)
test_accuracy = accuracy_score(y_test, y_test_pred)
print(f"テストデータの正解率: {test_accuracy:.4f}")

# 目標性能の確認
train_goal_achieved = train_accuracy >= 0.90
test_goal_achieved = test_accuracy >= 0.85

print(f"訓練データの目標達成: {train_goal_achieved}")
print(f"テストデータの目標達成: {test_goal_achieved}")

# 必要に応じてモデルのチューニング (例: ハイパーパラメータの調整)
from sklearn.model_selection import GridSearchCV
parameters = {
    'tfidf__ngram_range': [(1, 1), (1, 2)],
    'clf__C': [0.1, 1, 10]
}
grid_search = GridSearchCV(pipeline, parameters, cv=5, n_jobs=-1)
grid_search.fit(text_train, y_train)
print(f"Best score: {grid_search.best_score_}")
print(f"Best parameters: {grid_search.best_params_}")

# 最適なパラメータで再度評価
best_pipeline = grid_search.best_estimator_
y_test_pred_best = best_pipeline.predict(text_test)
test_accuracy_best = accuracy_score(y_test, y_test_pred_best)
print(f"チューニング後のテストデータの正解率: {test_accuracy_best:.4f}")
