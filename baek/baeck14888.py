from itertools import permutations as per
from collections import deque
import sys

input = sys.stdin.readline

N = int(input())                                    #N 갯수
A = list(map(int, input().split()))                 #A순열
operator = ['+', '-', '*', '//' ]                   #operator 지정 및 입력 받기
operator_input = list(map(int, input().split()))
operator_list = []

for i in range(4):
    if operator_input[i] == 0:
        pass
    else:
        for j in range(operator_input[i]):
            operator_list.append(operator[i])

num_case = list(per(operator_list, len(operator_list))) #연산자의 모든 조합
q = deque(num_case)                                     #조합 q에 저장

min_result = 1e9                                        #최대값 최소값 저장위한 큰 수 
max_result = -1e9

while q:
    now_list = q.popleft()
    result = A[0]

    for i in range(1, len(A)):
        if now_list[i-1] == '+':
            result += A[i]
        elif now_list[i-1] == '-':
            result -= A[i]
        elif now_list[i-1] == '*':
            result *= A[i]
        else:
            if result < 0:
                result = -(abs(result) // A[i])
            else:
                result = result // A[i]

    max_result = max(max_result, result)
    min_result = min(min_result, result)

print(max_result)
print(min_result)