'''
# 1259 - 펠린드롬 수
'''

while True:
    number = input()

    left = 0
    right = len(number) - 1
    flag = True

    if number == '0':
        break

    while left < right:
        if number[left] == number[right]:
            left +=1
            right -=1
        else:
            flag = False
            print("no")
            break
  
    if flag:
        print("yes")
