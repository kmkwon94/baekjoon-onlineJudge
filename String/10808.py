import collections
alpha = 'abcdefghijklmnopqrstuvwxyz'
string = input()

default_dict = collections.defaultdict(int)

for letter in alpha:
    default_dict[letter]

for letter in string:
    default_dict[letter] += 1

for values in default_dict.values():
    print(values, '', end='')
