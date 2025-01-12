import numpy as np

def arange_square_matrix(n):
    return np.array([np.arange(i, n+i) for i in range(n)])

print(all(map(all,(arange_square_matrix(3) == np.array([[0,1,2],[1,2,3],[2,3,4]])))))
