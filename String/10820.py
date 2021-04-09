'''
문자열 N개가 주어진다. 이때, 문자열에 포함되어 있는 소문자, 대문자, 숫자, 공백의 개수를 구하는 프로그램을 작성하시오.

각 문자열은 알파벳 소문자, 대문자, 숫자, 공백으로만 이루어져 있다.

소문자 / 대문자 / 숫자 / 공백 을 공백을 기준으로 return

'''
import sys

while True:
    string = sys.stdin.readline().rstrip('\n')

    if not string:
        break

    l, u, n, s = 0, 0, 0, 0

    for letter in string:
        if letter.islower():
            l += 1
        elif letter.isupper():
            u += 1
        elif letter.isalnum():
            n += 1
        else:
            s += 1

    print(l, u, n, s)
