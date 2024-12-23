def remove_duplicates(a):
    return list(set(a))

if __name__ == '__main__':
    # テストケース1
    a1 = [1, 2, 2, 3, 4, 4, 5]
    b1 = remove_duplicates(a1)
    print(f"入力: {a1}, 出力: {b1}")  # 出力例: 入力: [1, 2, 2, 3, 4, 4, 5], 出力: [1, 2, 3, 4, 5] (順番は不定)

    # テストケース2
    a2 = [1, 1, 1, 1, 1]
    b2 = remove_duplicates(a2)
    print(f"入力: {a2}, 出力: {b2}")  # 出力例: 入力: [1, 1, 1, 1, 1], 出力: [1]

    # テストケース3
    a3 = [1, 2, 3, 4, 5]
    b3 = remove_duplicates(a3)
    print(f"入力: {a3}, 出力: {b3}")  # 出力例: 入力: [1, 2, 3, 4, 5], 出力: [1, 2, 3, 4, 5] (順番は不定)

    # テストケース4 (空のリスト)
    a4 = []
    b4 = remove_duplicates(a4)
    print(f"入力: {a4}, 出力: {b4}") # 出力例: 入力: [], 出力: []

    # テストケース5 (要素数が多い場合)
    import random
    a5 = [random.randint(1, 1000) for _ in range(50000)]  #要素数5万のリスト
    b5 = remove_duplicates(a5)
    print(f"入力リストの要素数: {len(a5)}, 重複を取り除いた後のリストの要素数: {len(b5)}") #出力例: 入力リストの要素数: 50000, 重複を取り除いた後のリストの要素数: 918 (要素数は毎回異なる)
