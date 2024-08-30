def dynamic_programming(A):
    dp = [[0]*1001 for _ in range(6)]
    dp[0][0] = 1

    for card in A:
        for total in range(1000, -1, -1):
            for card_cnt in range(5, 0, -1):
                if total >= card:
                    dp[card_cnt][total] += dp[card_cnt - 1][total - card]
    return dp[5][1000]

def main():
    N = input()
    A = list(map(int, input().split()))
    print(dynamic_programming(A))

if __name__ == "__main__":
    main()
