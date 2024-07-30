def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def lcm(a, b):
    return a * b // gcd(a,b)

def main():
    N = int(input())
    A = list(map(int, input().split()))
    res = A[0]
    for i in range(1, len(A)):
        res = lcm(res, A[i])
    return print(res)

if __name__ == "__main__":
    main()
