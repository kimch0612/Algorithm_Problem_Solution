word = []
word_list = []
tmp = ""
i = 0
for _ in range(0, 5):
    word.append(input())

for _ in range(len(word[_])):
    word_list.append(list(word[_]))

for _ in range(0, 5):
    try:
        tmp += word_list[i][_]
    except:
        pass
    print(tmp, end="")
    i += 1