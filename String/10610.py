string = input()

string = sorted(string, reverse=True)
sum = 0
if '0' not in string:
    print('-1')
else:
    for idx in range(len(string) - 1):
        sum += int(string[idx])
    if sum % 3 == 0:
        print(''.join(string))
    else:
        print('-1')
