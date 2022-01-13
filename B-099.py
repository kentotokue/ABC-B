'''
Created on 2021/12/10

@author: kentoo
'''
a,b = map(int,input().split())

S = b - a
ans = [1]
sum = 1
for i in range(1,1001):
    sum += i+1 
    ans.append(sum)
    if sum - ans[i-1] == S:
         break
print(ans[-1] - b)