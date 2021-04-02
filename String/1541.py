arr = input().split('-')  #들어오면 - 단위로 끝어낸 list 형태
s = 0
for i in arr[0].split('+'):  # - 단위로 정리된 list를 이번엔 + 로 정리
    s += int(i)
for i in arr[1:]:
    for j in i.split('+'):
        s -= int(j)
print(s)