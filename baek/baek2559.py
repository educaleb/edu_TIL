import sys
input = sys.stdin.readline

N, K = map(int, input().split())    
degree = list(map(int, input().split()))
avg = []
avg.append(sum(degree[:K]))

for i in range(N - K):
    avg.append(avg[i] - degree[i] + degree[K+i])
   
print(max(avg))