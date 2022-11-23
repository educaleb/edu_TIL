import sys
input = sys.stdin.readline

n = int(input())
line = [list(map(int, input().split())) for _ in range(n)]
line.sort(key = lambda x:x[0])
dp = [0]*n

for i in range(n):
    result = 0
    for j in range(i):
        if line[i][1] > line[j][1] and result < dp[j]:
            result = dp[j]
    dp[i] = result + 1

print(n - max(dp))