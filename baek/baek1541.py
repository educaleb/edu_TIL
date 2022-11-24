import sys
input = sys.stdin.readline

quest = input().split('-')
num = 0
for i in quest[0].split('+'):
    num += int(i)
for i in quest[1:]:
    for j in i.split('+'):
        num -= int(j)
print(num)