'''
Created on 2022/01/23

@author: kentoo
'''
N = int(input())
S = str(input())

x = 0 
ans = 0
for i in range(N):
    if S[i] == "I":
        x += 1
    else:
        x -= 1
    ans = max(ans,x)
print(ans)