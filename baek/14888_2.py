import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
add, sub, mul, div = map(int, input().split())

min_value = 1e9
max_value = -1e9

def per(i, arr):
    global add, sub, mul, div, min_value, max_value

    if i == N:
        min_value = min(min_value, arr)
        max_value = max(max_value, arr)
    else:
        if add>0:
            add -= 1
            per(i+1, arr + A[i])
            add += 1
        if sub>0:
            sub -= 1
            per(i+1, arr - A[i])
            sub += 1
        if mul>0:
            mul -= 1
            per(i+1, arr * A[i])
            mul += 1
        if div>0:
            div -= 1
            per(i+1, int(arr / A[i]))
            div +=1

per(1, A[0])

print(max_value)
print(min_value)