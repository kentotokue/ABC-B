'''
Created on 2021/11/27

@author: kentoo
'''

A,B = map(str,input().split())
A1 = max(A,B)
B2 = min(A,B)
MaL = len(max(A,B))
ML = len(min(A,B))
S = MaL - ML
for i in range(ML-1,-1,-1):
    #print(i,int(A1[i+S]),int(B2[i]))



    if (int(A1[i+S])+int(B2[i])) > 9:

        print("Hard")
        exit()
print("Easy") 

