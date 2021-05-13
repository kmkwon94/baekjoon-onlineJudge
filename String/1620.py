'''
# 1620 - 나는야 포켓몬 마스터 이다솜

첫째줄에 포켓몬 도감에 등록된 몬스터의 수 N
내가 맞춰야 하는 문제의 갯수 M 이 주어짐

1 <= N,M <= 100,000
N개의 줄에 포켓몬 이름이 들어오고 
다음 M개의 줄에 영어로 이름이 들어오면 그 포켓몬의 숫자
숫자로 들어오면 그 포켓몬의 이름으로 return 해야함
'''

import sys
import collections

n,m = map(int, sys.stdin.readline().split())
poket_dict = collections.defaultdict()
poket_num_dict = collections.defaultdict()
answer = []
for i in range(1, n+1): 
    name = sys.stdin.readline().strip()
    poket_dict[i] = name
    poket_num_dict[name] = i


for i in range(m):
    question = sys.stdin.readline().strip()

    if question.isdigit():
        answer.append(poket_dict[int(question)])
        #print(poket_dict[int(question)])
    elif question.isalpha():
        answer.append(poket_num_dict[question])
        #print(poket_num_dict[question])

for i in answer:
    print(i)
