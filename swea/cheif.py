import sys                                                                  #인터프리터가 변수와 함수를 직접 제어할수있게 
from itertools import combinations                                          #combination 함수 반복자를 생성 반환 순열, 조합에 좋아용

sys.stdin = open('sample_input.txt', 'r')                                   # input은 한줄읽고 개행문자를 벗겨낸후 문자열변환 return

def taste(synerge , case):                                                 #조합을 구하기 위한 함수 설정
    food = 0                                                                 #시너지갑을 저장
    for i, j in combinations(case,2):                                        #2길이에 case를 반복요소 없이 조합
        food += synerge[i][j] + synerge[j][i]                                     #주어진 시너지 1,2 + 다시 2,1 
    return food


T = int(input())                                                             #테스트케이스
for Test_Case in range(1, T+1):
    N = int(input())

    synerge = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]      # 시너지 판

    min = 20000                                                                     #적당히 큰 수 
    for k in combinations(range(N), N//2):                                   #한음식에 들어갈 갯수
        another = list(set(range(N)) - set(k))                               #중복제거 인덱스 값 분리 
        res1 = taste(synerge, k)                                            # 시너지 저장
        res2 = taste(synerge, another)                                         #분리된 인덱스 값 저장
        if (min > abs(res1-res2)):
            min = abs(res1-res2)

    print('#{} {}'.format(Test_Case, min))