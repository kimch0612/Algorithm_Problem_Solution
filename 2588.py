a = int(input(""))
b = int(input(""))
c = []
d = []
e = []
f = []
g = []

for i in map(int, str(b)):
    c.append(i)

three = a*int(c[2])
four = a*int(c[1])
five = a*int(c[0])
six = a*b

for i in map(int, str(three)):
    d.append(i)
for i in map(int, str(four)):
    e.append(i)
for i in map(int, str(five)):
    f.append(i)

print(three)
print(four)
print(five)
print(six)