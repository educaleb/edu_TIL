T = int(input())                                                # 노선 수

for i in range(1, T+1):
    K, N, M = map(int, input().split())                         # 최대 이동량, 총 이동량, 설치된 충전소
    charger = list(map(int, input().split()))
    cnt = 0                                                     # 충전횟수 카운트
    current = 0                                                 # 현재 위치

    while((current + K) < N):
        charge = False
        for j in range(K, 0, -1):
            if current + j in charger:
                current = current + j
                cnt += 1
                charge = True
                break

        if charge == False:                                     # 충전을 못한 경우
            cnt = 0
            break

    print("#%d %d" %(i, cnt))