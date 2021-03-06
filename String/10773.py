import collections

loop = int(input())
string_num = ''
number_list = collections.deque()
while loop > 0:
    num = int(input())
        if num == 0 and number_list[0] != 0:
            number_list.pop()
        else:
            number_list.append(num)
        loop -= 1
answer = 0
for number in number_list:
    answer += number

print(answer)

