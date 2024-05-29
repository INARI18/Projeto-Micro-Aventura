#O Olho Do Idolo

import curses
from time import sleep

stdscr = curses.initscr()

PUPILA = [0, 4, 5, 6, 6, 5]

ESPACOS = "      "
PUPILA_CHEIA = "000000"
CONTORNO = "******"

for i in range (3):
    for j in range(12):
        COLUNA = j+1

        if i == 2:
            COLUNA = 13 - COLUNA
         
        LINHA_ATUAL = ESPACOS
        CONTORNO_ATUAL = CONTORNO
        
        if i == 1:
            LINHA_ATUAL = PUPILA_CHEIA
            CONTORNO_ATUAL = PUPILA_CHEIA

        COMPRIMENTO_LINHA = 20-2*abs(6-COLUNA)

        if COLUNA > 6:
            COMPRIMENTO_LINHA += 2

        ESPACO_HORIZONTAL = 7 - COLUNA

        if COLUNA <= 6:
            ESPACO_HORIZONTAL = COLUNA - 6

        stdscr.addstr(ESPACO_HORIZONTAL, COLUNA, CONTORNO_ATUAL)
        print("**")
        NUM_PUPILA = PUPILA[6-ESPACO_HORIZONTAL] #7 - ....
        TAM_ESPACO = COMPRIMENTO_LINHA - 2*NUM_PUPILA - 4

        if NUM_PUPILA == 0:
            if TAM_ESPACO <= 0:
                print(LINHA_ATUAL[0:NUM_PUPILA])
                print("**")
    sleep(2)                
    stdscr.move(0, 22)
