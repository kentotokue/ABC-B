'''
Created on 2021/06/24

@author: kentoo
'''
N=int(input())
A=[]
B=[]
sum=0
for i in range(N):
    a,b=map(int,input().split())
    
    
    sum+=b*(b+1)//2-a*(a-1)//2
        
        
print(sum)
        