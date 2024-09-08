def count_pairs(A):
    count = [A.count(color) for color in (1, 2, 3)]
    return sum(c * (c - 1) // 2 for c in count)

def main():
    N = int(input())
    A = list(map(int, input().split()))
    print(count_pairs(A))

if __name__ == "__main__":
    main()
