def count_combination(N, S):
    cnt = 0
    for red in range(1, N+1):
        max_blue = min(N, S - red)
        if max_blue >= 1:
            cnt += max_blue
        else:
            break
    return cnt

def main():
    N, S = map(int, input().split())
    print(count_combination(N, S))

if __name__ == "__main__":
    main()
