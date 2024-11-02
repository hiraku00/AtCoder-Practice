def dfs(N, graph):
    visited = [False] * N
    stack = [0]
    while stack:
        v = stack.pop()
        print(f'=============================================== v : {v}')
        print(f'stack : {stack}')
        print(f'visited[{v}] : {visited[v]}')
        if not visited[v]:
            visited[v] = True
            print(f'visited : {visited}')
            print(f'graph[{v}] : {graph[v]}')
            for nv in graph[v]:
                stack.append(nv)
        print(f'stack : {stack}')
    return all(visited)

def is_connected(N, edges):
    graph = [[] for _ in range(N)]
    for a, b in edges:
        graph[a-1].append(b-1)
        graph[b-1].append(a-1)
        print(f'*********************************** a, b : {a}, {b}')
        print(graph)
    return dfs(N, graph)

def main():
    N, M = map(int, input().split())
    edges = [list(map(int, input().split())) for _ in range(M)]
    if is_connected(N, edges):
        print('The graph is connected.')
    else:
        print('The graph is not connected.')

if __name__ == "__main__":
    main()
