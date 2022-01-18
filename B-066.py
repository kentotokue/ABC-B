'''
Created on 2022/01/18

@author: kentoo
'''
S = str(input())



for i in range(len(S)):
    
    S = S[:len(S)-1]
    #print(S)
    L = len(S)//2
    #print(S[:L],S[L:])
    if S[:L] == S[L:]:
        print(len(S))
        exit()
    else:
        continue
