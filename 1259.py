word_list = []

while True:
    word = input()
    if word == "0":
        break
    else:
        word_list.append(word)

for _ in range(len(word_list)):
    if str(word_list[_]) == str(word_list[_])[::-1]:
        print("yes")
    else:    
        print("no")