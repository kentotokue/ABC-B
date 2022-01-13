'''
Created on 2021/12/09

@author: kentoo
'''
N = int(input())
S = str(N)
ans = 0
for i in range(len(S)):
    ans += int(S[i])

if N % ans == 0:
    print("Yes")
else:
    print("No")