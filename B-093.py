'''
Created on 2021/12/18

@author: kentoo
'''
A,B,K = map(int,input().split())

for i in range(A,min(A+K,B)):
    print(i)
    
for i in range(max(B-K+1,min(A+K,B)),B+1):
    print(i)
