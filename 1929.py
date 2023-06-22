m,n=map(int,input().split())

for i in range(m,n+1):
    if i==1:
        continue
    for _ in range(2,int(i**0.5)+1):
        if i%_==0:
            break
    else:
        print(i)