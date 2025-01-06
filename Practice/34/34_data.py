import pandas as pd
import numpy as np

# 1. MovieLensデータセットの読み込み (ratings.csv)
ratings_df = pd.read_csv('ml-latest-small/ratings.csv')

# 2. 映画データの読み込み (movies.csv) - レコメンド結果に映画タイトルを表示するため
movies_df = pd.read_csv('ml-latest-small/movies.csv')

print("ratings_df の情報:")
print(ratings_df.info())
print("\nratings_df の先頭5行:")
print(ratings_df.head())
print("\nratings_df の統計量:")
print(ratings_df.describe())
print("\nratings_df の欠損値の数:")
print(ratings_df.isnull().sum())
print("\nratings_df のユニークなユーザー数:", ratings_df['userId'].nunique())
print("ratings_df のユニークな映画数:", ratings_df['movieId'].nunique())
print("\nratings_df の評価値の分布:")
print(ratings_df['rating'].value_counts().sort_index())

print("\nmovies_df の情報:")
print(movies_df.info())
print("\nmovies_df の先頭5行:")
print(movies_df.head())
print("\nmovies_df の欠損値の数:")
print(movies_df.isnull().sum())
print("\nmovies_df のユニークな映画数:", movies_df['movieId'].nunique())
print("\nmovies_df の genres のユニークな値:")
print(movies_df['genres'].nunique())
print("\nmovies_df の genres の上位10個:")
print(movies_df['genres'].value_counts().head(10))
