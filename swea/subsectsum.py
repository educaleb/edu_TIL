T = int(input())

for Test_Case in range(1, T+1):
    N, K = map(int, input().split())
    A = list(range(1, 13))                      # 원소가 1~12 까지인 집합 A
    cnt = 0
                                                # 부분집합
    for i in range(1 << 12):                    # [0]*12 ~ [1]*12 까지
        subset = []                             
        sum = 0
        for j in range(12):                     # 원소가 12개 이므로, 각 인덱스 마다 해당 원소가 이번 부분집합에 들어갈지를 확인
            if i & (1 << j):                    # 1이 j번 쉬프트 되며 i값과 비교
                subset.append(A[j])             
                sum += A[j]

        if (len(subset) == N and sum == K):     # 두개의 조건과 일치하면 cnt +1
            cnt += 1
    print('#{} {}'.format(Test_Case, cnt))