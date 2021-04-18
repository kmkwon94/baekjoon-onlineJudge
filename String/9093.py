'''
# 단어 뒤집기

'''
import sys

TC = int(input())

for _ in range(TC):
    strings = sys.stdin.readline().split()
    answer = []
    for string in strings:
        string = string[::-1]
        answer.append(string)
    print(" ".join(answer))
