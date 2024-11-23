def count_pairs(A):
    cnt = {}
    res = 0
    for a in A:
        if 100000-a in cnt:
            res += cnt[100000-a]
        if a in cnt:
            cnt[a] += 1
        else:
            cnt[a] = 1
    return res

def main():
    _ = input()
    A = list(map(int, input().split()))
    print(count_pairs(A))

if __name__ == "__main__":
    main()
