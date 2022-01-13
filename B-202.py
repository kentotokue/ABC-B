'''
Created on 2021/06/14

@author: kentoo
'''
S=str(input())
A=[]


for i in range(len(S)):
    A.append(int(S[i]))
    if S[i]=="6":
        A[i]=9
    elif S[i]=="9":
        A[i]=6

for i in range(len(A)-1,-1,-1):
    print(A[i],end="")
