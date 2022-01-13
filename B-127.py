'''
Created on 2021/09/04

@author: kentoo
'''
r,D,X = map(int,input().split())


for i in range(10):
    print(r*X-D)
    X = r*X-D