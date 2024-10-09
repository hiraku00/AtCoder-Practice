def can_make_sum(S, A):
    dp = [0] * (S+1)
    dp[0] = 1
    for i in A:
        for j in range(S-i, -1, -1):
            if dp[j] == 1:
                dp[j+i] = 1
    return 'Yes' if dp[-1] == 1 else 'No'

def main():
    N, S = map(int, input().split())
    A = tuple(map(int, input().split()))
    print(can_make_sum(S, A))

if __name__ == "__main__":
    main()
