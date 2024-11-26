def merge_sort(A):
    if len(A) <= 1:
        return A

    mid = len(A) // 2
    # print("===================================")
    # print(f'A[:mid] : {A[:mid]}')
    # print(f'A[mid:] : {A[mid:]}')
    left = merge_sort(A[:mid])
    right = merge_sort(A[mid:])
    return merge(left, right)

def merge(left, right):
    # print("----------------------")
    # print(f'left : {left}')
    # print(f'right : {right}')
    res = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            res.append(left[i])
            i += 1
        else:
            res.append(right[j])
            j += 1
        # print(f'res : {res}')
    res.extend(left[i:])
    res.extend(right[j:])
    return res

def main():
    _ = input()
    A = list(map(int, input().split()))
    print(' '.join(map(str, merge_sort(A))))

if __name__ == "__main__":
    main()
