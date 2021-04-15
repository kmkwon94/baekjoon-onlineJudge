'''
# 쇠막대기 - 구글링
https://claude-u.tistory.com/331

() -> 이렇게 바로 인접한 괄호가 나오면 레이저이다
((())) -> 괄호가 인접하지 않게 나오면 쇠막대기이다.

()(((()())(())()))(())
  
  쇠막대기 조건
1. 쇠막대기는 자기 자신보다 긴 쇠막대기 위에만 존재할 수 있다.
2. 쇠막대기기 위에 존재한다면 아래 쇠막대기의 양 끝점 안에 있다.
   - 즉 완전히 포함된다
3. 레이저는 쇠막대기의 양 끝점에 존재할 수 없다.

레이저로 잘려진 쇠막대기의 총 개수를 구하라

if ( 이 들어오면 stack에 채워

else
    if input_[i-1]이 ( 이면 
      stack에서 ( 을 pop 하고 stack의 갯수만큼 answer에 더해
    else: #즉 지금 ) 인데 input_[i-1]도 ) 이면 끄트머리 막대를 더해
      stack에서 ( 을 pop 하고 answer += 1  
'''
import sys

input_ = sys.stdin.readline().rstrip()

answer = 0
stack = []
for i in range(0, len(input_)):
    if input_[i] == '(':
        stack.append(input_[i])
    else:
        if input_[i - 1] == '(':
            stack.pop()
            answer += len(stack)
        else:
            stack.pop()
            answer += 1

print(answer)
