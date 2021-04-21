'''
#음료수 얼려 먹기
N, M 이 주어짐 N*M 크기의 얼음틀 0은 구멍이 뚫려있고 1은 막혀있는 벽

아이스크림 총 몇개 생성되는가?

'''

import sys

n, m = map(int, sys.stdin.readline().split())
matrix = []
for i in range(n):
    matrix.append(list(map(int, sys.stdin.readline().rstrip())))


def dfs(x, y) -> bool:
    #만약 범위를 벗어난다면 false 종료조건
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False

    if matrix[x][y] == 0:
        matrix[x][y] = 1

        dfs(x, y + 1)  #상
        dfs(x, y - 1)  #하
        dfs(x - 1, y)  #좌
        dfs(x + 1, y)  #우
        return True
    return False


result = 0

for i in range(n):
    for j in range(m):
        if dfs(i, j) == True:
            result += 1
print(result)
