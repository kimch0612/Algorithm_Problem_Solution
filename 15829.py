L = int(input())
string = input()
output = 0

for i in range(L):
    output += (ord(string[i])-96) * (31 ** i)
print(output % 1234567891)