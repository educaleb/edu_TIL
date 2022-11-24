import sys
input = sys.stdin.readline

T = int(input())
for test_case in range(T):
    VPS = input()
    char = list(VPS)
    sum = 0
    for i in char:
        if i == '(':
            sum += 1
        elif i == ')':
            sum -= 1
        if sum < 0:     #sum 값이 -1이 되는 순간 조건이 부합하지 않기에 종료
            print('NO')
            break
    if sum > 0:
        print('NO')
    elif sum == 0:
        print('YES')