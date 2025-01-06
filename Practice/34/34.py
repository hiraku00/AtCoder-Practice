import pandas as pd
from sklearn.neighbors import NearestNeighbors
import numpy as np

# 1. MovieLensデータセットの読み込み
ratings_df = pd.read_csv('ml-latest-small/ratings.csv')
movies_df = pd.read_csv('ml-latest-small/movies.csv')

ratings_df.head()
movies_df.head()

# ユーザー-アイテム行列の作成
def create_user_item_matrix(ratings):
    return ratings.pivot_table(index='userId', columns='movieId', values='rating').fillna(0)

user_item_matrix = create_user_item_matrix(ratings_df)

# NearestNeighborsモデルの学習
knn = NearestNeighbors(metric='cosine', algorithm='brute')
knn.fit(user_item_matrix)

def get_user_ratings(user_id, ratings_df, movies_df):
    """
    特定のユーザーの評価履歴を取得する関数。
    """
    user_ratings = ratings_df[ratings_df['userId'] == user_id].merge(movies_df, on='movieId')
    return user_ratings[['movieId', 'title', 'rating']]

def recommend_movies(user_id, user_item_matrix, movies_df, knn, top_n=5, n_neighbors=10):
    """
    特定のユーザーに映画をレコメンドし、根拠となる情報も返す関数。
    """
    if user_id not in user_item_matrix.index:
        print(f"ユーザーID {user_id} は評価履歴がありません。")
        return None

    user_row = user_item_matrix.loc[[user_id]]
    distances, neighbor_indices = knn.kneighbors(user_row, n_neighbors=n_neighbors + 1) # 自分自身を含むため + 1

    # 類似ユーザーのIDと類似度を取得 (自分自身を除く)
    similar_users = pd.DataFrame({'neighborId': user_item_matrix.index[neighbor_indices.flatten()[1:]],
                                  'similarity': 1 - distances.flatten()[1:]})
    print(f"\nユーザーID {user_id} と類似度の高いユーザー:")
    print(similar_users)

    # 予測評価値の計算
    n_neighbors_for_pred = min(n_neighbors, len(similar_users))  # 類似ユーザー数がn_neighborsより少ない場合を考慮
    if n_neighbors_for_pred == 0:
        print("類似ユーザーが見つかりませんでした。人気映画からレコメンドします。")
        # 人気映画からレコメンド (例として平均評価の高い映画)
        mean_ratings = ratings_df.groupby('movieId')['rating'].mean().sort_values(ascending=False)
        popular_movies = movies_df[movies_df['movieId'].isin(mean_ratings.head(top_n).index)]
        return popular_movies.merge(mean_ratings, on='movieId').rename(columns={'rating': 'predicted_rating'})

    relevant_neighbors = similar_users['neighborId'].head(n_neighbors_for_pred)
    neighbor_ratings = user_item_matrix.loc[relevant_neighbors]

    # ユーザーがまだ評価していない映画を取得
    unrated_movie_ids = user_item_matrix.columns[user_item_matrix.loc[user_id] == 0]

    predicted_ratings = pd.Series(0.0, index=unrated_movie_ids)
    for movie_id in unrated_movie_ids:
        numerator = 0
        denominator = 0
        for neighbor_id in relevant_neighbors:
            similarity = similar_users[similar_users['neighborId'] == neighbor_id]['similarity'].iloc[0]
            rating = neighbor_ratings.at[neighbor_id, movie_id]
            numerator += similarity * rating
            denominator += abs(similarity)

        if denominator > 0:
            predicted_ratings[movie_id] = numerator / denominator

    print("\n予測評価値:")
    print(predicted_ratings.head(20))

    # レコメンド結果の作成
    recommended_movie_ids = predicted_ratings.sort_values(ascending=False).head(top_n).index
    recommended_movies = movies_df[movies_df['movieId'].isin(recommended_movie_ids)].copy()
    if not recommended_movies.empty:
        recommended_movies['predicted_rating'] = recommended_movies['movieId'].map(predicted_ratings)
    else:
        print("\nレコメンドできる映画が見つかりませんでした。")
        return None

    print("\n予測評価値 (上位):")
    print(predicted_ratings.sort_values(ascending=False).head(top_n))

    return recommended_movies.sort_values(by='predicted_rating', ascending=False)

if __name__ == "__main__":
    print("利用可能なユーザーID:")
    print(user_item_matrix.index.tolist())

    while True:
        try:
            user_id_input = int(input("レコメンドを実行するユーザーIDを入力してください (終了するには '0' を入力): "))
            if user_id_input == 0:
                break

            if user_id_input in user_item_matrix.index:
                print(f"\nユーザーID {user_id_input} の評価履歴:")
                user_ratings = get_user_ratings(user_id_input, ratings_df, movies_df)
                print(user_ratings)

                recommended = recommend_movies(user_id_input, user_item_matrix, movies_df, knn, top_n=10) # top_n を 10 に変更
                if recommended is not None:
                    print(f"\nユーザーID {user_id_input} へのレコメンド結果:")
                    print(recommended[['movieId', 'title', 'predicted_rating']])
            else:
                print("入力されたユーザーIDは存在しません。")
        except ValueError:
            print("有効な整数を入力してください。")
