'''
Created on 2021/12/19

@author: kentoo
'''
N = int(input())
S = list(map(str,input().split()))
S = len(sorted(set(S)))

'''
ans = {}
for i in range(N):
    if S[i] in ans:
        ans[S[i]] += 1
    else:
        ans[S[i]] = 1

if len(ans) == 3:
    print("Three")
else:
    print("Four")
'''
if S == 3:
    print("Three")
else:
    print("Four")