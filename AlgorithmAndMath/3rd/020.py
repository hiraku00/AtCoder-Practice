def count_combination(A):
    dp = [[0]*1001 for _ in range(6)]
    dp[0][0] = 1

    for num in A:
        for i in range(4, -1, -1):
            for j in range(1000 - num + 1):
                dp[i+1][j+num] += dp[i][j]
    return dp[5][1000]

def main():
    _ = input()
    A = list(map(int, input().split()))
    print(count_combination(A))

if __name__ == "__main__":
    main()
