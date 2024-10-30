def calc_total_distance(A, M, B):
    distance = 0
    for i in range(M-1):
        start, end = B[i]-1, B[i+1]-1
        print(f'===================== i : {i}')
        print(f'start : {start}')
        print(f'end   : {end}')
        if start < end:
            distance += sum(A[start:end])
            print(f'sum(A[{start}:{end}]) : {sum(A[start:end])}')
        else:
            distance += sum(A[end:start])
            print(f'sum(A[{end}:{start}]) : {sum(A[end:start])}')
        print(f'distance    : {distance}')
    return distance

def main():
    _ = input()
    A = list(map(int, input().split()))
    M = int(input())
    B = [int(input()) for _ in range(M)]
    calc_total_distance(A, M, B)

if __name__ == "__main__":
    main()
