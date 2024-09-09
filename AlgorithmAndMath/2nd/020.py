def calc(A):
    dp = [[0] * 1001 for _ in range(6)]
    dp[0][0] = 1

    for num in A:
        for k in range(4, -1, -1):
            for s in range(1000 - num + 1):
                dp[k + 1][s + num] += dp[k][s]
    return dp[5][1000]

def main():
    N = int(input())
    A = list(map(int, input().split()))
    print(calc(A))

if __name__ == "__main__":
    main()
