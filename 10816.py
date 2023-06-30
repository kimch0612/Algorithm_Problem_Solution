N = int(input())
N_list = input().split()
M = int(input())
M_list = input().split()

for _ in range(M):
    M_list[_] = N_list.count(M_list[_])

print(*M_list)