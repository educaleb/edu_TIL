#쿼드트리 색종이와 같다 분할후 같은수로묶어 하나로 출력
import sys 
input = sys.stdin.readline
N = int(input())
tree = [list(map(int, input().strip())) for _ in range(N)]

def quard (x, y , N):
    number = tree[x][y]
    for i in range(x, x+N):
        for j in range(y, y+N):
            if number != tree[i][j]:
                print('(',end='')
                quard(x,y,N//2)
                quard(x, y+N//2, N//2)
                quard(x+N//2, y, N//2)
                quard(x+N//2, y+N//2, N//2)
                print(')',end='')
                return

    if number==0:
        print('0',end='')
        return
    else:
        print('1',end='')
        return

quard(0,0,N)