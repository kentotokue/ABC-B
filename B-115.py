N = int(input())

P = [int(input()) for i in range(N)]

P.sort()
sum = P[N-1]//2

for i in range(N-1):
    sum += P[i]

print(sum)