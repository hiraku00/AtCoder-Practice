from collections import deque

def bfs(R, C, maze, start, goal):
    # 4方向（右、左、下、上）
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    # 各マスへの最小手数を記録する2Dリスト
    dist = [[-1] * C for _ in range(R)]
    # 探索対象のマスを格納するキュー
    queue = deque([start])
    # スタート地点の初期化
    dist[start[0]][start[1]] = 0
    print(f'dist[start[0]] = {dist[start[0]]}')
    print(f'queue = {queue}')
    while deque:
        y, x = queue.popleft()
        print(f'======================================== y, x : {y}, {x}')
        if(y, x) == goal:
            return dist[y][x]
        for dx, dy in directions:
            ny, nx = y+dy, x+dx
            print(f'------------------------- dy, dx : {dy}, {dx}')
            print(f'ny, nx : {ny}, {nx}')
            print(f'maze[{ny}][{nx}] : {maze[ny][nx]}')
            print(f'dist[{ny}][{nx}] : {dist[ny][nx]}')
            if maze[ny][nx] != '#' and dist[ny][nx] == -1:
                queue.append((ny, nx))
                dist[ny][nx] = dist[y][x] + 1
                print(f'queue = {queue}')
                print(f'dist[{y}][{x}]] : {dist[y][x]}')
    return -1

def main():
    R, C = map(int, input().split())
    sy, sx = map(int, input().split())
    gy, gx = map(int, input().split())
    maze = [list(input()) for _ in range(R)]
    start = (sy-1, sx-1)
    goal = (gy-1, gx-1)
    print(bfs(R, C, maze, start, goal))

if __name__ == "__main__":
    main()
