from collections import deque
import sys
input = sys.stdine.readline

X = int(input())
Q = deque([X])
visited = [0]*(X+1)

while Q:
    c=Q.popleft()
    if c == 1:
        break
    if c%3 == 0 and visited[c//3] == 0:
        Q.append(c//3)
        visited[c//3] = visited[c]+1
    if c%2 == 0 and visited[c//2] == 0:
        Q.append(c//2)
        visited[c//2] = visited[c]+1
    if visited[c-1] == 0:
        Q.append(c-1)
        visited[c-1] = visited[c]+1
print(visited)