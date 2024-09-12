def main():
    N = int(input())
    res = 0
    for _ in range(N):
        P, Q = map(int, input().split())
        res += Q/P
    print(res)

if __name__ == "__main__":
    main()
