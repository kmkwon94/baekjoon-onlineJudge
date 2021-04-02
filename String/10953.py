loop = int(input())

while loop > 0:
    string = input()
    string_list = string.split(',')
    answer = int(string_list[0]) + int(string_list[1])
    print(answer)
    loop -= 1
