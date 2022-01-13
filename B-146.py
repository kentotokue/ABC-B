'''
Created on 2021/08/03

@author: kentoo
'''
N=int(input())
S=str(input())

A=["A","B","C","D","E","F","G","H","I","J","K","L",
   "M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

ans=""
for i in range(len(S)):
    
    #ans+=A[min((A.index(S[i])+N)%26,25)]
    ans+=A[(A.index(S[i])+N)%26]

print(ans)