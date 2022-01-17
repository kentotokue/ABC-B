'''
Created on 2022/01/17

@author: kentoo
'''


N = int(input())

for i in range(10):
    if (2**i) > N:
        print(2**(i-1))
        exit()
        