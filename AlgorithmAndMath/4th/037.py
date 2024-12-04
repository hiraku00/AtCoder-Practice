def cross_product(p1, p2, p3):
    """2D ベクトルの外積を計算"""
    return (p2[0] - p1[0]) * (p3[1] - p1[1]) - (p2[1] - p1[1]) * (p3[0] - p1[0])

def on_segment(p, q, r):
    """点 q が線分 pr の上にあるかを判定する (外積チェックは呼び出し元で行う)"""
    return (min(p[0], r[0]) <= q[0] <= max(p[0], r[0]) and
            min(p[1], r[1]) <= q[1] <= max(p[1], r[1]))

def segments_intersect(p1, q1, p2, q2):
    """2つの線分 (p1, q1) と (p2, q2) が交差するかを判定"""
    d1 = cross_product(p1, q1, p2)
    d2 = cross_product(p1, q1, q2)
    d3 = cross_product(p2, q2, p1)
    d4 = cross_product(p2, q2, q1)

    # 線分が交差する通常のケース
    if ((d1 > 0 and d2 < 0) or (d1 < 0 and d2 > 0)) and \
       ((d3 > 0 and d4 < 0) or (d3 < 0 and d4 > 0)):
        return True

    # 特殊ケース: 点が線分上にある
    if d1 == 0 and on_segment(p1, p2, q1): return True
    if d2 == 0 and on_segment(p1, q2, q1): return True
    if d3 == 0 and on_segment(p2, p1, q2): return True
    if d4 == 0 and on_segment(p2, q1, q2): return True

    # 平行かつ重なっている場合
    if d1 == 0 and d2 == 0:  # 平行
        if on_segment(p1, p2, q1) or on_segment(p1, q2, q1) or \
           on_segment(p2, p1, q2) or on_segment(p2, q1, q2):
            return True

    return False

def main():
    # 入力と出力
    p1 = list(map(int, input().split()))
    q1 = list(map(int, input().split()))
    p2 = list(map(int, input().split()))
    q2 = list(map(int, input().split()))

    if segments_intersect(p1, q1, p2, q2):
        print("Yes")
    else:
        print("No")

if __name__ == "__main__":
    main()
