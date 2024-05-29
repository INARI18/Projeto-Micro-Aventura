import curses
from time import sleep

PUPILA = "0000000000"
CONTORNO_OLHO = "******"
DESENHO_ATUAL = ""

stdscr = curses.initscr()
curses.curs_set(0)

for i in range (3):
    stdscr.clear()
    stdscr.refresh()
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
            stdscr.addstr(5, 2, DESENHO_ATUAL)
            stdscr.addstr(6, 4, CONTORNO_OLHO)

        if i == 1:
            stdscr.addstr(0, 1, CONTORNO_OLHO*2) # 12 (*)
            stdscr.addstr(1, 0, CONTORNO_OLHO*2 + "*"*2) # 14 (*)
            stdscr.addstr(2, 0, CONTORNO_OLHO*2 + "*"*2) # 14 (*)
            stdscr.addstr(3, 1, CONTORNO_OLHO*2) # 12 (*)
            stdscr.addstr(4, 2, CONTORNO_OLHO + "*"*4) # 10 (*)
            stdscr.addstr(5, 4, CONTORNO_OLHO) # 6 (*)
        
        if i == 2:
            stdscr.addstr(0, 4, CONTORNO_OLHO)
            DESENHO_ATUAL = CONTORNO_OLHO[0:2] + PUPILA[0:6] + CONTORNO_OLHO[0:2]
            stdscr.addstr(1, 2, DESENHO_ATUAL)

            linha = 2
            DESENHO_ATUAL = CONTORNO_OLHO[0:2] + PUPILA + CONTORNO_OLHO[0:2]
            while linha != 5:

                stdscr.addstr(linha,0,DESENHO_ATUAL)
                linha+=1

            DESENHO_ATUAL = CONTORNO_OLHO[0:2] + PUPILA[0:6] + CONTORNO_OLHO[0:2]
            stdscr.addstr(5, 2, DESENHO_ATUAL)
            stdscr.addstr(6, 4, CONTORNO_OLHO)

        stdscr.refresh()
        sleep(5)

curses.endwin()
