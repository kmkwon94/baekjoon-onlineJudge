'''
#2667번 - 단지번호붙이기
정사각형 지도를 주어졌을때 (5 <= N <= 25 ) 1은 집이 있는곳 0은 집이 없음
집이 연결되었다는것은 좌우 혹은 상하에 집이 인접해있다는 것
대각선은 아님
단지수를 출력하고 각 단지에 속하는 집의 갯수를 오름차순으로 출력''
'''

import sys


def dfs(x, y):
    #만약 범위를 벗어나면 False
    if x <= -1 or x >= n or y <= -1 or y >= n:
        return False

    # 집이면 이제 상하좌우 탐색을 시작해야지
    if matrix[x][y] == 1:
        #자 방문한 곳이면 0으로 표시해서 바꿔놔야함
        matrix[x][y] = 0
        global home
        home += 1
        dfs(x, y + 1)  #상
        dfs(x, y - 1)  #하
        dfs(x - 1, y)  #좌
        dfs(x + 1, y)  #우
        return True
    return False


n = int(sys.stdin.readline().rstrip())
matrix = []

for _ in range(n):
    matrix.append(list(map(int, sys.stdin.readline().rstrip())))

result = 0
home = 0
ans = []
for i in range(n):
    for j in range(n):
        if dfs(i, j) == True:
            result += 1
            ans.append(home)
            home = 0
ans.sort()
print(result)
for i in ans:
    print(i)
