from collections import deque

def bfs(N, M, edges):
    graph = [[] for _ in range(N+1)]
    for A, B in edges:
        graph[A].append(B)
        graph[B].append(A)

    dist = [-1] * (N+1)
    dist[1] = 0
    queue = deque([1])
    while queue:
        v = queue.popleft()
        for nv in graph[v]:
            if dist[nv] == -1:
                dist[nv] = dist[v] + 1
                queue.append(nv)
    return dist[1:]

def main():
    N, M = map(int, input().split())
    edges = [list(map(int, input().split())) for _ in range(M)]
    dist = bfs(N, M, edges)
    for d in dist:
        print(d)

if __name__ == "__main__":
    main()
