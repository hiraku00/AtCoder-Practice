def count(N, S):
    cnt = 0
    for A in range(1, N+1):
        max_B = min(N, S-A)
        if max_B >= 1:
            cnt += max_B
    return cnt

def main():
    N, S = map(int, input().split())
    print(count(N, S))

if __name__ == "__main__":
    main()
