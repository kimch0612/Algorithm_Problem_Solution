for _ in range(int(input())):
    R, S = input().split()
    SC = ''
    for i in S:
        SC += int(R) * i
    print(SC)