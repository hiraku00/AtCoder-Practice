import math

def calc(r1, r2, d):
    if d < abs(r1 - r2):
        return 1
    elif d == abs(r1 - r2):
        return 2
    elif abs(r1 - r2) < d < r1 + r2:
        return 3
    elif d == r1 + r2:
        return 4
    elif d > r1 + r2:
        return 5
    else:
        return None

def main():
    x1, y1, r1 = map(int, input().split())
    x2, y2, r2 = map(int, input().split())
    d = math.sqrt((x1-x2)**2 + (y1-y2)**2)
    print(calc(r1, r2, d))

if __name__ == "__main__":
    main()
