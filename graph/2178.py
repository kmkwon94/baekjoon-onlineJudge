'''
#미로찾기 - bfs

시작위치 1,1 에서 N,M 까지의 움직여야하는 최소 칸을 구해라.
'''

import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
matrix = []
for i in range(n):
    matrix.append(list(map(int, sys.stdin.readline().rstrip())))

#이동할 방향 정의 (상하좌우)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(x, y):
    #큐 정의
    dq = deque()
    dq.append((x, y))
    #큐가 빌때까지 반복
    while dq:
        x, y = dq.popleft()
        #현재 위치에서 네 방향으로의 위치확인
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            #미로찾기에서 범위를 벗어낫을때
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            #벽을 만났을때
            if matrix[nx][ny] == 0:
                continue
            #해당 노드를 처음 방문하는 겨우에만 최단 거리 기록
            if matrix[nx][ny] == 1:
                matrix[nx][ny] = matrix[x][y] + 1
                dq.append((nx, ny))
    return matrix[n - 1][m - 1]


print(bfs(0, 0))
