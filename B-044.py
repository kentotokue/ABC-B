'''
Created on 2022/01/24

@author: kentoo
'''
from collections import defaultdict
W = str(input())

ans = defaultdict(int)

for i in range(len(W)):
    ans[W[i]] += 1 

for i in ans.values():
    if i % 2 != 0:
        print("No")
        exit()
print("Yes")
