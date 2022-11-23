import sys
input = sys.stdin.readline

N, K = map(int, input().split())
NV = [list(map(int, input().split())) for _ in range(N)]
# NV.sort(key = lambda x:x[0])
dp = [[0]*(K+1) for _ in range(N+1)]

for i in range(1, N+1):
    for j in range(1, K+1):
        w = NV[i-1][0]
        v = NV[i-1][1]

        if j<w:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-w]+v)
print(dp[N][K])


# for i in range(n):
#     result = 0
#     for j in range(i):
#         if line[i][1] > line[j][1] and result < dp[j]:
#             result = dp[j]
#     dp[i] = result + 1

# print(n - max(dp))