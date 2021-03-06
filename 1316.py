test_num = int(input())
count = 0
#'happy'
for _ in range(test_num):
    previous_word = ''
    ban_list = []  # 한 번 들어왔기 때문에 또 들어오면 그룹단어가 아니게 됌
    flag = True
    words = input()
    for word in words:
        if word not in ban_list:
            ban_list.append(word)
            previous_word = word
        else:
            if word == previous_word:
                previous_word = word
                ban_list.append(word)
                continue
            else:
                flag = False
                break
    if flag: count += 1

print(count)
