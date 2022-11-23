import sys             
input = sys.stdin.readline

S = input().strip().lower()   
q = int(input())                
char = []

for i in range(q):
    a, l, r = input().split()   
    l = int(l)
    r = int(r)
    cnt = 0
    for j in S[l:r+1]:
        if j == a:
            cnt+=1
    print(cnt)