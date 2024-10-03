from collections import deque

def is_bipartite_graph(N, edges):
    graph = [[] for _ in range(N+1)]
    for a, b in edges:
        graph[a].append(b)
        graph[b].append(a)

    color = [0] * len(graph)

    def bfs(start):
        queue = deque([start])
        color[start] = 1
        while queue:
            node = queue.popleft()
            for neighbor in graph[node]:
                if color[neighbor] == 0:
                    color[neighbor] = -color[node]
                    queue.append(neighbor)
                elif color[neighbor] == color[node]:
                    return False
        return True

    for i in range(1, N+1):
        if color[i] == 0:
            if not bfs(i):
                return 'No'
    return 'Yes'

def main():
    N, M = map(int, input().split())
    edges = [tuple(map(int, input().split())) for _ in range(M)]
    print(is_bipartite_graph(N, edges))

if __name__ == "__main__":
    main()
