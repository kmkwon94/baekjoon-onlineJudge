loop = int(input())
string_list = []
while loop > 0:
    string = input()
    string_list.append(string)
    loop -= 1
string_list = list(set(string_list))
answer = (sorted(string_list, key=lambda x: (len(x), x)))

for string in answer:
    print(string)