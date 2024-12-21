def game():
    a = int(input("最小値 a を入力してください： "))
    b = int(input("最大値 b を入力してください： "))
    while a > b:
        print("b は a より大きい値を入力してください")
        b = int(input("最大値 b を入力してください： "))

    used_numbers = []

    player = 1
    while True:
        num = int(input(f"プレイヤー{player}の番です。数字を入力してください： "))
        if num < a or num > b:
            print(f' {a} 以上 {b} 以下の値を入力してください')
            continue
        if num in used_numbers:
            print(f'プレイヤー{player}の負けです。{num}はすでに言いました。')
            break
        used_numbers.append(num)
        if num == b:
            print(f'プレイヤー{player}の勝ちです。')
            break
        player = 3 - player

if __name__ == "__main__":
    game()
