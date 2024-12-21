FROM python:3.11

# MeCab と関連パッケージをインストール
RUN apt-get update && \
apt-get install -y mecab libmecab-dev mecab-ipadic-utf8

# mecab-python3のインストール
RUN pip install mecab-python3
# Pythonでよく使うライブラリをインストール
RUN pip install numpy scikit-learn matplotlib pandas
