def calc_cumulative_sum(N, LRX):
    cumulative_sum = [0] * (N+1)
    for l, r, x in LRX:
        cumulative_sum[l-1] += x
        cumulative_sum[r] -= x
    return cumulative_sum

def output(N, cumulative_sum):
    res = []
    for i in range(1, N):
        if cumulative_sum[i] > 0:
            res.append("<")
        elif cumulative_sum[i] == 0:
            res.append("=")
        else:
            res.append(">")
    return print(''.join(res))

def main():
    N, Q = map(int, input().split())
    LRX = [list(map(int, input().split())) for _ in range(Q)]
    cumulative_sum = calc_cumulative_sum(N, LRX)
    output(N, cumulative_sum)

if __name__ == "__main__":
    main()
