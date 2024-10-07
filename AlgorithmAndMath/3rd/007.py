def gcd(x, y):
    while y != 0:
        x, y = y, x % y
    return x

def lcm(x, y):
    return x * y // gcd(x, y)

def count_multiples(N, X, Y):
    cnt_X = N // X
    cnt_Y = N // Y
    lcm_xy = lcm(X, Y)
    cnt_XY = N // lcm_xy
    return cnt_X + cnt_Y - cnt_XY

def main():
    N, X, Y = map(int, input().split())
    print(count_multiples(N, X, Y))

if __name__ == "__main__":
    main()
