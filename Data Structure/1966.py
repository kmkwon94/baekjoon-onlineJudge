'''
# 프린터 큐

입력 : 테케 
       N(문서의 갯수),  M(알고 싶은 문서의 인덱스)
       문서의 중요도 (1 ~9 사이 차례로 주어짐, 숫자가 높을수록 중요도도 높다)

중요도가 같은 것이 여러개 일수도 있다. 

자 우선순위를 비교를 해
제일 max를 찾아 max 값을 가지고 list[0] 와 비교해
 - max 보다 작은 값은 뒤로 보내
 - max 보다 크거나 같은 값은 pop을 해서 answer에 담아
 - list가 빌때까지 이걸 반복해야지

그럼 인덱스 추적은 어케할거야?
알고자 하는 인덱스 M을 받아서 target_idx 변수를 만들고
target_idx가 0 이고 pr[max_pr_idx] == pr[target_idx] 일때 추적하는 인덱스가
answer에 추가되는 시점이기에 while문을 나와

그리고 answer에 추가하지 않았기 때문에 len(answer) 길이보다 1개 많은 것이
추적한 값이 몇번째로 프린트 된 것인지에 대한 답

ex)

4 2
1 2 3 4

A B C D (1 2 3 4)
B C D A (2 3 4 1)
C D A B (3 4 1 2)
D A B C (4 1 2 3) -> D 출력
A B C (1 2 3)
B C A (2 3 1)
C A B (3 1 2) -> C 출력
A B (1 2)
B A (2 1) -> B 출력
A (1) -> A 출력
'''
import sys
from collections import deque
TC = int(sys.stdin.readline())
#dic = collections.defaultDict(int)
for _ in range(TC):
    answer = []
    N, M = map(int, sys.stdin.readline().split())
    pr = deque(list(map(int, sys.stdin.readline().split())))
    target_idx = M
    if N == 1:
        print(1)
    else:
        #for i in range(len(pr)):
        while pr:
            if target_idx < 0:
                target_idx = len(pr) - 1
            max_pr_idx = pr.index(max(pr))
            if pr[max_pr_idx] == pr[target_idx] and target_idx == 0:
                break
            if pr[0] < pr[max_pr_idx]:
                pr.append(pr.popleft())
                target_idx -= 1
                #print(pr, answer, target_idx)
            else:
                answer.append(pr.popleft())
                target_idx -= 1
                #print(pr, answer, target_idx)

        print(len(answer) + 1)
