import sys

input = sys.stdin.readline
N = int(input())
num = list(map(int, input().split()))


for i in range(1, N):
    # print(num[i])
    num[i] = max(num[i], num[i] + num[i-1])
    print(num[i])

print(max(num))