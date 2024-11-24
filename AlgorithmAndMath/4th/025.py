def calc_expectation(A, B):
    return sum(A)*2/6 + sum(B)*4/6

def main():
    _ = int(input())
    A = map(int, input().split())
    B = map(int, input().split())
    print(calc_expectation(A, B))

if __name__ == "__main__":
    main()
