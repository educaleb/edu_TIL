import sys
input = sys.stdin.readline

board = [list(map(int, input().split()))for _ in range(9)]
check = [(i, j) for i in range(9) for j in range(9) if board[i][j] == 0]

def is_promising(i, j):
    promising = [1,2,3,4,5,6,7,8,9]

    for k in range(9):                      #행과 열 검사
        if board[i][k] in promising:
            promising.remove(board[i][k])
        if board[k][j] in promising:
            promising.remove(board[k][j])

    i //= 3
    j //= 3
    for p in range(i*3, (i+1)*3):          #3*3검사
        for q in range(j*3, (j+1)*3):
            if board[p][q] in promising:
                promising.remove(board[p][q])
    
    return promising

game = False                            # 정답 출력 됐나요? 
def dfs(x):
    global game

    if game:
        return

    if x == len(check):
        for row in board:
            print(*row)
        game = True
        return

    else:
        (i, j) = check[x]
        promising = is_promising(i, j)

        for num in promising:
            board[i][j] = num
            dfs(x+1)
            board[i][j] = 0

dfs(0)