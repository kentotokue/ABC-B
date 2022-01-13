'''
Created on 2021/06/16

@author: kentoo
'''
x=input()
d=x.find(".")
if d!=-1:
    x=x[:d]

print(x)