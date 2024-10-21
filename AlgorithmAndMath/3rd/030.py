def knapsack(N, W, items):
    dp = [0] * (W+1)
    for w, v in items:
        print(f'======================== w, v : {w}, {v}')
        for i in range(W, w-1, -1):
            print(f'----------------- i : {i}')
            print(f'dp[{i}]    : {dp[i]}')
            print(f'dp[{i-w}]    : {dp[i-w]}')
            print(f'dp[{i-w}]+{v} : {dp[i-w]+v}')
            dp[i] = max(dp[i], dp[i-w]+v)
        print(f'dp : {dp}')
    return dp[-1]

def main():
    N, W = map(int, input().split())
    items = [list(map(int, input().split())) for _ in range(N)]
    print(knapsack(N, W, items))

if __name__ == "__main__":
    main()
