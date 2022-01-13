'''
Created on 2021/06/23

@author: kentoo
'''
Sx,Sy,Gx,Gy=map(float,input().split())

print((Gx-Sx)*((Sy)/(Sy+Gy))+Sx)