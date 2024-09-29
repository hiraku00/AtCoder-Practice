def is_connected(N, edges):
    graph = [[] for _ in range(N)]
    for a, b in edges:
        graph[a-1].append(b-1)
        graph[b-1].append(a-1)
    return dfs(graph, N)

def dfs(graph, N):
    visited = [False] *  N
    stack = [0]
    while stack:
        v = stack.pop()
        if not visited[v]:
            visited[v] = True
            for nv in graph[v]:
                stack.append(nv)
    return all(visited)

def main():
    N, M = map(int, input().split())
    edges = [tuple(map(int, input().split())) for _ in range(M)]
    if is_connected(N, edges):
        print("The graph is connected.")
    else:
        print("The graph is not connected.")

if __name__ == "__main__":
    main()
