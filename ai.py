import util
import random

#pole = '--------------------'
#pozice = '0'
#symbol = 'x'

def tah_pocitace(pole,symbol):
    """Vrátí herní pole se zaznamenaným tahem počítače

    `pole` je herní pole, na které se hraje.
    `symbol` může být 'x' nebo 'o', podle toho jestli hráč hraje za křížky
    nebo za kolečka.
    """
    while True:
        i = random.randrange(0,20)
        if pole[i] != '-':
            #print(i)
            while pole[i] != '-':
                i = random.randrange(0,20)
                #print(i)
        if pole[i] != 'o' or 'x':
            zacatek = pole[:i]
            konec = pole[i + 1:]
            pole_se_symbolem = zacatek + symbol + konec
            return pole_se_symbolem
        else:
            i = random.randrange(0,20)

#print(tah_pocitace('o-------------------', 'x'))
