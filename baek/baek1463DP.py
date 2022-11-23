import sys
input = sys.stdin.readline

X = int(input())

dp={1:0}                            #1일 때 0번의 연산횟수
def rec(n):
    if n in dp.keys():              #dp값이 key가 될때 종료
        return dp[n]
    if (n%3 == 0) and (n%2 == 0):
        dp[n] = min(rec(n//3)+1, rec(n//2)+1)
    elif n%3==0:
        dp[n] = min(rec(n//3)+1, rec(n-1)+1)
    elif n%2==0:
        dp[n] = min(rec(n//2)+1, rec(n-1)+1)
    else:
        dp[n] = rec(n-1)+1
    return dp[n]
print(rec(X))