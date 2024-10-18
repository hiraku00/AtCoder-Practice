def calc_expectation(N):
    res = 0
    for i in range(N, 0, -1):
        res += N/i
        print(res)
    return res

def main():
    N = int(input())
    print(calc_expectation(N))

if __name__ == "__main__":
    main()
