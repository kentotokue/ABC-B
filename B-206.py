'''
Created on 2021/06/19

@author: kentoo
'''
N=int(input())
sum=0

for i in range(1,1000000000):
    sum+=i
    
    if sum>=N:
        print(i)
        break

    
    
    
    