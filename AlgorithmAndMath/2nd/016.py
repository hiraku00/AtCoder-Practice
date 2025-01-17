def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def gcd_list(A):
    res = A[0]
    for i in A[1:]:
        res = gcd(res, i)
    return res

def main():
    N = int(input())
    A = list(map(int, input().split()))
    print(gcd_list(A))

if __name__ == "__main__":
    main()
