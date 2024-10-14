def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def lcm(A):
    res = A[0]
    for i in A[1:]:
        res = (res * i) // gcd(res, i)
    return res

def main():
    _ = input()
    A = list(map(int, input().split()))
    print(lcm(A))

if __name__ == "__main__":
    main()
