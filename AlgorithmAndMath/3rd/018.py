def total_amount(A):
    TOTAL = 500
    dp = [0] * 401
    res = 0
    for price in A:
        if price < TOTAL:
            res += dp[TOTAL - price]
            dp[price] += 1
    return res

def main():
    _ = input()
    A = map(int, input().split())
    print(total_amount(A))

if __name__ == "__main__":
    main()
