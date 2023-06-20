N = int(input())
output = 1
NN = 0

for _ in range(1, N+1):
    output *= _

for _ in range(len(str(output))):
    if list(str(output))[_] == "0":
        NN += 1

print(NN)