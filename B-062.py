'''
Created on 2022/01/19

@author: kentoo
'''
H,W = map(int,input().split())

A = [str(input())for i in range(H)]
I = ""
for i in range(W+2):
    I += "#"
A.insert(0,I)
A.append(I)

for i in range(1,H+1):
    A[i] = "#" + A[i] +"#"

for i in range(H+2):
    print(A[i])
