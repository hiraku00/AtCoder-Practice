def answer(calmulative_sum, LR):
    for L, R in LR:
        print(calmulative_sum[R] - calmulative_sum[L-1])

def calc_cumulative_sum(N, A):
    calmulative_sum = [0] * (N+1)
    for i in range(N):
        calmulative_sum[i+1] = calmulative_sum[i] + A[i]
    return calmulative_sum

def main():
    N, Q = map(int, input().split())
    A = list(map(int, input().split()))
    LR = [tuple(map(int, input().split())) for _ in range(Q)]
    calmulative_sum = calc_cumulative_sum(N, A)
    answer(calmulative_sum, LR)

if __name__ == "__main__":
    main()
