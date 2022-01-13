'''
Created on 2021/11/26

@author: kentoo
'''

S = input()

M = 100100100
for i in range(len(S)-2):
    F = (int(S[i])*100)+int(S[i+1])*10+int(S[i+2])
    #print(F)
    M = min (M,abs(F-753))    
print(M)