def min_cost(N, h):
    dp = [0] * N
    dp[1] = abs(h[1] - h[0])
    for i in range(2, N):
        cost1 = dp[i-1] + abs(h[i] - h[i-1])
        cost2 = dp[i-2] + abs(h[i] - h[i-2])
        dp[i] = min(cost1, cost2)
    return dp[-1]

def main():
    N = int(input())
    h = list(map(int, input().split()))
    print(min_cost(N, h))

if __name__ == "__main__":
    main()
