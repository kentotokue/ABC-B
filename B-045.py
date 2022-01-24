'''
Created on 2022/01/24

@author: kentoo
'''
SA = input()
SB = input()
SC = input()




now = SA[0]

SA = SA[1:]
for i in range(1000):

    if now == "a":
        if len(SA) == 0:
            print("A")
            exit()
        now = SA[0]
        SA = SA[1:]
        
        
    elif now == "b":
        if len(SB) == 0:
            print("B")
            exit()
        now = SB[0]
        SB = SB[1:]

    elif now == "c":
        if len(SC) == 0:
            print("C")
            exit()
        now = SC[0]
        SC = SC[1:]

        
        