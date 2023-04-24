import ai
import util

#import tah_hrace
#import tah_pocitace
#import vyhodnot


def vyhodnot(pole):
    # Vyhrál hráč s křížky
    if "xxx" in pole:
        print('vyhrál hráč s křížky')
        return "x"
    # Vyhrál hráč s kolečky
    if "ooo" in pole:
        print('vyhrál hráč s kolečky')
        return "o"
    if "-" not in pole:
        print('remíza')
        return "!"
    else:
        print('hra ještě neskončila')
        return '-'


#import tah_s_ValueError
#symbol = 'x'
#pole = 'o-------------------'
def tah_hrace(pole, symbol):
    #"""Zeptá se hráče na tah a vrátí nové herní pole
    #`pole` je herní pole, na které se hraje.
    #`symbol` může být 'x' nebo 'o', podle toho jestli hráč hraje za křížky
    #nebo za kolečka.
    #"""
    while True:
        try:
            pozice = int(input('Kam chceš hrát? '))
            while pozice in range(0,20):
                pole_s_tahem_hrace = util.tah(pole,pozice,symbol)
                #pole_s_tahem_hrace = pole[:pozice] + symbol + pole[pozice + 1:]
                #if pole[pozice] != '-':
                #    print('Tam nejde hrát')
                #print("Nový stav hry je:", pole_s_tahem_hrace)
                return pole_s_tahem_hrace
                #break
            if pozice not in range(0,20):
                print('Tam nejde hrát')
            if type(pozice) is int():
                print('Zadávej čísla')
        except ValueError:
            #print("funkce tah_hrace, kam chceš hrát")
            print('Zadávej čísla')
        except PermissionError:
            print('Tam nejde hrát')


#print(tah_hrace(pole,symbol))

#import tah_hrace
#import tah_pocitace
#import vyhodnot

def piskvorky1d():
    pole = '--------------------'
    while '-' in pole:
        hernipole = tah_hrace(pole,'x')
        #print(hernipole)
        hernipole2 = ai.tah_pocitace(hernipole,'o')
        print(hernipole2)
        hodnoceni = vyhodnot(hernipole2)
        pole = hernipole2
        if hodnoceni == 'x':
            print("Gratuluji, hráči s křížky!")
            break
        if hodnoceni == 'o':
            print("Gratuluji, hráči s kolečky!")
            break
        if hodnoceni == '!':
            print("Díky za hru")
        #return pole

#print(piskvorky1d())
