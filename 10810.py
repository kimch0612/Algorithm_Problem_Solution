N, M = map(int, input().split())
basket_list = [0] * int(N)
for o in range(0, M):
    i, j, k = map(int, input().split())
    i -= 1
    j -= 1
    while True:
        if i <= j:
            basket_list[i] = k
            i += 1
        else:
            break

print(*basket_list)