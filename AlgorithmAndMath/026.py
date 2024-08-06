def calc(n):
    res = 0
    for i in range(n, 0, -1):
        res += n/i
    return res

def main():
    N = int(input())
    print(calc(N))

if __name__ == "__main__":
    main()
