import sys
from itertools import combinations 

# sys.stdin = open()

def Taste(synerge, case):
    food = 0
    for i, j in combinations(case, 2):
        food += synerge[i][j] + synerge[j][i]
    return food

T = int(input())
for Test_Case in range(1, T+1):
    N = int(input())

    synerge = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

    min = 20000

    for case in combinations(range(N), N//2):
        another = list(set(range(N)) - set(case))
        res1 = Taste(synerge, case)
        res2 = Taste(synerge, another)
        if (min > abs(res1 - res2)):
            min = abs(res1 - res2)

    print('#{} {}'.format(Test_Case, min))
