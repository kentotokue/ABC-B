'''
Created on 2021/07/29

@author: kentoo
'''
a,b=map(int,input().split())

A=str(a)*b 
B=str(b)*a 


ans=[]
ans.append(A)
ans.append(B)

ans.sort()

print(ans[0])
