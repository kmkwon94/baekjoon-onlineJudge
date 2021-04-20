'''
#2606 - 바이러스

1번 컴퓨터가 바이러스에 걸렸을때 바이러스에 걸리게 되는 컴퓨터의 갯수(1번 제외)
'''

import sys


def dfs(v):
    #현재 정점은 방문했으니 추가
    visited[v] = 1
    answer.append(v)

    for i in range(1, computer_cnt + 1):
        if visited[i] == 0 and matrix[v][i] == 1:
            dfs(i)


computer_cnt = int(input())
edge = int(input())
matrix = [[0] * (computer_cnt + 1) for _ in range(computer_cnt + 1)]
visited = [0] * (computer_cnt + 1)
answer = []
for _ in range(edge):
    a, b = map(int, sys.stdin.readline().split())
    matrix[a][b] = matrix[b][a] = 1

dfs(1)
del answer[0]
print(len(answer))
