N, B = map(int, input().split())
output = ''

word = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

while N!=0:
    output += str(word[N%B])
    N //= B

print(output[::-1])