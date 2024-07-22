def bf2(S, A):
    dp = [1] + [0] * S
    for i in A:
        print(f'----------------------------------------------------- i : {i}')
        print(range(S - i, -1, -1))
        for j in range(S - i, -1, -1):
            print(f'------------------------------------------ j : {j}')
            print(f'dp[{j}] : {dp[j]}')
            if dp[j] == 1:
                dp[j + i] = 1
                print(f'dp[{j}] == 1 => {dp[j] == 1}')
                print(f'dp[{j} + {i}] = 1')
            print(dp)
    print(f'========')
    print(dp)
    print("Yes" if dp[-1] == 1 else "No")

# def bf2(S, A):
#     dp = [1] + [0] * S
#     for i in A:
#         for j in range(S-i, -1, -1):
#             if dp[j] == 1:
#                 dp[j+i] = 1
#     print(dp)
#     print("Yes" if dp[-1] == 1 else "No")

N, S = map(int, input().split())
A = list(map(int, input().split()))
bf2(S, A)
