'''
Created on 2022/01/24

@author: kentoo
'''


N,K = map(int,input().split())

print(K*((K-1)**(N-1)))