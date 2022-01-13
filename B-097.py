'''
Created on 2021/12/11

@author: kentoo
'''
X = int(input())
ans = 1
for i in range(1,1000):
    for j in range(2,1000):
        if i**j > X:
            break 
        #print(i,j,i**j)
        ans = max(ans,i**j)
    
print(ans)
        