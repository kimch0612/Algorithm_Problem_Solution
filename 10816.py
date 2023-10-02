import sys

N = int(sys.stdin.readline())
N_list = sys.stdin.readline().split()
M = int(sys.stdin.readline())
M_list = sys.stdin.readline().split()

for _ in range(M):
    M_list[_] = N_list.count(M_list[_])

print(*M_list)