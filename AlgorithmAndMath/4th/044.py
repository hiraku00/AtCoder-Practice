from collections import deque

def build_graph(n, edges):
    # グラフを隣接リストとして構築
    graph = [[] for _ in range(n)]
    for a, b in edges:
        graph[a-1].append(b-1)  # 0-indexed に調整
        graph[b-1].append(a-1)
    return graph

def bfs(graph, start, n):
    # 距離を記録するリスト (-1 は未到達を表す)
    distances = [-1] * n
    distances[start] = 0
    queue = deque([start])

    # 幅優先探索 (BFS)
    while queue:
        current = queue.popleft()
        for neighbor in graph[current]:
            if distances[neighbor] == -1:  # 未到達のノードを更新
                distances[neighbor] = distances[current] + 1
                queue.append(neighbor)
    return distances

def main():
    n, m = map(int, input().split())
    edges = [list(map(int, input().split())) for _ in range(m)]
    graph = build_graph(n, edges)
    dist = bfs(graph, 0, n)
    print(*dist, sep='\n')

if __name__ == "__main__":
    main()
