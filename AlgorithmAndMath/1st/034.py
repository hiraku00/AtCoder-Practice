import math

def distance(x1, y1, x2, y2):
    return math.sqrt((x1-x2)**2 + (y1-y2)**2)

def min_distance(points):
    min_dist = float('inf')
    for i in range(len(points)):
        for j in range(i+1, len(points)):
            dist = distance(points[i][0], points[i][1],
                            points[j][0], points[j][1])
            min_dist = min(min_dist, dist)
    return min_dist

def main():
    N = int(input())
    points = [tuple(map(int, input().split())) for _ in range(N)]
    print(min_distance(points))

if __name__ == "__main__":
    main()
