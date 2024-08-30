N, S = map(int, input().split())
cnt = 0
for i in range(1, N+1):
    print(f'N : {N}, max(0,{S}-{i}) : {max(0,S-i)}')
    cnt += min(N, max(0,S-i))
print(cnt)
