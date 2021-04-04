string = input()
'''
1. 문자열을 입력받아서 순회
2. 순회하면서 ord()함수를 통해 숫자를 획득해냄
3. 순자에 13을 더하는데 소문자 혹은 대문자의 범위에 벗어나는 숫자라면
  3-1. 벗어난 범위만큼 소문자는 97에 대문자는 65에 더해준다.
4. 영 대,소문자가 아닌 문자들은 적용하지 않는다.
'''
new_letter = ''
for i in string:
    if i.isupper():
        if ord(i) + 13 > 90:
            new_letter += chr(64 + ((ord(i) + 13) - 90))
        else:
            new_letter += chr(ord(i) + 13)
    elif i.islower():
        if ord(i) + 13 > 122:
            new_letter += chr(96 + ((ord(i) + 13) - 122))
        else:
            new_letter += chr(ord(i) + 13)
    else:
        new_letter += i

print(new_letter)
