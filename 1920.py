import sys

N = int(sys.stdin.readline())
NA = set(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())
MA = list(map(int, sys.stdin.readline().split()))

for i in MA:
    if i in NA:  
        print(1)
    else:
        print(0)