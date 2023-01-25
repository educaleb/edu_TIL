import sys
from itertools import combinations
input = sys.stdin.readline

arr = [int(input()) for _ in range(9)]
result = []

def dfs(depth, start):
    if depth == 7:
        if sum(result) == 100:
            for j in sorted(result):
                print(j)
            exit()
        else:
            return
    
    for i in range(start, len(arr)):
        result.append(arr[i])
        dfs(depth + 1, i+1)
        result.pop()

dfs(0,0)