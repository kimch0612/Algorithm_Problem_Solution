N, M = map(int, input().split())
basket = [0] * N
o = 1

for i in range(0, N):
    basket[i] = o
    o += 1

for __ in range(0, M):
    o = 0
    i, j, k = map(int, input().split())
    basket_temp = [0] * int(j-i+1)
    basket_begin = [0] * int()

# for __ in range(0, M):
#     o = 0
#     i, j, k = map(int, input().split())
#     basket_temp = [0] * int(j-i+1)
#     basket_begin = [0] * int(k-4)
#     basket_end = [0] * int(j-k+1)
#     for _ in range(0, int(j-i+1)):
#         basket_temp[_] = basket[i+_-1]
#     for _ in range(0, int(k-4)):
#         basket_begin[_] = basket_temp[_]
#     for _ in range(0, j-k+1):
#         basket_end [_] = basket_temp[k+_-1]
#     # for _ in range(0, j-k+1):
#     #     basket[o] = basket_end[_]
#     #     o += 1
#     # for _ in range(0, int(k-2)):
#     #     basket[o] = basket_begin[_]
#     #     o += 1
#     # basket[o] = int(k-1)

print(*basket)
print(*basket_temp)
print(*basket_begin)
print(*basket_end)
print(*basket)