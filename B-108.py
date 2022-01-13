'''
Created on 2021/11/28

@author: kentoo
'''
X1,Y1,X2,Y2 = map(int,input().split())

dx = X2-X1
dy = Y2-Y1 
print(dx,dy)

X3 = X2 - dy 
Y3 = Y2 + dx 

X4 = X3 - dx
Y4 = Y3 - dy

print(X3,Y3,X4,Y4)
