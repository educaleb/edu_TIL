import sys
from itertools import *

input = sys.stdin.readline
T = int(input())

arr = [int(input()) for _ in range(T)]
seq = [1, 1, 1, 2, 2]

for i in range(5, max(arr)):
    seq.append(seq[i-1]+seq[i-5])

for i in arr:
    print(seq[i-1])