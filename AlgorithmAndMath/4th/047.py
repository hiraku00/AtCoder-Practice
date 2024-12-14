from collections import deque

def build_graph(n, edges):
    graph = [[] for _ in range(n)]
    for a, b in edges:
        graph[a-1].append(b-1)
        graph[b-1].append(a-1)
    print(f'graph : {graph}')
    return graph

def is_bipartite_graph(N, edges):
    graph = build_graph(N, edges)

    color = [0] * len(graph)

    def dfs(node, color):
        queue = deque([node])
        color[node] = 1
        while queue:
            node = queue.popleft()
            for neighbor in graph[node]:
                if color[neighbor] == 0:
                    color[neighbor] = -color[node]
                    queue.append(neighbor)
                elif color[neighbor] == color[node]:
                    return False
        return True

    for i in range(N):
        if color[i] == 0:
            if not dfs(i, color):
                return 'No'
    return 'Yes'

def main():
    N, M = map(int, input().split())
    edges = [list(map(int, input().split())) for _ in range(M)]
    print(is_bipartite_graph(N, edges))

if __name__ == "__main__":
    main()
