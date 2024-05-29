#O OLHO DO IDOLO

import curses
from time import sleep

PUPILA = "0000000000"
CONTORNO_OLHO = "******"
DESENHO_ATUAL = ""

stdscr = curses.initscr()

for i in range (3):
    for j in range (10):

        if i == 0:
            stdscr.addstr(0, 4, CONTORNO_OLHO)
            DESENHO_ATUAL = CONTORNO_OLHO[0:2] + PUPILA[0:6] + CONTORNO_OLHO[0:2]
            stdscr.addstr(1, 2, DESENHO_ATUAL)

            linha = 2
            DESENHO_ATUAL = CONTORNO_OLHO[0:2] + PUPILA + CONTORNO_OLHO[0:2]
            while linha != 5:
                stdscr.addstr(linha,0,DESENHO_ATUAL)
                linha+=1

            DESENHO_ATUAL = CONTORNO_OLHO[0:2] + PUPILA[0:6] + CONTORNO_OLHO[0:2]
            stdscr.addstr(6, 2, DESENHO_ATUAL)
            stdscr.addstr(5, 4, CONTORNO_OLHO)

        if i == 1:
            stdscr.addstr(8, 1, CONTORNO_OLHO*2) # 12 (*)
            stdscr.addstr(9, 0, CONTORNO_OLHO*2 + "*"*2) # 14 (*)
            stdscr.addstr(10, 0, CONTORNO_OLHO*2 + "*"*2) # 14 (*)
            stdscr.addstr(11, 1, CONTORNO_OLHO*2) # 12 (*)
            stdscr.addstr(12, 2, CONTORNO_OLHO + "*"*4) # 10 (*)
            #stdscr.addstr(13, 6, CONTORNO_OLHO + "*"*2)
            stdscr.addstr(13, 3, CONTORNO_OLHO[0:4]) # 6 (*)
        
        if i == 2:
            stdscr.addstr(13, 4, CONTORNO_OLHO)
            DESENHO_ATUAL = CONTORNO_OLHO[0:2] + PUPILA[0:6] + CONTORNO_OLHO[0:2]
            stdscr.addstr(1, 2, DESENHO_ATUAL)

            linha = 15
            DESENHO_ATUAL = CONTORNO_OLHO[0:2] + PUPILA + CONTORNO_OLHO[0:2]
            while linha != 18:
                stdscr.addstr(linha,0,DESENHO_ATUAL)
                linha+=1

            DESENHO_ATUAL = CONTORNO_OLHO[0:2] + PUPILA[0:6] + CONTORNO_OLHO[0:2]
            stdscr.addstr(19, 2, DESENHO_ATUAL)
            stdscr.addstr(18, 4, CONTORNO_OLHO)

        stdscr.refresh()
        sleep(2)
        stdscr.clear() 
        stdscr.refresh()

curses.endwin()

"""
    ******
  **000000**
**000000000**
**000000000**
**000000000**
  **000000**
    ******

 ************
**************
**************
 ************
  ********** 
    ******

    ******
  **000000**
**000000000**
**000000000**
**000000000**
  **000000**
    ******

"""
