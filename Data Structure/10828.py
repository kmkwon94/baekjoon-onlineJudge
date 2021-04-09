'''
스택구현
1. push X : 정수 X를 스택에 넣는 행위
2. pop : 스택에서 가장 위의 수를 빼고, 그 수를 출력. 없을경우 -1 출력
3. size : 스택에 들어있는 정수의 개수를 출력
4. empty : 스택이 비어있으면 1, 아니면 0 출력
5. top : 스택의 가장 위에 있는 정수를 출력, 만약 정수가 없을경우 -1
'''
import sys
import collections

TEST_CASE = int(input())
stack = collections.deque()


def push(number: str):
    stack.append(number)


def pop():
    if stack:
        print(stack.pop())
    else:
        print(-1)


def size():
    print(len(stack))


def empty():
    if stack: print(0)
    else: print(1)


def top():
    if stack:
        print(stack[len(stack) - 1])
    else:
        print(-1)


for _ in range(TEST_CASE):
    cmd = sys.stdin.readline()

    if 'push' in cmd:
        cmd = cmd.split()
        push(cmd[1])
    elif 'pop' in cmd:
        pop()
    elif 'size' in cmd:
        size()
    elif 'empty' in cmd:
        empty()
    elif 'top' in cmd:
        top()
