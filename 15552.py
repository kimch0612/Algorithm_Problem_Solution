import sys

T = sys.stdin.readline()
for i in range(int(T)):
    a, b = map(int, sys.stdin.readline().split())
    print(a+b)