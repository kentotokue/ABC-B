'''
Created on 2021/07/31

@author: kentoo
'''

A,B,K=map(int,input().split())

if A>K:
    print(f"{A-K} {B}")
else:
    print(f"{0} {max(B-(K-A),0)}")