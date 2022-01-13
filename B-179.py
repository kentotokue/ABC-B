'''
Created on 2021/06/30

@author: kentoo
'''
N=int(input())

D=[list(map(int,input().split())) for _ in range(N)]


cnt=0

for i in range(N):

    if (D[i][0]==D[i][1]):
        cnt+=1
    else:
        cnt=0        
    if cnt==3:
        print("Yes")
        exit()
    

print("No")
      


            
        
