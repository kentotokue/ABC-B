'''
Created on 2021/11/27

@author: kentoo
'''
N = int(input())

for i in range(N,1000):
    a = i // 100
    #print(a)
    if (a*100 + a*10 + a) == i:
        print(i)
        exit()
