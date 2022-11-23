import sys
input = sys.stdin.readline

N, M = map(int, input().split())
A = list(map(int, input().split()))

A_pix = [0 for i in range(M)]
A_sum = 0

A_pix[0] = 1

for i in range(N):
    A_sum += A[i]
    A_pix[A_sum%M] += 1

ans = 0
for i in A_pix:
    ans += i*(i-1)//2

print(ans)