FROM python:3.11

# MeCab と関連パッケージをインストール
RUN apt-get update && \
    apt-get install -y mecab libmecab-dev mecab-ipadic-utf8

# mecab-python3のインストール
RUN pip install mecab-python3
# Pythonでよく使うライブラリをインストール
RUN pip install numpy scikit-learn matplotlib pandas requests bs4

# # .devcontainer/requirements.txt をコピーしてインストール
# COPY .devcontainer/requirements.txt /tmp/requirements.txt
# RUN pip install -r /tmp/requirements.txt

# # アプリケーションのディレクトリを作成し、そこに移動
# WORKDIR /workspace

# # ホストのファイルをコンテナにコピー
# COPY . /workspace

# # ポート番号を指定
# EXPOSE 5000

# # Flask アプリケーションの実行
# CMD ["python", "Practice/22/app.py"]
