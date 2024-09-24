def answer(N, snow):
    res = []
    for i in range(1, N):
        if snow[i] > 0:
            res.append('<')
        elif snow[i] == 0:
            res.append('=')
        else:
            res.append('>')
    return print(''.join(res))

def calc_cumulative_sum(N, items):
    snow = [0] * (N+1)
    for L, R, X in items:
        snow[L-1] += X
        snow[R] -= X
    return snow

def main():
    N, Q = map(int, input().split())
    items = [tuple(map(int, input().split())) for _ in range(Q)]
    snow = calc_cumulative_sum(N, items)
    answer(N, snow)

if __name__ == "__main__":
    main()
