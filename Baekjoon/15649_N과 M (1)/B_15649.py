def combination(idx, m):
    global comb
    if idx == m:
        ans.append(comb[:])
    else:
        for j in range(N):
            if str(arr[j]) not in comb:
                comb.append(str(arr[j]))
                combination(idx + 1, m)
                comb.pop()


N, M = map(int, input().split())
arr = [i for i in range(1, N + 1)]
comb = []
ans = []
combination(0, M)
for k in ans:
    print(' '.join(k))
