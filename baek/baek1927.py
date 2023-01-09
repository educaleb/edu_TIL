import sys
import heapq
input = sys.stdin.readline

heap = []
N = int(input())

for _ in range(N):
    X = int(input())
    if X == 0:
        if len(heap) == 0:
            print('0')
        else:
            print(heapq.heappop(heap))
    else:
        heapq.heappush(heap, X)