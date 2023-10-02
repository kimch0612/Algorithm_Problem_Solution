import sys

N = int(sys.stdin.readline())
NN = list(map(int, sys.stdin.readline().split()))

print(min(NN), max(NN))