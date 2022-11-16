# N = 구간 크기 , M = 구간의 합 
T = int(input())

for test_case in range(1, T+1):
    N, M = map(int, (input().split()))
    sect = list(map(int, (input().split())))  
    sect_sum = []
    
    for j in range(N-M+1):                                # N-M+1만큼 (즉, N구간의 M리스트 만큼 끝까지 탐색하기 위해 1번은 무조건 탐색함으로 +1)
        result = 0
        for k in range(j, j+M):                              # 연속적 수를 j 부터 j+M까지 더한다
            result += sect[k] 
        sect_sum.append(result)

    print("#%d %d"%(test_case, max(sect_sum)-min(sect_sum)))


