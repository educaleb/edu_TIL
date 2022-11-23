T = int(input())

for Test_Case in range(1, T+1):
    P, Pa, Pb = map(int, input().split())
    cnt_a = cnt_b = 0
    strat_search = 1                # 서칭한 감을 저장할 변수 및 활용할 변수
    end_serach = P                  # 서칭을 어디서 종료할지 정하는 변수

    while(True):
        C = int((strat_search + end_serach)/2)
        cnt_a += 1
        if(C == Pa):
            break
        elif(C < Pa):
            strat_search = C        # 찾고자한 쪽 번호가 서칭보다 작다면 시작값과 치환
        elif(C > Pa):               # 찾고자한 쪽 번호가 서칭보다 크다면 끝값과 치환
            end_serach = C

    strat_search = 1                # 서칭한 감을 저장할 변수 및 활용할 변수
    end_serach = P                  # 서칭을 어디서 종료할지 정하는 변수
    while(True):
        C = int((strat_search + end_serach)/2)
        cnt_b += 1
        if(C == Pb):
            break
        elif(C < Pb):
            strat_search = C        # 찾고자한 쪽 번호가 서칭보다 작다면 시작값과 치환
        elif(C > Pb):               # 찾고자한 쪽 번호가 서칭보다 크다면 끝값과 치환
            end_serach = C

    result = ' '    
    if (cnt_a < cnt_b):
        result = 'A'
    elif (cnt_a > cnt_b):
        result = 'B'
    elif (cnt_a == cnt_b):
        result = '0'

    print("#{} {}".format(Test_Case, result))