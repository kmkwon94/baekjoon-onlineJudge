'''
# 2468 - 안전영역 

어떤지역에 높낮이가 주어지고 
장마철에 비가 내려서 특정 수위는 잠기게 된다.
안전영역이 최대일때의 갯수를 구하시오.

입력 N : 사각형의 크기
5
6 8 2 6 2
3 2 3 4 6
6 7 3 3 2
7 2 5 3 6
8 9 5 2 7

1일때 잠기고 0일때 안잠기는거로 
즉 0인 부위의 영역 구하기
'''

import sys

#sys.setrecursionlimit(10**7) 

def dfs(j,k,i):
    if j < 0 or j >= n or k < 0 or k >= n:
        return False
    
    if matrix[j][k] <= i:
        return False
    
    if visited[j][k] == 0:
        visited[j][k] = 1
        dfs(j-1,k,i)
        dfs(j+1,k,i)
        dfs(j,k-1,i)
        dfs(j,k+1,i)
        return True
    return False


n = int(input())
matrix, answer = [], []

#input 받아오고
for _ in range(n):
    matrix.append(list(map(int, sys.stdin.readline().split())))

# 강수량이 100까지 내리는데 굳이 100까지 다 돌지 않고 max만 알아내서 거기까지만 조사 하기 위해서 임의의 max_height 선언
max_height = -999

#max_height값을 알아내는 과정
for i in range(n):
    for j in range(n):
        max_height = max(max_height, matrix[i][j])

# 비가 안올 경우엔 그냥 1을 집어넣고, 비가 오면 max_height까지 반복문들 돌면서 잠긴 지역과 안잠긴 지역을 표현
for i in range(0, max_height + 1):
    if i == 0:
        answer.append(1)
        continue
    for j in range(n):
        for k in range(n):
            if matrix[j][k] <= i:
                matrix[j][k] = i
   
    visited = [[0] * n for _ in range(n)]
    ans = 0
    for a in range(n):
        for b in range(n):
            if dfs(a,b,i) == True:
                ans += 1
    answer.append(ans)
print(max(answer))

