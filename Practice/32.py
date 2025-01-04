import numpy as np
import pandas as pd
from statsmodels.graphics.tsaplots import plot_acf
import matplotlib.pyplot as plt

# # グラフを描画する前にフォントを設定
# plt.rcParams['font.family'] = ['IPAexGothic']

# import matplotlib.font_manager as fm

# font_list = fm.findSystemFonts(fontpaths=None, fontext='ttf')
# print("利用可能なフォントリスト:")
# for font in font_list:
#     print(font)

# # シンプルなグラフを作成
# plt.plot([1, 2, 3], [4, 5, 6])
# plt.title("日本語タイトル")
# plt.xlabel("日本語X軸")
# plt.ylabel("日本語Y軸")
# plt.show()

def calculate_autocorrelation(data: np.ndarray, maxlag: int) -> np.ndarray:
    """
    自己相関を計算する関数

    Args:
        data: 時系列データ (numpy.ndarray)
        maxlag: 最大ラグ (int)

    Returns:
        自己相関係数の配列 (numpy.ndarray)
    """
    autocorr = np.correlate(data, data, mode='full')
    autocorr = autocorr[autocorr.size//2 : autocorr.size//2 + maxlag+1]
    return autocorr / autocorr[0]

def find_max_autocorrelation_lag(autocorr: np.ndarray) -> int or None:
    """
    自己相関係数が最大となるラグを返す関数

    Args:
        autocorr: 自己相関係数の配列 (numpy.ndarray)

    Returns:
        最大のラグ (int) または データが不十分な場合は None
    """
    if len(autocorr) <= 1:
        return None
    max_lag_index = np.argmax(autocorr[1:]) + 1
    return max_lag_index

if __name__ == "__main__":
    try:
        # データの読み込み
        df = pd.read_csv("https://raw.githubusercontent.com/aweglteo/tokyo_weather_data/main/data.csv", parse_dates=True, index_col=0)
    except Exception as e:
        print(f"データの読み込み中にエラーが発生しました: {e}")
        exit()

    # 分析対象の列
    target_column = "ave_tmp"

    if target_column not in df.columns:
        print(f"エラー：指定された列 '{target_column}' はデータフレームに存在しません。")
        exit()

    # NaN値を処理
    data = df[target_column].dropna().values

    # 最大ラグの設定
    max_lag = 40

    # 自己相関の計算
    autocorr = calculate_autocorrelation(data, max_lag)

    # 最大のラグ
    max_lag_index = find_max_autocorrelation_lag(autocorr)
    if max_lag_index is not None:
        print(f"'{target_column}' の自己相関係数が最大となるタイムラグ: {max_lag_index} 日")
    else:
        print("自己相関を計算するのに十分なデータがありません。")

    # 自己相関プロット (statsmodelsを使用)
    fig, ax = plt.subplots(figsize=(10, 6))
    plot_acf(data, lags=max_lag, ax=ax, title=f"{target_column}の自己相関プロット (statsmodels)")
    plt.show()
