'''
Created on 2022/01/23

@author: kentoo
'''
S = str(input())

A = [n for n, v in enumerate(S) if v == "A"]
Z = [n for n, v in enumerate(S) if v == "Z"]



ans = max(Z)-min(A) + 1


print(ans)