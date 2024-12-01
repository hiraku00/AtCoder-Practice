def find_min_distance(N, points):
    min_dist = float('Inf')
    for i in range(N):
        for j in range(i+1, N):
            x1, y1 = points[i]
            x2, y2 = points[j]
            dist = ((x1-x2)**2 + (y1-y2)**2)**0.5
            if dist < min_dist:
                min_dist = dist
    return min_dist

def main():
    N = int(input())
    points = [list(map(int, input().split())) for _ in range(N)]
    print(find_min_distance(N, points))

if __name__ == "__main__":
    main()
