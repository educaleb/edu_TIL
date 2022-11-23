T = int(input())

for Test_Case in range(1, T+1):
    N = int(input())
    a = list(map(int, input().split()))
    
    a_min = sorted(a)
    a_max = list(reversed(a_min))

    print("#"+str(Test_Case),end=' ')
    for i in list(zip(a_max[:5],a_min[:5])):
        print(i[0],i[1],end=' ')
    print()