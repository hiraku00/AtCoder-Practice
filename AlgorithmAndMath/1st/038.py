def calc_pre_sum(N, A):
    prefix_sum = [0] * (N+1)
    for i in range(1, N+1):
        prefix_sum[i] = prefix_sum[i-1] + A[i-1]
    return prefix_sum

def main():
    N, Q = map(int, input().split())
    A = list(map(int, input().split()))
    queries = [tuple(map(int, input().split())) for _ in range(Q)]
    # 累積和
    prefix_sum = calc_pre_sum(N, A)
    # 各クエリへの回答
    for L, R in queries:
        print(prefix_sum[R] - prefix_sum[L-1])

if __name__ == "__main__":
    main()
