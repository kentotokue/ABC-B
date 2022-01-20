'''
Created on 2022/01/19

@author: kentoo
'''

A,B,C = map(int,input().split())

for i in range(1,A*B+1):
    if (A*i) % B == C:
        print("YES")
        exit()
print("NO")