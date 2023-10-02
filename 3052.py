import sys
N = []
NN = []

for i in range(1, 11):
    N.append(int(sys.stdin.readline()))

for i in range(0, 10):
    NN.append(int(N[i]%42))

NN = set(NN)
print(len(NN))