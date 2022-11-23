T = int(input())

for Test_Case in range(1, T+1):
    N, K = map(int, input().split())
    num = [list[map(int, input())] for _ in range(N)]
    turn = N//4                 #4번돌아야 하니 한변에 저장할 수
    rock_num = []               #회전된 값이 저장될 리스트

    for i in range(turn):
        pop = num.pop()
        num.inser(0,pop)