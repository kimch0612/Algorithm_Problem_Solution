N = set(range(1, 10001))
NN = set()

for i in range(1, 10001):
    for n in str(i):
        i += int(n)
    NN.add(i)

self = sorted(N - NN)
for i in self:
    print(i)