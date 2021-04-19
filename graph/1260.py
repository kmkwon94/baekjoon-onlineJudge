'''
# DFS와 BFS
DFS 기본

def dfs(graph, v, visited):
  #현재 노드를 방문처리
  visited[v] = True
  print(v, end=' ')
  #현재 노드와 연결된 다른 노드를 재귀적으로 방문
  for i in graph[v]:
    if not visited[i]:
      dfs(graph, i, visited)

def bfs(graph, start, visited):
  #큐 구현을 위해 deque 가져오기
  queue = deque([start])
  # 현재 노드를 방문 처리
  visited[start] = True
  #큐가 빌때까지 반복
  while queue:
    #큐에서 하나의 원소를 뽑아 출력
    v = queue.popleft()
    print(v, end=' ')
    #해당 원소와 연결된, 아직 방문하지 않은 원소들을 큐에 삽입
    for i in graph[v]:
      if not visited[i]:
        queue.append(i)
        visited[i] = True

#각 노드가 연결된 정보를 리스트 자료형으로 표현 (2차원 리스트)
graph = [
  [],       #0번 정점
  [2,3,8],  #1번 정점
  [1,7],    #2번 정점
  [1,4,5],  #3번 정점
  [3,5],    #4번 정점
  [3,4],    #5번 정점
  [7],      #6번 정점
  [2,6,8],  #7번 정점
  [1,7]     #8번 정점
]

#각 노드가 방문딘 정보를 리스트 자료형으로 표현 (1차원 리스트)
visited = [False] * 9

#정의된 DFS 함수 호출
dfs(graph, 1, visited)
'''

import sys
from collections import deque
# N : 정점의 갯수
# M : 간선의 갯수
# V : 시작하는 정점의 번호


def bfs(start):
    #큐 구현
    dq = deque([start])
    #현재 노드 방문처리
    visited[start] = 0
    #큐가 빌때까지 반복
    while dq:
        v = dq.popleft()
        print(v, end=' ')
        #해당 원소와 연결된, 아직 방문하지 않은 원소들을 큐에 삽입
        for i in range(1, N + 1):
            if visited[i] == 1 and matrix[v][i] == 1:
                dq.append(i)
                visited[i] = 0


def dfs(v):
    #현재 노드를 방문처리
    visited[v] = 1
    print(v, end=' ')
    #현재 노드와 연결된 다른 노드를 재귀적으로 방문
    for i in range(1, N + 1):
        if visited[i] == 0 and matrix[v][i] == 1:
            dfs(i)


N, M, V = map(int, sys.stdin.readline().split())
matrix = [[0] * (N + 1) for _ in range(N + 1)]
for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    matrix[a][b] = matrix[b][a] = 1
visited = [0] * (N + 1)

dfs(V)
print()
bfs(V)
