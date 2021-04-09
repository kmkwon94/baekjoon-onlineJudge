'''
push X: 정수 X를 큐에 넣는 연산이다.
pop: 큐에서 가장 앞에 있는 정수를 빼고, 그 수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
size: 큐에 들어있는 정수의 개수를 출력한다.
empty: 큐가 비어있으면 1, 아니면 0을 출력한다.
front: 큐의 가장 앞에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
back: 큐의 가장 뒤에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.

'''
import sys
import collections

def push(x : str):
  queue.append(x)

def pop():
  if queue:
    print(queue.popleft())
  else: print(-1)

def size():
  print(len(queue))

def empty():
  if queue:print(0)
  else : print(1)

def front():
  if queue:
    print(queue[0])
  else:
    print(-1)

def back():
  if queue:
    print(queue[len(queue)-1])
  else:
    print(-1)
    
TC = int(input())
queue = collections.deque()

for _ in range(TC):
  cmd = sys.stdin.readline().split()
  
  for core in cmd:
    if 'push' in core:
      push(cmd[1])
    elif 'pop' in core:
      pop()
    elif 'size' in core:
      core()
    elif 'empty' in core:
      empty()
    elif 'front' in core:
      front()
    elif 'back' in core:
      back()