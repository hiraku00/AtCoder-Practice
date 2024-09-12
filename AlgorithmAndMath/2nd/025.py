def calc_expectation(A, B):
    return (sum(A) / 3) + (sum(B) * 2 / 3)

def main():
    N = int(input())
    A = map(int, input().split())
    B = map(int, input().split())
    print(calc_expectation(A, B))

if __name__ == "__main__":
    main()
