'''
# 11725 트리의 부모 찾기

루트가 없는 트리가 주어지는데 이 때 루트의 노드를 1번 정점이라고 가정할때,
각 노드의 부모를 구하시오

DFS BFS 둘 다 될듯
인접행렬 방식은 N의 범위가 10만까지 이므로 매우크다 
그러므로 메모리 초과가 되기때문에 
인접 리스트 방식으로 풀어야한다. 
'''

import sys
import collections

v_num = int(sys.stdin.readline().strip())
graph = [[] for _ in range(v_num + 1)]
visited = [0 for _ in range(v_num + 1)]
my_parent = collections.defaultdict()
for _ in range(v_num - 1):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(1, len(graph)):
    graph[i].sort()


def dfs(v):
    #dfs가 시작됏으니까 간선 visited
    visited[v] = 1

    #현재 정점에서 가야할 정점이 있는지 탐색
    for i in graph[v]:
        # 연결되어 있는 정점을 찾았다면, 그 정점을 탐색
        if visited[i] == 0:
            my_parent[i] = v
            dfs(i)


dfs(1)
for i in range(2, len(graph)):
    print(my_parent[i])
