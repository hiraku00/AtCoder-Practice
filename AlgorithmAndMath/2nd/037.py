def cross_product(x1, y1, x2, y2):
    return x1*y2 - x2*y1

def vector(a, b):
    return b[0]-a[0], b[1]-a[1]

def read_point():
    return list(map(int, input().split()))

def main():
    A = read_point()
    B = read_point()
    C = read_point()
    D = read_point()

    AB = vector(A, B)
    AC = vector(A, C)
    AD = vector(A, D)
    CD = vector(C, D)
    CA = vector(C, A)
    CB = vector(C, B)

    cp1 = cross_product(*AB, *AC)
    cp2 = cross_product(*AB, *AD)
    cp3 = cross_product(*CD, *CA)
    cp4 = cross_product(*CD, *CB)

    if A > B:
        A, B = B, A
    if C > D:
        C, D = D, C

    if cp1 == 0 and cp2 == 0 and cp3 == 0 and cp4 == 0:
        if max(A, C) <= min(B, D):
            print('Yes')
        else:
            print('No')
    else:
        if cp1 * cp2 <= 0 and cp3 * cp4 <= 0:
            print('Yes')
        else:
            print('No')

if __name__ == "__main__":
    main()
