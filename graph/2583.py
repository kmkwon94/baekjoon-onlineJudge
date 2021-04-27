'''
# 2583 - 영역 구하기 

좌표에 K개의 직사각형을 그릴때 직사각형이 그려진 부분을 제외한
나머지 영역의 갯수를 구하고, 그 크기를 구하시오

입력 M : 세로
     N : 가로
     K : K개의 직사각형 

5 7 3
0 2 4 4
1 1 2 5
4 0 6 2
'''

import sys

sys.setrecursionlimit(10**7) 

def dfs(x,y):
    global cnt
    # 좌표 바깥으로 나간 값들은 return False
    if x < 0 or x >= n or y <0 or y >= m:
        return False,cnt
    
    # 직사각형이 존재하는 부분은 return False
    if matrix[x][y] == 1:
        return False,cnt
    
    # 방문하지 않았으면
    if visited[x][y] == 0:
        visited[x][y] = 1 # 방문처리 후 dfs
        cnt += 1 # 직사각형의 갯수가 곧 넓이이므로 카운트 세줌
        dfs(x-1,y)
        dfs(x+1,y)
        dfs(x,y-1)
        dfs(x,y+1)
        return True,cnt 
    return False,cnt

m,n,k = map(int, sys.stdin.readline().split())
matrix = [[0] * (m) for _ in range(n)]
visited = [[0] * (m) for _ in range(n)]
cnt = 0
tf_count = 0
size_list = []
for _ in range(k):
    x1,y1,x2,y2 = map(int,sys.stdin.readline().split())
    
    for i in range(x1,x2):
        for j in range(y1, y2):
            matrix[i][j] = 1

for i in range(n):
    for j in range(m):
        cnt = 0
        tf, size = dfs(i,j)
        if tf == True: # dfs가 온전히 끝났으면
            tf_count += 1 # 끝난 횟수를 센다. 즉 영역의 갯수
            size_list.append(size) #넓이는 size_list에 추가
size_list.sort() #오름차순 정렬
print(tf_count) 

for i in size_list:
    print(i, end= ' ')
