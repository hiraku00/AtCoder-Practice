def main():
    N = int(input())
    B = list(map(int, input().split()))
    R = list(map(int, input().split()))
    print((sum(B)+sum(R))/N)

if __name__ == "__main__":
    main()
