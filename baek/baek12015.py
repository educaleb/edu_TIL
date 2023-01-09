import sys
from bisect import bisect_left
input = sys.stdin.readline

A = int(input())
Ai = list(map(int, input().split()))
dp = []

for i in Ai:
    k = bisect_left(dp, i)
    if len(dp) <= k:
        dp.append(i)
    else:
        dp[k] = i
print(len(dp))