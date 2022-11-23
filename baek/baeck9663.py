import sys
input = sys.stdin.readline

def logic(n): 
    if n == N:                          #마지막 가지 탐색하는가
        global count

        count += 1

    else:
        for i in range(N):
            if visited[i]:
                continue

            board[n] = i                #(n, i)에 퀸 올리기

            if check(n):                #조건이 맞다면 퀸을 놓아라
                visited[i] = True
                logic(n+1)              #다음행으로 넘어가라
                visited[i] = False
                
def check(n):
    for i in range(n):      #이미 놓여진 퀸과 같은 열이거나 대각선 상에 있는지를 확인
        if (board[n] == board[i]) or (n - i == abs(board[n] - board[i])):
            return False    #(행끼리의차 == 열끼리 차의 절대값)이 True이면 대각선 상에 있으므로

    return True

N = int(input())
count = 0
board = [0 for _ in range(N)]           #인덱스 번호 == 행, 인덱스 값 == 열
visited = [False for _ in range(N)]

logic(0)
print(count)