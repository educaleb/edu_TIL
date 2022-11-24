import sys
input = sys.stdin.readline

N = int(input())
roads = list(map(int, input().split()))
costs = list(map(int, input().split()))

ans = 0
min_price = costs[0]

for i in range(N-1):
    if costs[i] < min_price:
        min_price = costs[i]

    ans += min_price * roads[i]

print(ans)