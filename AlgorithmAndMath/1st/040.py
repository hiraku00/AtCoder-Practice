def calc(A, M, B):
    dist = 0
    for i in range(M-1):
        start, end = B[i]-1, B[i+1]-1
        if start < end:
            dist += sum(A[start:end])
        else:
            dist += sum(A[end:start])
    return dist

def main():
    N = int(input())
    A = list(map(int, input().split()))
    M = int(input())
    B = [int(input()) for _ in range(M)]
    print(calc(A, M, B))

if __name__ == "__main__":
    main()
