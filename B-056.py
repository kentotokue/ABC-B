'''
Created on 2022/01/20

@author: kentoo
'''
W,a,b = map(int,input().split())

if (a + W) < (b + W):
    print(max(0,b-(a+W)))
else:
    print(max(0,a-(b+W)))

    

    
    