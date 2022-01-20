'''
Created on 2022/01/20

@author: kentoo
'''

O = str(input())
E = str(input())

S = len(O) + len(E)

ans = ""
cntO = 0
cntE = 0
for i in range(1,S+1):
    if i % 2 == 0:
        ans += E[cntE]
        cntE += 1
    else:
        ans += O[cntO]
        cntO += 1
print(ans)