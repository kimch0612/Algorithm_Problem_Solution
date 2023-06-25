import sys
N = int(sys.stdin.readline())
NN = map(int, sys.stdin.readline().split())
NNN = 0
for _ in NN:
    err = 0
    if _ > 1:
        for __ in range(2, _):
            if _ % __ == 0:
                err += 1
        if err == 0:
            NNN += 1
print(NNN)