N = int(input())
Word = []

for _ in range(N): # 리스트 중복제거
    Word_temp = str(input())
    if Word_temp not in Word:
        Word.append(Word_temp)

Word.sort() # abc순으로 정렬
Word.sort(key=len) # 길이순으로 정렬

for _ in range(N):
    try:
        print(Word[_])
    except:
        quit()