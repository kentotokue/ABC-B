'''
Created on 2021/11/13

@author: kentoo
'''
N = int(input())
S = list(map(int,input().split()))
cnt = 0
for i in range(N):
    
    for j in range(1,150):
        for k in range(j,150):
            M = (3*j)+(4*j*k)+(3*k)
            if S[i] == M:
                cnt += 1
                #print(S[i])
                #print(j,k)
                break
        else:
            continue
        break
            
            
        
            
                
            
        
        
print(N-cnt)
            
                