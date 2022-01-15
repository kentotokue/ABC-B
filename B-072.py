'''
Created on 2022/01/15

@author: kentoo
'''

S = str(input())

ans = ""
for i in range(len(S)):
    if (i+1) % 2 == 0:
        continue
    else:
        ans += S[i]
print(ans)
    