def cross_product(x1, y1, x2, y2):
    return x1 * y2 - x2 * y1

def vector(a, b):
    return b[0] - a[0], b[1] - a[1]

def read_point():
    return list(map(int, input().split()))

def are_segments_overlapping(A, B, C, D):
    """2つの線分が重なっているかどうかを判定する

    Args:
        A, B: 1つ目の線分の端点の座標
        C, D: 2つ目の線分の端点の座標

    Returns:
        bool: 重なっている場合True、そうでない場合False
    """
    # x座標の範囲が重なっているか
    overlap_x = max(A[0], C[0]) <= min(B[0], D[0])
    # y座標の範囲が重なっているか
    overlap_y = max(A[1], C[1]) <= min(B[1], D[1])
    # x座標とy座標の両方が重なっている場合のみTrue
    return overlap_x and overlap_y

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

    cp_ABAC = cross_product(*AB, *AC)
    cp_ABAD = cross_product(*AB, *AD)
    cp_CDCA = cross_product(*CD, *CA)
    cp_CDCB = cross_product(*CD, *CB)

    # 線分の端点の大小関係を調整
    if A > B:
        A, B = B, A
    if C > D:
        C, D = D, C

    if cp_ABAC == 0 and cp_ABAD == 0 and cp_CDCA == 0 and cp_CDCB == 0:
        # 線分が平行な場合、重なり判定を行う
        if are_segments_overlapping(A, B, C, D):
            print('Yes')
        else:
            print('No')
    else:
        # 線分が平行でない場合、外積を用いて交差判定を行う
        if cp_ABAC * cp_ABAD <= 0 and cp_CDCA * cp_CDCB <= 0:
            print('Yes')
        else:
            print('No')

if __name__ == "__main__":
    main()
