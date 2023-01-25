import sys
input = sys.stdin.readline

student = int(input())
num = list(map(int, input().split()))
change_student = []

for i in range(student):
    change_student.insert(i-num[i], i+1) 
# print(change_student)

for j in change_student:
    print(j,end=' ')