import sys
input = sys.stdin.readline
N = int(input())
time = [[0]*2 for _ in range(N)]                # 시작시간과 끝나는시간을 인덱싱하기 위해

for i in range(N):
    s, e = map(int, input().split())
    time[i][0] = s                              # 0은 시작 시간
    time[i][1] = e                              # 1은 끝나는 시간

time.sort(key = lambda x:(x[1], x[0]))          # 끝나는 시간을 먼저 정렬한다 이유는 끝나는 지점으로 부터 시작해야하니까

cnt = 1                                         # 첫 회의 시작은 1
end_time = time[0][1]                           # end_time에 첫 회의 끝나는 시간 저장하고
for i in range(1, N):                           
    if time[i][0] >= end_time:                  # 시작시간이 끝나는 시간보다 크거나 같으면
        cnt += 1                                # 회의 하나 더 시작
        end_time = time[i][1]                   # 끝나는 시간 다시 저장

print(cnt)