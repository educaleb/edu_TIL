import sys
input = sys.stdin.readline

K = int(input())
jangbu = []

for i in range(K):
    call = int(input())

    if call == 0:
        jangbu.pop()
    else:
        jangbu.append(call)
print(sum(jangbu))