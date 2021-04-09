import sys

data = [sys.stdin.readline().strip() for i in range(5)]
MAX_INPUT = 15
for idx in range(len(data)):
    if len(data[idx]) < MAX_INPUT :
        times = MAX_INPUT - len(data[idx])  
        data[idx] = data[idx] + (' ' * times) 

new_word = ''
for i in range(MAX_INPUT):
    for j in range(len(data)):
        new_word += data[j][i]

new_word = new_word.replace(' ','')
print(new_word)
'''
    [0][0]
    [1][0]
    [2][0]
    [3][0]
    [4][0]
'''