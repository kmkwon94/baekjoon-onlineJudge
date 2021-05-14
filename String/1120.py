'''
# 1120 - 문자열

문자열 A, B 가 주어질때 A <= B 이다.
A 문자열의 문자와 B 문자열의 문자가 다를때 차이가 1씩 증가하는데
차이가 최소가 되게끔 할때 그 차이의 값을 구해라
A B가 같아지려면
1. A의 앞에 아무 알파벳 추가
2. A의 뒤에 아무 알파벳 추가
'''

import sys

a,b = map(str, sys.stdin.readline().split())
cnt = 0

min_ = len(a)
for i in range(len(b) - len(a)+1):
    count = 0
    for j in range(len(a)):
        if a[j] != b[i+j]:
            cnt += 1
    if cnt < min_:
        min_ = count

print(min_)
