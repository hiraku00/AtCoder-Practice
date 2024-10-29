def output(N, cumulative_sum):
    res = []
    for i in range(1, N):
        if cumulative_sum[i] > 0:
            res.append('<')
        elif cumulative_sum[i] == 0:
            res.append('=')
        else:
            res.append('>')
    return res

def calc_cumulative_sum(N, items):
    cumulative_sum = [0] * (N+1)
    for L, R, X in items:
        cumulative_sum[L-1] += X
        cumulative_sum[R] -= X
    return cumulative_sum

def main():
    N, Q = map(int, input().split())
    items = [list(map(int, input().split())) for _ in range(Q)]
    cumulative_sum = calc_cumulative_sum(N, items)
    return print(''.join(output(N, cumulative_sum)))

if __name__ == "__main__":
    main()
