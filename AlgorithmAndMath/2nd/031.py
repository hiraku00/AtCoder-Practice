def calc_vacation(N, A):
    dp = [0] * (N+1)
    dp[1] = A[0]
    for i in range(2, N+1):
        dp[i] = max(dp[i-1], dp[i-2]+A[i-1])
    return dp[-1]

def main():
    N = int(input())
    A = list(map(int, input().split()))
    print(calc_vacation(N, A))

if __name__ == "__main__":
    main()
