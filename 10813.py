N, M = map(int, input().split())
basket_list = [0] * N
o = 1

for i in range(0, N):
    basket_list[i] = o
    o += 1

for p in range(0, M):
    i, j = map(int, input().split())
    i -= 1
    j -= 1
    temp = basket_list[i]
    basket_list[i] = basket_list[j]
    basket_list[j] = temp

print(*basket_list)