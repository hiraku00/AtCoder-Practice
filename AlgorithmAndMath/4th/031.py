def calc_max(N, A):
    dp = [0] * (N+1)
    dp[1] = A[0]
    print(f'dp : {dp}')
    for i in range(2, N+1):
        dp[i] = max(dp[i-1], dp[i-2] + A[i-1])
        print(f'============================ i : {i}')
        print(f'dp[{i-1}] : {dp[i-1]}')
        print(f'dp[{i-2}]+A[{i-1}] : {dp[i-2]} + {A[i-1]} = {dp[i-2]+A[i-1]}')
        print(f'dp : {dp}')
    return dp[-1]

def main():
    N = int(input())
    A = list(map(int, input().split()))
    print(calc_max(N, A))

if __name__ == "__main__":
    main()