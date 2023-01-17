a = int(input(""))
b = int(input(""))
c = []
for i in map(int, str(b)):
    c.append(i)

three = a*int(c[2])
four = a*int(c[1])
five = a*int(c[0])
six = a*b

print(three)
print(four)
print(five)
print(six)