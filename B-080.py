'''
Created on 2022/01/13

@author: kentoo
'''
N = str(input())
sum = 0
for i in range(len(N)):
    sum += int(N[i])
if int(N) % sum == 0:
    print("Yes")
else:
    print("No")