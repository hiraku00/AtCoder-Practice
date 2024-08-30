from collections import deque

def bfs(maze, start, goal):
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    R, C = len(maze), len(maze[0])
    dist = [[-1] * C for _ in range(R)]
    queue = deque([start])
    dist[start[0]][start[1]] = 0
    while deque:
        y, x = queue.popleft()
        if (y, x) == goal:
            return dist[y][x]
        for dx, dy in directions:
            ny, nx = y + dy, x + dx
            if maze[ny][nx] != '#' and dist[ny][nx] == -1:
                queue.append((ny, nx))
                dist[ny][nx] = dist[y][x] + 1
    return -1

def main():
    R, C = map(int, input().split())
    sy, sx = map(int, input().split())
    gy, gx = map(int, input().split())
    maze = [list(input()) for _ in range(R)]
    start = (sy-1, sx-1)
    goal = (gy-1, gx-1)
    print(bfs(maze, start, goal))

if __name__ == "__main__":
    main()
