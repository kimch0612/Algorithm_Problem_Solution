T = input()
for i in range(int(T)):
    a, b = map(int, input().split())
    print("Case #%s: %s + %s = %s"%(i+1, a, b, a+b))