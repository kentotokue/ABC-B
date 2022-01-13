'''
Created on 2021/12/03

@author: kentoo
'''
S = str(input())

Q = "oxx"

for i in range(100000):
    Q += "oxx"

if S in Q:
    print("Yes")
else:
    print("No")
    