'''
Created on 2021/07/24

@author: kentoo
'''

A,B,C,D=map(int,input().split())


for i in range(1000):
    
    C-=B 
    if C<=0:
        print("Yes")
        exit()
    A-=D 
    if A<=0:
        print("No")
        exit()
    
    