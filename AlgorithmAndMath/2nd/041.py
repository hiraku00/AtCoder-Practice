def count_employees(T, items):
    diff = [0] * (T+1)
    for L, R in items:
        diff[L] += 1
        diff[R] -= 1

    res = 0
    for i in range(T):
        res += diff[i]
        print(res)

def main():
    T = int(input())
    N = int(input())
    items = [tuple(map(int, input().split())) for _ in range(N)]
    print(count_employees(T, items))

if __name__ == "__main__":
    main()
