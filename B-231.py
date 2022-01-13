'''
Created on 2021/12/11

@author: kentoo
'''
N = int(input())
S = [str(input())for i in range(N)]

ans = {}

for i in range(N):
    if S[i] in ans:
        ans[S[i]] += 1
    else:
        ans[S[i]] = 1

ans = sorted(ans.items(), key=lambda x:x[1], reverse=True)
print(ans[0][0])