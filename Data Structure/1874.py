'''
#스택수열

1~N까지 차례로 스택에 넣는다.
주어진 입력값으로 수열이 완성되게끔 push와 pop을 이용한다.
@ input_list를 잘 이용해야함. 빼면 복원되지 않음
8 - > [1,2,3,4,5,6,7,8]

4 -> 어 4가 들어왔네 지금 top은 없어 그럼 4까지 push한 뒤 pop [1,2,3]
3 -> 3을 원하네? 근데 지금 top은 3 ok 바로 pop [1,2]
6 ->6을 원하네? 근데 지금 top는 2 그럼 push를 해야지 6까지 push 하고 pop
                  [1,2,5]
8 -> 8을 원하네? 근데 지금 top은 5 그럼 push를 해야지 8까지 push 하고 pop
                  [1,2,5,7]
7 ->7을 원하네? 근데 지금 top은 7 ok 바로 pop [1,2,5]
5 -> 5를 원하네? 근데 지금 top은 5 ok 바로 pop [1,2]
2 -> 2를 원하네? 근데 지금 top은 2 ok 바로 pop [1]
1 -> 1을 원하네? 근데 지금 top은 1 ok 바로 pop

그래서 loop가 끝나고 최종적으로 stack이 안비어있으면 'no'
'''
from collections import deque
import sys

TC = int(input())


def push(stack: list, num: int):
    global ans
    for _ in range(input_list.index(num) + 1):
        stack.append(input_list.popleft())
        ans += "+"


def top() -> int:
    return stack[-1]


def pop():
    global ans
    stack.pop()
    ans += "-"


input_list = deque([i + 1 for i in range(TC)])
stack = []
ans = ''
for _ in range(TC):
    num = int(sys.stdin.readline())
    if not stack:
        push(stack, num)
    if top() == num:
        pop()
    elif top() < num:
        push(stack, num)
        if top() == num:
            pop()
if stack:
    print("NO")
else:
    for i in ans:
        print(i)
