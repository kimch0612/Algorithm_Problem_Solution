N = int(input())
devil = 666

while N != 0:
    if '666' in str(devil):
        N = N-1
        if N == 0:
            break
    devil = devil + 1
print(devil)