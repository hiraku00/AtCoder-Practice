def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def lcm(a, b):
    return a * b // gcd(a, b)

def main():
    N, X, Y = map(int, input().split())
    cnt_X = N // X
    cnt_Y = N // Y
    lcm_XY = lcm(X, Y)
    cnt_XY = N // lcm_XY
    print(cnt_X + cnt_Y - cnt_XY)

if __name__ == "__main__":
    main()
