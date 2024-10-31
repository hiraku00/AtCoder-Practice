def count_employees(T, LR):
    cnt = [0] * (T+1)
    for L, R in LR:
        cnt[L] += 1
        cnt[R] -= 1
    return cnt

def output(T, cnt):
    res = 0
    for i in range(T):
        res += cnt[i]
        print(res)

def main():
    T = int(input())
    N = int(input())
    LR = [list(map(int, input().split())) for _ in range(N)]
    cnt = count_employees(T, LR)
    output(T, cnt)

if __name__ == "__main__":
    main()
