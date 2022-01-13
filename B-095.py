'''
Created on 2021/12/15

@author: kentoo
'''
N,X = map(int,input().split())
sum = 0
M = []
for i in range(N):
    m = int(input())
    sum += m 
    M.append(m)

M.sort()

if sum == X:
    print(len(M))
    exit()
X -= sum
cnt = len(M)
'''
while True:
    X -= M[0]
    if X < 0:
        break

    cnt += 1
    #print(X,cnt)
'''

print(cnt+X//M[0])
