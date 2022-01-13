'''
Created on 2021/09/07

@author: kentoo
'''
S = str(input())

T = "ATCG"

ans = 0
now = 0

for i in range(len(S)):
    
    isATCG = False
    
    for j in range(len(T)):
        if S[i]==T[j]:
            isATCG = True
    
    if isATCG:
        now += 1
        ans = max(ans,now)
    else:
        now = 0
    
print(ans)