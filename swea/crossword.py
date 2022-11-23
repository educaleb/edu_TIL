T = int(input())

for Test_Case in range(1, T+1):
    N, M = map(int, input().split())
    palindrome = []
    
    board = []
    for i in range(N):
        board.append(input())

    for r in range(N):                                                  #r은 row c는 column (가로 검색)
        for c in range(N - M + 1): 
            if board[r][c : c + M] == board[r][c : c + M][ : : -1]:     #회문이 맞는지 확인
                palindrome.append(board[r][c : c + M])                  #회문에 추가

    for r in range(N - M + 1):                                          #세로 검색
        for c in range(N):
            c_list = []                                                 #세로 검색을 위한 배열 선언
            for i in range(M):                                          
                c_list.append(board[r+i][c])                            #세로열 문자를 저장
            if (c_list == c_list[ : : -1]):                             #회문 검색
                palindrome.append(''.join(c_list))                      #회문 저장
    print('#{} {}'.format(Test_Case, palindrome[0]))
