def count_pairs(A):
    cnt = [A.count(color) for color in (1, 2, 3)]
    return sum(c * (c-1) // 2 for c in cnt)

def main():
    _ = input()
    A = list(map(int, input().split()))
    print(count_pairs(A))

if __name__ == "__main__":
    main()
