def matrix_multiply(a, b, mod):
    return [
        [(a[0][0]*b[0][0] + a[0][1]*b[1][0]) % mod, (a[0][0]*b[0][1] + a[0][1]*b[1][1]) % mod],
        [(a[1][0]*b[0][0] + a[1][1]*b[1][0]) % mod, (a[1][0]*b[0][1] + a[1][1]*b[1][1]) % mod]
    ]

def matrix_power(matrix, n, mod):
    result = [[1, 0], [0, 1]]
    while n > 0:
        if n % 2 == 1:
            result = matrix_multiply(result, matrix, mod)
        matrix = matrix_multiply(matrix, matrix, mod)
        n //= 2
    return result

def fibonacci_mod(n):
    if n <= 1:
        return n
    MOD = 10**9 + 7
    matrix = [[1, 1], [1, 0]]
    result = matrix_power(matrix, n - 1, MOD)
    return result[0][0]

def main():
    N = int(input())
    print(fibonacci_mod(N))

if __name__ == "__main__":
    main()

# ===========
# 遅い
# ↓
# def fibonacchi_mod(n):
#     MOD = 10**9 + 7
#     a, b = 0, 1
#     for _ in range(n):
#         a, b = b, (a+b) % MOD
#     return a

# def main():
#     N = int(input())
#     print(fibonacchi_mod(N))

# if __name__ == "__main__":
#     main()
