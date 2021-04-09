loop = int(input())
string_list = []

for i in range(loop):
    string_list.append(input())

ex_list = list(string_list[0])

for i in range(loop):
    for j in range(len(ex_list)):
        if ex_list[j] != string_list[i][j]:
            ex_list[j] = '?'
        else:
            continue
print(''.join(ex_list))
