def count_valid_vertices(N, edges):
    cnt = [0] * (N+1)
    for a, b in edges:
        if a > b:
            cnt[a] += 1
        else:
            cnt[b] += 1
        print(f'cnt : {cnt}')
    return cnt.count(1)

def main():
    N, M = map(int, input().split())
    edges = [list(map(int, input().split())) for _ in range(M)]
    print(count_valid_vertices(N, edges))

if __name__ == "__main__":
    main()
