def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def main():
    A, B = map(int, input().split())
    print(gcd(A, B))

if __name__ == "__main__":
    main()
