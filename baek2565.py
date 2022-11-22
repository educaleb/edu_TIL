import sys
input = sys.stdin.readline

n = int(input())

line = [*map(int, input().split())for i in range(n)] 
print(line)