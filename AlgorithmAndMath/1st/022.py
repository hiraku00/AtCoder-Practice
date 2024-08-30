def pair(A):
    D = [0]*100000
    res = 0
    for a in A:
        res += D[a]
        D[-a] += 1
    return res

def main():
    N = input()
    A = list(map(int, input().split()))
    print(pair(A))

if __name__ == "__main__":
    main()
