# 가장 많은 카드에 적힌 숫자와 카드가 몇장인지 출력 장수가 같다면 적흰 수가 큰것을 출력

T = int(input())

for i in range(1, T+1):
    N = int(input())
    num = list(map(int, input()))
    maxnum = num[0]

    for j in num:                                             #가장 큰 값 찾기
        if (j > maxnum):
            maxnum = j

    cnt_list = [0] * (maxnum +1)                              # 카운팅할 리스트 길이 설정
        
    for k in range(0, N):                                     # i의 값만큼 count_list의 인덱스로 가서 1씩 더해주기
        cnt_list[num[k]] += 1                                 # 출력을 위한 초기값 설정
        max_count = 0
        temp_card = 0                                         # 정렬된 count_list를 돌면서

        for l in range(0, len(cnt_list)):                     # count_list의 값의 최대를 찾아                                                        
            if cnt_list[l] >= max_count:                      # 여기서 **크거나 같다**를 설정해 준 이유는 카드의 장수가 같더라도 더 값이 큰 카드를 출력하기 위해서!
                max_count = cnt_list[l]                       # 최대값을 저장하고
                temp_card = l                                 # 그 최대값을 가지는 인덱스값이 즉 카드숫자

    print('#{} {} {}'.format(i, temp_card, max_count))