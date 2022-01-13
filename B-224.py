'''
Created on 2021/10/23

@author: kentoo
'''
H,W = map(int,input().split())
A = [list(map(int,input().split()))for i in range(H)]
cnt = 0
for i in range(H):
    for j in range(i,H):
        if i == j :
            continue
        #print(i,j)
        
        for k in range(W):
            for g in range(k,W):
                
                if k == g:
                    continue
                #print(i,j,k,g)
                if (A[j][k]+A[i][g])-(A[i][k]+A[j][g]) < 0:
                    
                    print("No")
                    exit()


print("Yes")

