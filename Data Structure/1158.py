'''
1 ~ N 까지 원형으로 사람이 앉아있고
K 번째 사람을 빼는걸 반복해서 

제거한 사람의 순서대로 모여진 수열을 
요세푸스 순열이라고 한다. 
그 순열을 구하라 
current = 1
1,2,3,4,5,6,7 -> 3 제거 
1,2,4,5,6,7 -> 6 제거 
1,2,4,5,7 -> 2 제거
1,4,5,7 -> 7 제거
1,4,5 -> 5제거
1,4 -> 1제거
4 제거

del_idx = K
while문으로 돌자 while person_list: 이렇게
그래서 person_list[K-1] list에 추가한 뒤 del 하고
del_idx += K
del person_list[del_idx - 1]
만약에 del_idx가 person_list보다 길어질경우엔
del_idx % len(person_list) 으로 나머지 부분을 구하자 그게 초과한 부분에 대한
나머지지
'''
import sys

N, K = map(int, sys.stdin.readline().split())

person_list = [i + 1 for i in range(N)]

del_idx = K - 1
answer = []
while person_list:
    #print(answer, person_list, del_idx)
    if len(person_list) == 1:
        answer.append(person_list[0])
        break
    answer.append(person_list[del_idx])
    del person_list[del_idx]
    del_idx += K - 1
    if del_idx >= len(person_list):
        del_idx = del_idx % len(person_list)
sol = ''
sol += '<'
for idx, ans in enumerate(answer):
    if idx == len(answer) - 1:
        sol += str(ans)
    else:
        sol += str(ans) + ', '
sol += '>'
print(sol)
