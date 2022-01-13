'''
Created on 2021/09/11

@author: kentoo
'''
P = list(map(int,input().split()))

A =['a',"b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

for i in range(26):
    print(A[P[i]-1],end="")