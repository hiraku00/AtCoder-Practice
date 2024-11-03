from collections import deque

def build_graph(N, edges):
    graph = [[] for _ in range(N+1)]
    for a, b in edges:
        graph[a].append(b)
        graph[b].append(a)
    return graph

def bfs(N, graph):
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
    edges = [tuple(map(int, input().split())) for _ in range(M)]
    graph = build_graph(N, edges)
    dist = bfs(N, graph)
    print(*dist, sep='\n')

if __name__ == "__main__":
    main()
