'''
Created on 2021/12/11

@author: kentoo
'''
N = int(input())
S = str(input())
ans = 0
for i in range(N):
    A = S[:i+1]
    B = S[i+1:]
    AS = {}
    BS = {}

    for j in range(len(A)):
        if A[j] in AS:
            AS[A[j]] += 1
        else:
            AS[A[j]] = 1
    
    for k in range(len(B)):
        if B[k] in BS:
            BS[B[k]] += 1
        else:
            BS[B[k]] = 1
    AS = dict(sorted(AS.items()))
    BS = dict(sorted(BS.items()))
    cnt = 0
    for l in AS.keys():
        for m in BS.keys():
            if l == m :
                cnt += 1
    ans = max(ans,cnt)
                
    #print(AS,BS)
 
                
print(ans)
'''
ans = {}
for i in range(N):
    if S[i] in ans:
        ans[S[i]] += 1
    else:
        ans[S[i]] = 1

print(len(ans)) 
'''