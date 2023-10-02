N, X = map(int, input().split())
A = input().split()
AA = []

for i in range(N):
    if int(A[i]) < int(X):
        AA.append(A[i])

for i in range(len(AA)):
    print(AA[i] + ' ', end='')