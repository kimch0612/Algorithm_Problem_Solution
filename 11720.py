a = int(input())
b = list(map(int, input()))
result = 0

for i in range(0, len(list(b))):
    result += b[i]

print(result)