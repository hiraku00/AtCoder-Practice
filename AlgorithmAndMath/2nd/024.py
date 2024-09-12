def calc_expectation(N):
    res = 0
    for _ in range(N):
        P, Q = list(map(int, input().split()))
        res += Q / P
    return res

def main():
    N = int(input())
    print(calc_expectation(N))

if __name__ == "__main__":
    main()
