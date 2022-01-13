'''
Created on 2021/07/29

@author: kentoo
'''

N=int(input())
A=list(map(int,input().split()))

for i in range(len(A)):
    
    if A[i]%2==0:
        
        if A[i]%3==0 or  A[i]%5==0:
            continue
            
        else:
            print("DENIED")
            exit()
    else:
        continue 
print("APPROVED")
            