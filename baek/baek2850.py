import sys
input = sys.stdin.readline

N, M = map(int, input().split())
wood = list(map(int, input().split()))
start, end = 1, max(wood)

while start<= end:
    mid = (start + end) // 2

    gwood = 0
    for i in wood:
        if i >= mid:
            gwood += i - mid

    if gwood >= M:
        start = mid + 1
    else:
        end = mid -1
print(end)