#pole = '-x------------------'
#pozice = 0
#symbol = 'x'

def tah(pole, pozice, symbol):
    # """Vrátí herní pole s daným symbolem umístěným na danou pozici
    #while True:
        #pozice = int(input('Zadej číslo políčka, čísluje se od nuly: '))
    if pozice in range(0,20):
        #try:
        #pozice = int(pozice)
            #symbol = input('Zadej symbol "x" nebo "o": ')
        #try:
            if "x" == symbol or "o" == symbol:
                if pole[pozice] == '-':
                    zacatek = pole[:pozice]
                    konec = pole[pozice + 1:]
                    pole_se_symbolem = zacatek + symbol + konec
                    return pole_se_symbolem
                else:
                    #print("funkce tah, pozice je obsazena")
                    raise PermissionError
            else:
                #print("funkce tah, neni x ani o")
                raise ValueError
        #except ValueError:
        #    print('chyba')
    else:
        #print("funkce tah, mimo range 0,20")
        raise ValueError
