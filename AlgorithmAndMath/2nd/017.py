def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def lcm(a, b):
    return a * b // gcd(a, b)

def lcm_list(A):
    res = A[0]
    for i in A[1:]:
        res = lcm(res, i)
    return res

def main():
    N = int(input())
    A = list(map(int, input().split()))
    print(lcm_list(A))

if __name__ == "__main__":
    main()
