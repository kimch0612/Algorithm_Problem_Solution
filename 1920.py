NA = []
MA = []
N = int(input())
NA.append(input().split(" "))
NA = sum(NA, [])
M = int(input())
MA.append(input().split(" "))
MA = sum(MA, [])
for _ in range(M):
    if MA[_] in NA:
        print("1")
    else:
        print("0")