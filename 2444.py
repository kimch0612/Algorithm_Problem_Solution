N = int(input())
NN = "*"
NNN = " "
for i in range(1, N+1):
    print(NNN*(N-i) + NN*i + (NN*int(i-1)))
for i in range(1, N):
    print(NNN*int(i) + NN*int(N-i) + NN*int(N-i-1))