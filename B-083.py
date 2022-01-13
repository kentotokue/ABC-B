'''
Created on 2021/12/25

@author: kentoo
'''
N,A,B = map(int,input().split())
ans = 0
for i in range(1,N+1):
    I = str(i)
    L = len(I)
    sum = 0
    for j in range(L):
        sum += int(I[j])
    #print(sum)
    if A <= sum and sum <= B:
        ans += i
        #print(i,sum)
    #print(ans)
print(ans)