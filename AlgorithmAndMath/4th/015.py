def gcd(A, B):
    while B != 0:
        A, B = B, A % B
    return A

def main():
    A, B = map(int, input().split())
    print(gcd(A, B))

if __name__ == "__main__":
    main()
