case = int(input())
OX = []
Sum_Temp = []
Sum = []

for i in range(0, case):
    OX.append(input())
    OX[i] = OX[i].split("X")
    OX[i] = [v for v in OX[i] if v]

for i in range(0, len(OX)):
    Sum_Temp.append(int(len(OX[0][i])))

print(Sum_Temp)

for i in range(0, len(Sum)):
    for t in range(1, Sum_Temp[i]+1):
        Sum += t
        
print(Sum)