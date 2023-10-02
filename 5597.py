N = [i for i in range(1, 31)]

for i in range(28):
    applied = int(input())
    N.remove(applied)

print(min(N))
print(max(N))