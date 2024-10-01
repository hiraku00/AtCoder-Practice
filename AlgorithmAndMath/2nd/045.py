def count_valid_vertices(N, edges):
    count = [0] * (N + 1)
    for a, b in edges:
        if a > b:
            count[a] += 1
        else:
            count[b] += 1
    return count.count(1)

def main():
    N, M = map(int, input().split())
    edges = [tuple(map(int, input().split())) for _ in range(M)]
    print(count_valid_vertices(N, edges))

if __name__ == "__main__":
    main()
