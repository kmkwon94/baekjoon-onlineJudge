import collections
import sys
test_case = int(input())
for _ in range(test_case):
    func = sys.stdin.readline().strip()
    length = sys.stdin.readline().strip()
    contents = sys.stdin.readline().strip()[1:-1].split(',')
    reverse_flag = 0
    error_flag = 0

    contents = collections.deque(contents)
    for letter in func:
        if letter == 'R':
            if reverse_flag == 0:
                reverse_flag = 1
            else:
                reverse_flag = 0
        else:
            if contents and contents[0] != '':
                if reverse_flag == 1:
                    contents.pop()
                else:
                    contents.popleft()
            else:
                error_flag = 1
                break
    if error_flag == 1:
        print("error")
    else:
        if reverse_flag == 1:
            contents.reverse()
        print("[", end='')
        for i in range(len(contents)):
            if i == len(contents) - 1:
                print(str(contents[i]), end='')
            else:
                print(contents[i], end=',')
        print("]")
