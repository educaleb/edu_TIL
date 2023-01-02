import sys
input = sys.stdin.readline

K, N =map(int, input().split())
KL = [int(input()) for _ in range(K)]
start, end = 1, max(KL)

while start <= end :
    mid = (start + end)//2
    line = 0

    for i in range(K):
        line += KL[i] // mid
    
    if line >= N:
        start = mid + 1
    else:
        end = mid - 1
print(end)