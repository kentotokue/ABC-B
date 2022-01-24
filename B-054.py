'''
Created on 2022/01/23

@author: kentoo
'''
N,M = map(int,input().split())

A = [str(input())for i in range(N)]
B = [str(input())for i in range(M)]


for i in range(N-M+1):
    for j in range(N-M+1):
        
        C = []
        
        for k in range(M):

            C.append(A[k+i][j:j+M])
            #print(A[k+i][j:j+M])
            #print(C)
        if B == C :
            print("Yes")
            exit()

print("No")
       
        
            
        
