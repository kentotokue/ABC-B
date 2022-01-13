'''
Created on 2021/07/24

@author: kentoo
'''
X=int(input())

sum=100 
cnt=0
while X>sum:
    
    sum+=(sum//100)
    cnt+=1

print(cnt)
    
    