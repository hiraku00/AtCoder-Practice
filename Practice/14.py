import MeCab

# mecabrcファイルのパスを直接指定
mecabrc_path = "/etc/mecabrc"

try:
    tagger = MeCab.Tagger(f"-r {mecabrc_path}")
    text = "Pythonはオープンソースのプログラミング言語であり、人工知能や機械学習などの分野で広く使われています。"
    node = tagger.parseToNode(text)
    nouns = []
    while node:
        if node.feature.split(",")[0] == "名詞":
            nouns.append(node.surface)
        node = node.next
    print(' '.join(nouns))

except RuntimeError as e:
    print(f"MeCabの初期化に失敗しました: {e}")
    exit()
