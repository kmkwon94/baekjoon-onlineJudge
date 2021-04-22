'''
#7576 토마토

M * N 상자안에 토마토가 있는데 
0이 안익은거 
1이 익은거 
-1은 토마토가 없다

익은 토마토는 상하좌우 안익은 토마토에 영향을 끼쳐 익게끔 만든다.
최소 며칠만에 모든 토마토가 익게 되는가?


#구글링 풀이

import sys
from collections import deque
m,n = map(int, sys.stdin.readline().split())
matrix = []

for i in range(n):
  matrix.append(list(map(int, input().split(' '))))

#이동할 방향 정의 (상하좌우)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
dq = deque()
def bfs():
  while dq:
    x,y = dq.popleft()

    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]

      if 0 <= nx < n and 0 <= ny < m and matrix[nx][ny] == 0:
        matrix[nx][ny] = matrix[x][y] + 1
        dq.append((nx,ny))

for i in range(n):
  for j in range(m):
    if matrix[i][j] == 1:
      dq.append((i,j))

bfs()
isTrue = False
result = -2
for i in matrix:
    for j in i:
        if j == 0:
            isTrue = True
        result = max(result, j)
if isTrue == True:
    print(-1)
elif result == -1:
    print(0)
else:
    print(result - 1)
'''
#내 풀이
import sys
from collections import deque


def bfs():
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    #dq가 빌때까지
    while dq:
        #익은 토마토위치를 꺼냄
        x, y = dq.popleft()

        #익은 토마토의 상하좌우 좌표를 얻어냄
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            #새로 얻은 좌표는 아직 익지 않은 토마토여야하고 농장 범위 안에 있어야함
            if (0 <= nx < n) and (0 <= ny < m) and farm[nx][ny] == 0:
                farm[nx][ny] = farm[x][y] + 1
                dq.append((nx, ny))


m, n = map(int, sys.stdin.readline().split())
farm, dq = [], deque()

#농장의 토마토 입력받기
for _ in range(n):
    farm.append(list(map(int, sys.stdin.readline().split(' '))))


for i in range(n):
    for j in range(m):
        #익은 토마토를 찾았다면 dq에 위치 삽입
        if farm[i][j] == 1:
            dq.append((i, j))

bfs()
max_num = 0
is_answer = False

for i in farm:
    if 0 in i:
        print(-1)
        is_answer = False
        break
    else:
        max_num = max(max_num, max(i))
        is_answer = True

if is_answer:
    print(max_num - 1)
