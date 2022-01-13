'''
Created on 2021/11/25

@author: kentoo
'''
N = int(input())
L = list(map(int,input().split()))
'''
M = max(L)
I = L.index(M)
sum = 0
for i in range(N):
    if i == I:
        continue
    sum += L[i]

if M < sum:
    print("Yes")
else:
    print("No")
''' 
L.sort(reverse = True)
sum = 0
for i in range(1,N):
    sum += L[i]
if L[0] < sum:
    print("Yes")
else:
    print("No")