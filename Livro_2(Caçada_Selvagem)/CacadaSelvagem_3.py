#O Olho Do Idolo

P = [0, 4, 5, 6, 6, 5]

OS = "      "
BS = "000000"
CS = "******"

for i in range (3):
    for j in range(12):
        V = j
        if i != 3: 
            SS = OS
            GS = CS
        elif i == 3:
            V =  13 - V
        elif i != 2:
            L = 20-2*abs(6-V)
        if V > 6:
            L = L+2
        H = 7 - V
        if V <= 6:
            
    



