import sys    
from collections import deque
input = sys.stdin.readline
T = int(input())   

for test_case in range(1, T+1):
    N, M = map(int, input().split())  
    infor = deque(list(map(int, input().split())))    
    idx = list(range(len(infor)))
    idx[M] = 'target'

    cnt = 0

    while True:
        if infor[0] == max(infor):
            cnt +=1

            if idx[0] == 'target':
                print(cnt)
                break
            else:
                infor.popleft()
                idx.pop(0)

        else:
            infor.append(infor.popleft())
            idx.append(idx.pop(0))