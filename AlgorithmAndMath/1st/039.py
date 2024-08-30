def calc(N, items):
    snow = [0 for _ in range(N+1)]
    for L, R, X in items:
        snow[L-1] += X
        snow[R] -= X
    return snow

def out(N, snow):
    res = []
    for i in range(1, N):
        if snow[i] > 0:
            res.append('<')
        elif snow[i] == 0:
            res.append('=')
        else:
            res.append('>')
    return print(''.join(res))

def main():
    N, Q = map(int, input().split())
    items = [tuple(map(int, input().split())) for _ in range(Q)]
    snow = (calc(N, items))
    out(N, snow)

if __name__ == "__main__":
    main()
