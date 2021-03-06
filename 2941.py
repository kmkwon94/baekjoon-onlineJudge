CNADIDATE_LIST = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

words = input()

for candidate in CNADIDATE_LIST:
    if candidate in words:
        words = words.replace(candidate, '*')

print(len(words))
