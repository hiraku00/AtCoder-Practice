def min_cost(N, h):
    dp = [0] * N
    dp[1] = abs(h[1]-h[0])
    print(f'dp : {dp}')
    for i in range(2, N):
        c1 = dp[i-1] + abs(h[i]-h[i-1])
        c2 = dp[i-2] + abs(h[i]-h[i-2])
        dp[i] = min(c1, c2)
        print(f'==============================')
        print(f'h[{i-2}] : {h[i-2]}')
        print(f'h[{i-1}] : {h[i-1]}')
        print(f'h[{i}] : {h[i]}')
        print(f'c1 : {c1}')
        print(f'c2 : {c2}')
        print(f'dp : {dp}')
    return dp[-1]

def main():
    N = int(input())
    h = list(map(int, input().split()))
    print(min_cost(N, h))

if __name__ == "__main__":
    main()
