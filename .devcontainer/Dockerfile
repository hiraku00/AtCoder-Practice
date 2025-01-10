FROM python:3.11

# MeCab と関連パッケージをインストール
RUN apt-get update && \
    apt-get install -y mecab libmecab-dev mecab-ipadic-utf8
# PyAudio関連
RUN apt-get install -y portaudio19-dev

# mecab-python3のインストール
RUN pip install mecab-python3
# Pythonでよく使うライブラリをインストール
RUN pip install numpy scikit-learn matplotlib pandas seaborn
# 追加
RUN pip install requests bs4 pillow Mecab
# PyTorchのインストール
RUN pip install torch torchvision torchaudio
# pygame
RUN pip install pygame
# flask, sqlalchemy
RUN pip install sqlalchemy Flask Flask-SQLAlchemy Flask-Migrate Flask-Login Werkzeug email_validator
# SpeechRecognition, PyAudio
RUN pip install SpeechRecognition PyAudio
# statsmodels
RUN pip install statsmodels
# selenium
RUN pip install selenium

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
