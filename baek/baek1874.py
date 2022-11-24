import sys
input = sys.stdin.readline

n = int(input())
stack = []
answer = []
start = 1
flag= 0
for i in range(n):
    num = int(input())
    while start <= num:
        stack.append(start)
        answer.append('+')
        start += 1

    if stack[-1] == num:
        stack.pop()
        answer.append('-')
    else:
        print("NO")
        flag = 1
        break

if flag == 0:
    for i in answer:
        print(i)