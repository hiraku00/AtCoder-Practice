class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n
        self.size = n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        rx, ry = self.find(x), self.find(y)
        if rx == ry:
            return
        if self.rank[rx] < self.rank[ry]:
            self.parent[rx] = ry
        elif self.rank[rx] > self.rank[ry]:
            self.parent[ry] = rx
        else:
            self.parent[ry] = rx
            self.rank[rx] += 1
        self.size -= 1

def is_connected(n, edges):
    uf = UnionFind(n)
    for a, b in edges:
        uf.union(a-1, b-1)
    return uf.size == 1

def main():
    N, M = map(int, input().split())
    edges = [tuple(map(int, input().split())) for _ in range(M)]

    if is_connected(N, edges):
        print("The graph is connected.")
    else:
        print("The graph is not connected.")

if __name__ == "__main__":
    main()
