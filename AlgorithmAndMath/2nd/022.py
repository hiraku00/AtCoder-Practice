def count_pairs(A):
    count = {}
    res = 0
    for a in A:
        if 100000 - a in count:
            res += count[100000 - a]

        if a in count:
            count[a] += 1
        else:
            count[a] = 1
    return res

def main():
    N = int(input())
    A = map(int, input().split())
    print(count_pairs(A))

if __name__ == "__main__":
    main()
