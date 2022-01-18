'''
Created on 2022/01/18

@author: kentoo
'''
from collections import defaultdict
S = str(input())

ans = defaultdict(int)

for i in range(len(S)):
    ans[S[i]] += 1
if len(S) == len(ans):
    print("yes")
else:
    print("no")