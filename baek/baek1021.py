import sys                                     
from collections import deque
N, M = map(int, input().split())
queue = deque([i for i in range(1, N+1)])
target = deque(list(map(int, input().split())))
cnt = 0 

for i in target:            #target에 인덱스를 위해
    while True:
        if queue[0] == i:
            queue.popleft()
            break
        else:
            if queue.index(i) < len(queue)/2:
                while queue[0] != i:
                   queue.append(queue.popleft())
                   cnt += 1
            else: 
                while queue[0] != i:
                    queue.appendleft(queue.pop())
                    cnt += 1
print(cnt)