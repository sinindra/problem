def dfs(F, i):
    global S, ans, n, N
    
    if len(F) == n:
        s1, s2 = 0, 0
        B = list(set(range(N)) - set(F))
        for i in range(n - 1):
            for j in range(i + 1, n):
                s1 += S[F[i]][F[j]] + S[F[j]][F[i]]
                s2 += S[B[i]][B[j]] + S[B[j]][B[i]]
        tmp = abs(s1 - s2)
        if tmp < ans:
            ans = tmp
        return
    
    if i == N:
        return

    if len(F) < n:
        dfs(F + [i], i + 1)
        dfs(F, i + 1)

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    n = int(N/2)
    S = [ list(map(int, input().split())) for _ in range(N) ]
    ans = float("inf")
    dfs([], 0)
    print("#{} {}".format(test_case, ans))
    
"""
풀이설명:
완전탐색.
DFS를 통해 재료로 들어가 순서를 하나씩 추가.
필요한 재료만큼 추가되면 리턴.
필요한 만큼 재료가 채워지면 각각 시너지를 합한다.
"""
