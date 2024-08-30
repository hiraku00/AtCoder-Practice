def dp(S, A):
    dp = [1] + [0] * S
    for i in A:
        for j in range(S-i, -1, -1):
            if dp[j] == 1:
                dp[j+i] = 1
    return "Yes" if dp[-1] == 1 else "No"

def main():
    N, S = map(int, input().split())
    A = list(map(int, input().split()))
    print(dp(S, A))

if __name__ == "__main__":
    main()
