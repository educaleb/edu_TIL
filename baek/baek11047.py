import sys
input = sys.stdin.readline

N, K = map(int, input().split()) 
A = []
for i in range(N):
    A.append(int(input()))

count = 0
for i in reversed(range(N)):
    count += K//A[i]
    K = K%A[i] 

print(count)