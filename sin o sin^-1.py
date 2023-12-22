from cmath import pi
import math
from multiprocessing.sharedctypes import Value
import numbers
import string
import time
from timeit import repeat

print('Benvenuto a "Matematica pallosa", sviluppato da Cosimo / Gond')
while True:
    print('Vuoi trovare il sin(x) o il sin^(-1)(x)?')
    inp = input()
    if inp != 'sin(x)' and inp != 'sin' and inp != 'sin^(-1)(x)' and inp != 'sin^(-1)' and inp != 'sin^-1':
        print('Input errato: restart programma...')
        print()
    if inp == 'sin(x)' or inp == 'sin':
        print("Scegliere l'angolo di cui trovare il sin:")
        num = input()
        try:
            float(num)
        except ValueError:
            print('Input errato: restart programma...')
            print()
        else:
            num = float(num)
            sin = math.sin(math.radians(num))
            num = str(num)
            sin = str(sin)
            time.sleep(0.2)
            print('il sin(' + num + '°) è: ' + sin)
            print()
            print()
    if inp == 'sin^(-1)(x)' or inp == 'sin^(-1)' or inp == 'sin^-1':
        print("Scegliere il valore di cui trovare il sin^(-1):")
        num = input()
        try:
            float(num)
        except ValueError:
            print('Input errato: restart programma...')
            print()
        else:
            num = float(num)
            if num < 1:
                asin = math.asin(math.radians(num) * (180/pi)) #per far diventare i radianti in °
                num = str(num)
                asinscritto = str(asin)
                time.sleep(0.2)
                print('Il sin^(-1)(' + num + ') è: ' + asinscritto + ' radianti')
                print('Vuoi il valore in gradi?')
                inp = input()
                if inp == 'Sì' or inp == 'sì' or inp == 'Si' or inp == 'si':
                    asinscritto = float(asinscritto)
                    asin2 = asinscritto*(180/pi)
                    asin2 = str(asin2)
                    asinscritto = str(asinscritto)
                    print('Il valore in gradi di ' + asinscritto + ' radianti è ' + asin2 + '°')
                if inp == inp == 'No' or inp == 'no':
                    print('Restart programma...')
                if inp != 'Sì' and inp != 'sì' and inp != 'Si' and inp != 'si' and inp != 'No' and inp != 'no':
                    print('Input errato: restart programma...')
            else:
                print('Input errato: restart programma...')
        print()
        print()
