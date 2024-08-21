from time import sleep

def Aberto():

    print(". . @ @ @ @ . . ")
    print(". @ . . . . @ . ")
    print("@ . . 0 0 . . @ ")
    print("@ . 0 O O 0 . @ ")
    print("@ . 0 O O 0 . @ ")
    print("@ . . 0 0 . . @ ")
    print(". @ . . . . @ . ")
    print(". . @ @ @ @ . . ")

"""
def Fechado1():

    print(". . . . . . . . ")
    print(". @ @ @ @ @ @ . ")
    print("@ @ . . . . @ @ ")
    print("@ . . 0 0 . . @ ")
    print("@ . 0 O O 0 . @ ")
    print("@ . 0 O O 0 . @ ")
    print(". @ . 0 0 . @ . ")
    print(". . @ @ @ @ . . ")
"""
def Entreaberto():

    print(". . . . . . . . ")
    print(". . . . . . . . ")
    print(". . . . . . . . ")
    print(". @ @ @ @ @ @ . ")
    print("@ . 0 O O 0 . @ ")
    print("@ . 0 O O 0 . @ ")
    print(". @ . 0 0 . @ . ")
    print(". . @ @ @ @ . . ")

def Fechado():

    print(". . . . . . . . ")
    print(". . . . . . . . ")
    print(". . . . . . . . ")
    print(". . @ @ @ @ . . ")
    print("@ @ @ @ @ @ @ @ ")
    print("@ @ @ @ @ @ @ @ ")
    print(". @ @ @ @ @ @ . ")
    print(". . @ @ @ @ . . ")

while 1:

    print("\n" * 60)
    Aberto()
    sleep(1)
    """
    print("\n" * 60)
    Fechado1()
    sleep(0.05)
    """
    print("\n" * 60)
    Entreaberto()
    sleep(0.05)

    print("\n" * 60)
    Fechado()
    sleep(0.2)

    print("\n" * 60)
    Entreaberto()
    sleep(0.05)
    """
    print("\n" * 60)
    Fechado1()
    sleep(0.05)
    """