'''
Created on 2021/12/09

@author: kentoo
'''
N = int(input())
A = list(map(int,input().split()))

A.sort()

print(abs(A[0]-A[-1]))