import math

def find_min_distance(N, points):
    min_distance = float('Inf')
    for i in range(N):
        for j in range(i+1, N):
            x1, y1 = points[i]
            x2, y2 = points[j]
            distance = math.sqrt((x2-x1)**2 + (y2-y1)**2)
            if distance < min_distance:
                min_distance = distance
    return min_distance

def main():
    N = int(input())
    points = [tuple(map(int, input().split())) for _ in range(N)]
    print(find_min_distance(N, points))

if __name__ == "__main__":
    main()
