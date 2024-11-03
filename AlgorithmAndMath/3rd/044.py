from collections import deque

def bfs(N, graph):
    dist = [-1] * (N+1)
    dist[1] = 0
    queue = deque([1])

    while queue:
        v = queue.popleft()
        print(f'============================ v : {v}')
        print(f'queue : {queue}')
        print(f'graph[{v}] : {graph[v]}')
        for nv in graph[v]:
            print(f'------------------- nv : {nv}')
            print(f'dist[{nv}] : {dist[nv]}')
            if dist[nv] == -1:
                dist[nv] = dist[v] + 1
                queue.append(nv)
                print(f'dist[{v}] + 1 : {dist[v] + 1}')
                print(f'dist : {dist}')
        print(f'queue : {queue}')
    return dist[1:]

def build_graph(N, edges):
    graph = [[] for _ in range(N+1)]
    for a, b in edges:
        graph[a].append(b)
        graph[b].append(a)
        print(f'**************************** a, b : {a}, {b}')
        print(graph)
    return graph

def main():
    N, M = map(int, input().split())
    edges = [list(map(int, input().split())) for _ in range(M)]
    graph = build_graph(N, edges)
    dist = bfs(N, graph)
    print(*dist, sep='\n')

if __name__ == "__main__":
    main()
