'''
Created on 2021/09/24

@author: kentoo
'''

A,B,K = map(int,input().split())

ans = []
L = min(A,B)
for i in range(L,0,-1):
    if A%i ==0 and B%i == 0:
        K -= 1
        print(i)
        if K==0:
            print(i)
            exit()
