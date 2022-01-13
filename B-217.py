'''
Created on 2021/09/04

@author: kentoo
'''
A =[]
for i in range(3):
    A.append(str(input()))
    
C = ['ABC','ARC','AGC','AHC']
for i in range(3):
    C.remove(A[i])


print(C[0])