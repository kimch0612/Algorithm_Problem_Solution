A = input()
B = input()
C = input()
D = input()
E = input()
output = ""

for _ in range(0, 16):
    try:
        output += str(list(A)[_])
    except:
        pass
    try:
        output += str(list(B)[_])
    except:
        pass
    try:
        output += str(list(C)[_])
    except:
        pass
    try:
        output += str(list(D)[_])
    except:
        pass
    try:
        output += str(list(E)[_])
    except:
        pass

print(output)