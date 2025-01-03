import speech_recognition as sr

def recognize_speech_and_save():
    """マイクからの音声を取得し、認識した言葉をテキストファイルに保存する関数"""
    r = sr.Recognizer()
    mic = sr.Microphone()

    print("音声認識を開始します。話しかけてください...")

    with mic as source:
        r.adjust_for_ambient_noise(source)  # 周囲の騒音を調整
        audio = r.listen(source)

    try:
        print("認識中...")
        # Google Web Speech APIを使用して音声認識
        recognized_text = r.recognize_google(audio, language='ja-JP')
        print(f"認識結果: {recognized_text}")

        # 認識したテキストをファイルに保存
        with open("recognized_text.txt", "a", encoding="utf-8") as f:
            f.write(recognized_text + "\n")
        print("認識結果を recognized_text.txt に保存しました。")

    except sr.UnknownValueError:
        print("音声を認識できませんでした。")
    except sr.RequestError as e:
        print(f"Google Speech Recognitionサービスに接続できませんでした; {e}")

if __name__ == "__main__":
    recognize_speech_and_save()
