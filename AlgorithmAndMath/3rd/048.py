from collections import deque

def min_digit_sum(K):
    # 各余りに対する最小の桁の和を保存する
    visited = [-1] * K
    queue = deque([(1 % K, 1)])  # (現在の余り, 桁の和)
    visited[1 % K] = 1

    while queue:
        remainder, digit_sum = queue.popleft()

        # 余りが 0 の場合、答えが見つかった
        if remainder == 0:
            return digit_sum

        # 次の状態を生成する（10 倍と 1 を足す操作）
        # この操作で次の余りを計算
        # 状態1: 10 * current + 0
        new_remainder = (remainder * 10) % K
        if visited[new_remainder] == -1:
            visited[new_remainder] = digit_sum
            queue.append((new_remainder, digit_sum))

        # 状態2: 10 * current + 1
        new_remainder = (remainder * 10 + 1) % K
        if visited[new_remainder] == -1:
            visited[new_remainder] = digit_sum + 1
            queue.append((new_remainder, digit_sum + 1))

def main():
    K = int(input())
    print(min_digit_sum(K))

if __name__ == "__main__":
    main()
