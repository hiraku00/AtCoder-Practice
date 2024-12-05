def calc_cumulative_sum(N, A):
    cumulative_sum = [0] * (N+1)
    for i in range(N):
        cumulative_sum[i+1] = cumulative_sum[i] + A[i]
    return cumulative_sum

def output(LR, cumulative_sum):
    for L, R in LR:
        print(cumulative_sum[R] - cumulative_sum[L-1])

def main():
    N, Q = map(int, input().split())
    A = list(map(int, input().split()))
    LR = [list(map(int, input().split())) for _ in range(Q)]
    cumulative_sum = calc_cumulative_sum(N, A)
    output(LR, cumulative_sum)

if __name__ == "__main__":
    main()
