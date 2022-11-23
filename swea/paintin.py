import sys

T = int(input())


for test_case in range(1, T+1):
    board = [[]*10 for _ in range(10)]
    sum = 0
    paint = int(input())
    
    for i in paint:
        r1, c1, r2, c2, color = map(int, input().split())
       
        for j in range(r1, r2+1):
            for k in range(c1, c2+1):
                board[j][k] += color
    
    for i in range(10):
        for j in range(10):
            if (board[i][j] == 3):
                sum += 1
                
    print()
