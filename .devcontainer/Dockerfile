FROM python:3.11

# MeCab と関連パッケージをインストール (requirements.txt に含める場合は削除可能)
RUN apt-get update && \
    apt-get install -y mecab libmecab-dev mecab-ipadic-utf8

# .devcontainer/requirements.txt をコピーしてインストール
COPY .devcontainer/requirements.txt /tmp/requirements.txt
RUN pip install -r /tmp/requirements.txt

# アプリケーションのディレクトリを作成し、そこに移動
WORKDIR /app

# ホストのファイルをコンテナにコピー (プロジェクトルート全体をコピーすると仮定)
COPY .. /app

# ポート番号を指定
EXPOSE 5000

# Flask アプリケーションの実行
CMD ["python", "Practice/22/app.py"]
