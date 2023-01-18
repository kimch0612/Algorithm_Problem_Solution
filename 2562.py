import sys
NN = []

for i in range(0, 9):
    N = int(sys.stdin.readline())
    NN.append(N)

print(max(NN))
print(NN.index(max(NN)) + 1)