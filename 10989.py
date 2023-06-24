N = int(input())
N_list = [0] * 10001
for _ in range(N):
    N_list[int(input())] += 1
for _ in range(10001):
    if N_list[_] != 0:
        for __ in range(N_list[_]):
            print(_)