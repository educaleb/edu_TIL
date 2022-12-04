import sys
input = sys.stdin.readline
N = int(input())
paper = [list(map(int, input().split())) for _ in range(N)]

minus, zero, plus = 0,0,0
def check (x, y, N):
    global minus, zero, plus

    number = paper[x][y]
    for i in range(x, x+N):
        for j in range(y, y+N):
            if number != paper[i][j]:
                for k in range(3):
                    for l in range(3):
                        check(x+k * N//3, y+l * N//3, N//3)
                return
    
    if number == -1:
        minus += 1
    elif number == 0:
        zero += 1
    else:
        plus += 1

check(0, 0, N)
print(f'{minus}\n{zero}\n{plus}')