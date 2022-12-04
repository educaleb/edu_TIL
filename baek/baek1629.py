import sys

input = sys.stdin.readline
A, B, C = map(int, input().split())

def cal (A, num):
    if num == 1:
        return A%C
    else:
        tmp = cal(A, num//2)
        if num%2 == 0:
            return (tmp * tmp) % C
        else:
            return (tmp * tmp * A) % C

print(cal(A, B))