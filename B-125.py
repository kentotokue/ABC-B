'''
Created on 2021/09/06

@author: kentoo
'''
N = int(input())

V = list(map(int,input().split()))
C = list(map(int,input().split()))

ans = 0
for i in range(N):
    
    ans += max(V[i]-C[i],0)
    '''
    if V[i]-C[i]>0:
        ans += V[i]-C[i]
    else:
        continue
    '''

print(ans)