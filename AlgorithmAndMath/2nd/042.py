def f(x):
    return x*(x+1) // 2

def sum_of_divisors(N):
    res = 0
    for i in range(1, int(N**0.5)+1):
        res += i * i + 2 * i * (f(N//i) - f(i))
    return res

def main():
    N = int(input())
    print(sum_of_divisors(N))

if __name__ == "__main__":
    main()

# =======================
# ↓遅い
# def f(x):
#     cnt = 0
#     for i in range(1, int(x**0.5)+1):
#         if x%i == 0:
#             # If x is a perfect square (e.g. 16, 25)
#             if i * i == x:
#                 cnt += 1
#             else:
#                 cnt += 2
#     return cnt

# def sum_f_k(N):
#     res = 0
#     for k in range(1, N+1):
#         res += k * f(k)
#     return res

# def main():
#     N = int(input())
#     print(sum_f_k(N))
