'''
Created on 2021/09/26

@author: kentoo
'''

K = int(input())
A,B = map(str,input().split())

def C (X,n):
    out = 0
    for i in range(1,len(str(X))+1):
        out += int(X[-i])*(n**(i-1))
    return out 

print(C(A,K)*C(B,K))
