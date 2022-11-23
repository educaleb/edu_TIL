from itertools import combinations as com           #swea chef와 같다 testcase가 존재하지 않을뿐
import sys

N = int(input())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

def status(board, case):
    team = 0
    for i, j in com(case, 2):
        team += board[i][j] + board[j][i]
    return team

num = 1e9
for i in com(range(N), N//2):
    another = list(set(range(N)) - set(i))
    result1 = status(board, i)
    result2 = status(board, another)
    if num > abs(result1-result2):
        num = abs(result1-result2)

print(num)