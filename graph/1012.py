'''
#유기농 배추 - DFS

유기농 배추를 키우는데 해충을 잡아먹는 지렁이가 최소 몇 마리 필요한지 구해라
지렁이는 배추의 상하좌우를 옮겨가기 때문에 몇 군데에 필요한지

DFS라고 생각한 이유는 상하좌우 돌아다니면서 연결되지 않는 순간 +1을 하면되니까

입력
- 테스트 케이스 T 가 주어지고 가로 M 세로 N 배추가 심어진 위치 K
예제입력
2
10 8 17
0 0
1 0
1 1
4 2
4 3
4 5
2 4
3 4
7 4
8 4
9 4
7 5
8 5
9 5
7 6
8 6
9 6
10 10 1
5 5
'''
import sys

TC = int(input())
sys.setrecursionlimit(10**7) 

def dfs(x, y):
    #범위를 벗어날 경우 return False
    if x < 0 or x >= m or y < 0 or y >= n:
        return False
    
    # 배추가 없다면 return False
    if matrix[x][y] == 0:
        return False
    #배추가 있고, 방문 하지 않았다면 
    if visited[x][y] == 0:
        visited[x][y] = 1 #해당 위치 방문처리 한 후 재귀
        dfs(x + 1, y)
        dfs(x - 1, y)
        dfs(x, y + 1)
        dfs(x, y - 1)
        return True #모든 재귀가 끝나면 return True
    return False
    
for _ in range(TC):
    m, n, k = map(int, sys.stdin.readline().split())
    answer = 0
    matrix = [[0] * (n) for _ in range(m)]
    visited = [[0] * (n) for _ in range(m)]

    for _ in range(k):
        a, b = map(int, sys.stdin.readline().split())
        matrix[a][b] = 1

    for i in range(m):
        for j in range(n):
            if dfs(i,j) == True:
                answer += 1
    print(answer)