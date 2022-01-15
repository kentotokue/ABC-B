'''
Created on 2022/01/15

@author: kentoo
'''
A,B,C,D = map(int,input().split())
print(max(0,min(B,D)-max(A,C)))
'''
if B < C or D < A :
    print("0")
    exit()
print(min(B,D)-max(A,C))
'''