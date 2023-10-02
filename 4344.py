case = int(input())

for i in range (case):
    N = list(map(int, input().split()))
    avg = sum(N[1:])/N[0]
    cnt = 0
    for score in N[1:]:
        if score > avg:
            cnt += 1
    rate = cnt/N[0] *100
    print(f'{rate:.3f}%')