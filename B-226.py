'''
Created on 2021/11/07

@author: kentoo
'''
N = int(input())

L = [list(map(str,input().split())) for i in range(N)]

ans = []
for i in range(N):
    #del L[i][0]
    ans.append('+'.join(L[i]))
#print(L)
print(ans)
print(len(set(ans)))
'''
A = {}
for i in range(N):
    if L[i] in A:
        A[L[i]] += 1
    else:
        A[L[i]] = 1
print(A)
'''