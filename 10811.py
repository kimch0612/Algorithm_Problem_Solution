N, M = map(int, input().split())
basket_list = [0] * N
o = 1

for i in range(0, N):
    basket_list[i] = o
    o += 1

for o in range(0, M):
    i, j = map(int, input().split())
    i -= 1
    j -= 1
    
    q = 0
    basket_temp = [0] * int(j-i+1)
    for p in range(i, j+1):
        basket_temp[q] = basket_list[p]
        q += 1
    basket_temp.reverse()

    q = 0
    for p in range(i, j+1):
        basket_list[p] = basket_temp[q]
        q += 1

print(*basket_list)