import math

def calc(A, B, H, M):
    angle_H = 360 * (H / 12) + 30 * (M / 60)
    angle_M = 360 * (M / 60)
    angle_diff = abs(angle_H - angle_M)
    if angle_diff > 180:
        angle_diff = 360 - angle_diff
    angle_rad = math.radians(angle_diff)
    return math.sqrt(A**2 + B**2 - 2*A*B*math.cos(angle_rad))

def main():
    A, B, H, M = map(int, input().split())
    print(calc(A, B, H, M))

if __name__ == "__main__":
    main()
