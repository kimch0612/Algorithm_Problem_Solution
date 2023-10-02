import sys
n = int(input())
N_List = []
for _ in range(n):
    N_List.append(int(sys.stdin.readline()))
N_List.sort()
for i in N_List:
    print(i)