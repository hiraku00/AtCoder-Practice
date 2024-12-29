import MeCab

def extract_nouns(text, mecabrc_path):
    tagger = MeCab.Tagger(f"-r {mecabrc_path}")
    node = tagger.parseToNode(text)
    nouns = []
    while node:
        if node.feature.split(",")[0] == "名詞":
            nouns.append(node.surface)
        node = node.next
    return nouns

def get_noun_frequencies(nouns):
    dict_nouns = {}
    for noun in nouns:
        if noun in dict_nouns:
            dict_nouns[noun] += 1
        else:
            dict_nouns[noun] = 1
    return sorted(dict_nouns.items(), key=lambda x: x[1], reverse=True)

def display_top_n(sorted_nouns, n):
    for noun, count in sorted_nouns[:n]:
        print(f"{noun}: {count}")

def main():
    mecabrc_path = "/etc/mecabrc"
    file_path = "./data/sample.txt"
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            text = f.read()
    except FileNotFoundError:
        print(f"ファイルが見つかりません: {file_path}")
        exit()

    nouns = extract_nouns(text, mecabrc_path)
    if nouns:
        noun_frequencies = get_noun_frequencies(nouns)
        display_top_n(noun_frequencies, 10)

if __name__ == "__main__":
    main()
