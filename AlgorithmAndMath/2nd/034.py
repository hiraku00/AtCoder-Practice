import math

def distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

def find_min_distance(points):
    min_distance = float('Inf')
    n = len(points)
    for i in range(n):
        for j in range(i+1, n):
            min_distance = min(min_distance, distance(points[i], points[j]))
    return min_distance

def main():
    N = int(input())
    points = [tuple(map(int, input().split())) for _ in range(N)]
    print(find_min_distance(points))

if __name__ == "__main__":
    main()
