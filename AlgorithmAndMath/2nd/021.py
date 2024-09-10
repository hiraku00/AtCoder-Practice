def comb(n, r):
    r = min(r, n - r)
    res = 1
    for i in range(r):
        res = res * (n - i) // (i + 1)
    return res

def main():
    n, r = map(int, input().split())
    print(comb(n, r))

if __name__ == "__main__":
    main()
