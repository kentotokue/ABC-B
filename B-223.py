'''
Created on 2021/10/17

@author: kentoo
'''
S = str(input())
ans = [S]
for i in range(len(S)):
    A = S[0]
    S = S[1:]
    
    S = S + A 
    
    ans.append(S)
ans.sort()
print(ans[0])
print(ans[len(S)])