from collections import deque

def find_min_digit_sum(K):
    # 初期化：全ての位置について、最小桁和を無限大に設定
    dist = [10**9] * K
    # 1の位置の最小桁和を1に設定
    dist[1] = 1
    q = deque()
    q.append(1)
    while q:
        pos = q.popleft()
        # 現在の位置から1増やす操作（u）と10倍する操作（v）を考える
        u = (pos + 1) % K
        v = 10 * pos % K

        # uへの移動が可能（最小桁和が更新される）ならば、distとキューを更新
        if dist[u] > dist[pos] + 1:
            dist[u] = dist[pos] + 1
            q.append(u)

        # vへの移動が可能（最小桁和が更新される）ならば、distとキューを更新
        if dist[v] > dist[pos]:
            dist[v] = dist[pos]
            q.append(v)
    return dist[0]

def main():
    K = int(input())
    print(find_min_digit_sum(K))

if __name__ == "__main__":
    main()
