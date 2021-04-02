name = input()

name.replace('-', '')
last_name = ''
for i in name:
    if i.isupper():
        last_name += i

print(last_name)
