number = int(input())

def check_under_ten(number):
    if number < 10:
        number = '0' + str(number)
    else:
        number = str(number)
    return number

#############################
def change_number(number):
    number = check_under_ten(number)
    sum_number = check_under_ten(int(number[0]) + int(number[1]))
    return number, sum_number


origin_number = number
new_number = -1
count = 0
while int(new_number) != origin_number:
    count += 1
    number, sum_number = change_number(number)
    new_number = number[1] + sum_number[1]
    number = int(new_number)

print(count)
'''

 26 -> 2 + 6 = 8 
 is 68 == 26?
 68 -> 6 + 8 = 14
 is 84 == 26?
 84 -> 8 + 4 = 12
 is 42 == 26?
 42 -> 4 + 2 = 6
 is 26 == 26?
 26

 0 -> 00 -> 0 + 0 = 0
 is 0 == 0 
'''
