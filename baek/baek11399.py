import sys 
input = sys.stdin.readline

N = int(input())
P = list(map(int, input().split()))

P.sort()
time = 0

for i in range(1, N+1):
    time += sum(P[0:i])
print(time)