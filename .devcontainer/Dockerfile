FROM python:3.11

# MeCab と関連パッケージをインストール
RUN apt-get update && \
    apt-get install -y mecab libmecab-dev mecab-ipadic-utf8

# mecab-python3のインストール
RUN pip install mecab-python3
# Pythonでよく使うライブラリをインストール
RUN pip install numpy scikit-learn matplotlib pandas

# # Flaskのインストール
# RUN pip install flask

# # アプリケーションのディレクトリ作成
# WORKDIR /app

# RUN ls -la #  ls -la コマンドを追加

# # ホストのファイルをコンテナにコピー (Practice/17の中身をコピー)
# # ビルドコンテキストから見たパスを指定
# COPY ./Practice/17 /app

# # ポート番号を指定
# EXPOSE 5000

# # Flask アプリケーションの実行
# CMD ["python", "app.py"]
