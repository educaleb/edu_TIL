import sys

input = sys.stdin.readline
N, K = map(int, input().split())

def pibo(N, K):
    if K > N :
        return 0 

    cache = [[-1 for _ in range(N+1)] for _ in range(N+1)]