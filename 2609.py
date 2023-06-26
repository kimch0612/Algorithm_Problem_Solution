import sys

a, b = map(int, sys.stdin.readline().split())
for _ in range(min(a,b),0,-1):
    if a%_ ==0 and b%_==0:
        print(_)
        break

for _ in range(max(a,b),(a*b)+1):
    if _%a==0 and _%b==0:
        print(_)
        break