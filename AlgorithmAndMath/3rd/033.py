import numpy as np
import math

def vector_subtract(v1, v2):
    return [v1[0]-v2[0], v1[1]-v2[1]]

def distance(p1, p2):
    return math.sqrt((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)

def shortest_distance(A, B, C):
    BA = vector_subtract(A, B)
    BC = vector_subtract(C, B)
    CA = vector_subtract(A, C)
    CB = vector_subtract(B, C)

    if np.dot(BA, BC) < 0:
        nearest = B
    elif np.dot(CA, CB) < 0:
        nearest = C
    else:
        t = np.dot(BA, BC) / np.dot(BC, BC)
        nearest = [B[0] + t * BC[0], B[1] + t * BC[1]]
    return distance(A, nearest)

def main():
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    C = list(map(int, input().split()))
    print(shortest_distance(A, B, C))

if __name__ == "__main__":
    main()
