import sys
import heapq
input = sys.stdin.readline

N = int(input())
heap = []

for i in range(N):
    X = int(input())
    if X == 0:
        if len(heap) == 0:
            print('0')
        else:
            print(heapq.heappop(heap))
    else:
        heapq.heappush(heap, X)