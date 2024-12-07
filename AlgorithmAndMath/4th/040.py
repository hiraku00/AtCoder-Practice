def calc_total_distance(N, A, M, B):
    cumulative_sum = [0] * (N)
    for i in range(N-1):
        cumulative_sum[i+1] = cumulative_sum[i] + A[i]

    dist = 0
    for i in range(M-1):
        start = B[i] - 1
        end = B[i+1] - 1
        dist += abs(cumulative_sum[start] - cumulative_sum[end])
    return dist

def main():
    N = int(input())
    A = list(map(int, input().split()))
    M = int(input())
    B = [int(input()) for _ in range(M)]
    print(calc_total_distance(N, A, M, B))

if __name__ == "__main__":
    main()
