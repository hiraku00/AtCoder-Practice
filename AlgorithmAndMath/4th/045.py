def build_graph(n, edges):
    graph = [[] for _ in range(n)]
    for a, b in edges:
        graph[a-1].append(b-1)
        graph[b-1].append(a-1)
    print(f'graph : {graph}')
    return graph

def count(n, graph):
    cnt = 0
    for i in range(n):
        print(f'============================== i : {i}')
        print(f'graph[{i}] : {graph[i]}')
        # 頂点 i の隣接頂点の中で、頂点 i より番号が小さいものが1つだけ存在する場合
        if sum(j < i for j in graph[i]) == 1:
            cnt += 1
        # smaller_neighbors = 0
        # for j in graph[i]:
        #     print(f'j : {j}')
        #     if j < i:
        #         smaller_neighbors += 1
        # print(f'smaller_neighbors : {smaller_neighbors}')
        # if smaller_neighbors == 1:
        #     cnt += 1
    return cnt

def main():
    n, m = map(int, input().split())
    edges = [list(map(int, input().split())) for _ in range(m)]
    graph = build_graph(n, edges)
    print(count(n, graph))

if __name__ == "__main__":
    main()
