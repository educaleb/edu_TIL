T = int(input())               # 왜 오답처리가 나지???????????????????????????

for Test_Case in range(1, T+1):
    str1 = input()
    str2 = input()
    str_dict = {}

    for i in range(len(str1)):
        str_dict[str1[i]] = 0               #str1을 기준으로 같은 문자 검색을 위해 diction에 str1과 0 매칭

    for i in range(len(str1)):              
        cnt = 0
        for j in range(len(str2)):          # STR2가 1과 매칭되는지 부르타포스로 검색
            if(str1[i] == str2[j]):
                cnt += 1                    # 맞다면 카운터에 1 대입
                str_dict[str1[i]] = cnt     # 딕션에 같은 문자에 대한 카운트 1씩 늘려가기

    result_cnt = 0
    for i in range(len(str1)):              #딕션에서 최대값 뽑아내기 위한 for
        if (result_cnt < str_dict.get(str1[i])):
            result_cnt = str_dict.get(str1[i])
    
    print("#{} {}".format(Test_Case, result_cnt))