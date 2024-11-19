def gcd(A, B):
    while B != 0:
        A, B = B, A % B
    return A

def gcd_list(A):
    res = A[0]
    for i in A[1:]:
        res = gcd(res, i)
    return res

def main():
    _ = input()
    A = list(map(int, input().split()))
    print(gcd_list(A))

if __name__ == "__main__":
    main()
