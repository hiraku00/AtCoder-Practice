def calc_expectation(N, B, R):
    return (sum(B) + sum(R)) / N

def main():
    N = int(input())
    B = map(int, input().split())
    R = map(int, input().split())
    print(calc_expectation(N, B, R))

if __name__ == "__main__":
    main()
