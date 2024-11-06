from collections import deque

def build_graph(N, edges):
    graph = [[] for _ in range(N+1)]
    for a, b in edges:
        graph[a].append(b)
        graph[b].append(a)
        print(f'************************************************************** a, b : {a}, {b}')
        print(graph)
    return graph

def is_bipartite_graph(N, edges):
    graph = build_graph(N, edges)

    color = [0] * len(graph)

    def bfs(start):
        queue = deque([start])
        color[start] = 1
        while queue:
            node = queue.popleft()
            print(f'====================================== node = {node}')
            print(f'queue = {queue}')
            print(f'color = {color}')
            for neighbor in graph[node]:
                print(f'----------------------- neighbor = {neighbor}')
                print(f'color[{neighbor}] = {color[neighbor]}')
                print(f'color[{node}] : {color[node]}')
                if color[neighbor] == 0:
                    color[neighbor] = -color[node]
                    queue.append((neighbor))
                    print(f'color[{neighbor}] : {color[neighbor]}')
                    print(f'queue = {queue}')
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
    edges = [list(map(int, input().split())) for _ in range(M)]
    print(is_bipartite_graph(N, edges))

if __name__ == "__main__":
    main()
