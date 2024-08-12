import numpy as np
import math

def calc(A, B, C):
    BA = [A[0] - B[0], A[1] - B[1]]
    BC = [C[0] - B[0], C[1] - B[1]]
    CA = [A[0] - C[0], A[1] - C[1]]
    CB = [B[0] - C[0], B[1] - C[1]]

    if np.dot(BA, BC) < 0:
        nearest = B
    elif np.dot(CA, CB) < 0:
        nearest = C
    else:
        nearest = [B[0] + np.dot(BA, BC) / (BC[0]**2 + BC[1]**2) * BC[0],
                   B[1] + np.dot(BA, BC) / (BC[0]**2 + BC[1]**2) * BC[1]]
    res = math.sqrt((nearest[0] - A[0])**2 + (nearest[1] - A[1])**2)
    return res

def main():
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    C = list(map(int, input().split()))
    print(calc(A, B, C))

if __name__ == "__main__":
    main()
