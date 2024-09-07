def dp(A):
    dp = [0] * 401
    count = 0
    for price in A:
        if price < 500:
            count += dp[500 - price]
        dp[price] += 1
    return count

def main():
    _ = input()
    A = map(int, input().split())
    print(dp(A))

if __name__ == "__main__":
    main()
