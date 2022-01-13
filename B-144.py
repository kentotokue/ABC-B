'''
Created on 2021/08/04

@author: kentoo
'''
N=int(input())

flag=False

for i in range(10):
    for j in range(10):
        if N==(i*j):
            flag=True
            break

if flag:
    print("Yes")
else:
    print("No")