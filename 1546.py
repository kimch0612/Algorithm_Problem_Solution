N = int(input())
test_new = []
test_now = list(map(int, input().split()))
average = 0

for i in range(0, N):
    test_new.append(float(test_now[i] / max(test_now) * 100))

for i in range(0, N):
    average += test_new[i]

print(average/N)