'''
Created on 2021/06/30

@author: kentoo
'''
a,b,c,d=map(int,input().split())

ans=max(a*c,a*d,b*c,b*d)
print(ans)

