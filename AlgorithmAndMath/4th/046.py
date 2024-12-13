from collections import deque

def bfs(R, C, maze, start, goal):
    # 4方向（上、下、左、右）
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    # 各マスへの最小手数を記録する2Dリスト
    dist = [[-1] * C for _ in range(R)]
    # 探索対象のマスを格納するキュー
    queue = deque([start])
    # スタート地点の初期化
    dist[start[0]][start[1]] = 0

    while queue:
        y, x = queue.popleft()
        if (y, x) == goal:
            return dist[y][x]
        for dy, dx in directions:
            ny, nx = y + dy, x + dx
            if 0 <= ny < R and 0 <= nx < C and \
                maze[ny][nx] != '#' and dist[ny][nx] == -1:
                queue.append((ny, nx))
                dist[ny][nx] = dist[y][x] + 1
    return -1

def main():
    R, C = map(int, input().split())
    sy, sx = map(int, input().split())
    gy, gx = map(int, input().split())
    maze = [list(input()) for _ in range(R)]
    start = (sy - 1, sx - 1)
    goal = (gy - 1, gx - 1)
    print(bfs(R, C, maze, start, goal))

if __name__ == "__main__":
    main()
