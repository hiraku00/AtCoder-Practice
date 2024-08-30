from collections import deque

def is_bipartite_graph(N, edges):
    graph = [[] for _ in range(N+1)]
    for A, B in edges:
        graph[A].append(B)
        graph[B].append(A)
    # 各頂点の色を記録するリスト
    # （0: 未訪問, 1: 色1, -1: 色2）
    color = [0] * len(graph)

    def bfs(start):
        queue = deque([start])
        color[start] = 1
        while queue:
            node = queue.popleft()
            for neighbor in graph[node]:
                # 未訪問の頂点
                if color[neighbor] == 0:
                    # 隣接する頂点は異なる色で塗る
                    color[neighbor] = -color[node]
                    queue.append(neighbor)
                # 同じ色の隣接頂点がある場合
                elif color[neighbor] == color[node]:
                    return False
        return True

    # 全ての頂点をチェック
    for i in range(1, N+1):
        # 未訪問の頂点から探索を開始
        if color[i] == 0:
            if not bfs(i):
                return 'No'
    return 'Yes'

def main():
    N, M  = map(int, input().split())
    edges = [list(map(int, input().split())) for _ in range(M)]
    print(is_bipartite_graph(N, edges))

if __name__ == "__main__":
    main()
