def calc(N, edges):
    cnt = [0] * (N+1)
    for a, b in edges:
        if a > b:
            cnt[a] += 1
        else:
            cnt[b] += 1
    return cnt.count(1)

def main():
    N, M = map(int, input().split())
    edges = [list(map(int, input().split())) for _ in range(M)]
    print(calc(N, edges))

if __name__ == "__main__":
    main()
