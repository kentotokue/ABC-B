'''
Created on 2021/06/15

@author: kentoo
'''
N=int(input())

A=list(map(int,input().split()))
B=list(map(int,input().split()))

AM=max(A)
BM=min(B)

print(max(0,BM-AM+1))