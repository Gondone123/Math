import time
import numbers
from numpy import random
 
print('Benvenuto nella Calcolatrice! By Cosimo / Gond')
while True:
    print("Scegli l'operazione: Addizione, sottrazione, moltiplicazione, potenza o divisione?")
    operazione = input()
 
    if operazione != 'Addizione' and operazione != 'Addizione' and operazione != 'addizione' and operazione != 'Sottrazione' and operazione != 'sottrazione' and operazione != 'Moltiplicazione' and operazione != 'moltiplicazione' and operazione != 'Divisione' and operazione != 'divisione' and operazione != 'Potenza' and operazione != 'potenza':
        print('Non valido! Restart della calcolatrice in corso...')
        print('--------------------------------------------------')
 
    if operazione == 'Addizione' or operazione == 'addizione':
        print('Scegli il primo addendo: ')
        num = input()
        if num.isdigit() is True:
            print('Scegli il secondo addendo: ')
            num2 = input()
            if num2.isdigit() is True:
                num = int(num)  
                num2 = int(num2)  
                num3 = num + num2
                num = str(num)  
                num2 = str(num2)
                num3 = str(num3)
                print('Calcolo in corso, attendere...')
                time.sleep(random.randint(2,5))
                print('La somma è: ' + num + ' + ' + num2 + ' = ' + num3)
                print('--------------------------------------------------')
    if operazione == 'Sottrazione' or operazione == 'sottrazione':
        print('Scegli il minuendo: ')
        num = input()
        if num.isdigit() is True:
            print('Scegli il sottraendo: ')
            num2 = input()
            if num2.isdigit() is True:
                num = int(num)
                num2 = int(num2)
                num3 = num - num2
                num = str(num)
                num2 = str(num2)
                num3 = str(num3)
                print('Calcolo in corso, attendere...')
                time.sleep(random.randint(2,5))
                print('La differenza è: ' + num + ' - ' + num2 + ' = ' + num3)
                print('--------------------------------------------------')
    if operazione == 'Moltiplicazione' or operazione == 'moltiplicazione':
        print('Scegli il moltiplicando: ')
        num = input()
        if num.isdigit() is True:
            print('Scegli il moltiplicatore: ')
            num2 = input()
            if num2.isdigit() is True:
                num = int(num)
                num2 = int(num2)
                num3 = num * num2
                num = str(num)
                num2 = str(num2)
                num3 = str(num3)
                print('Calcolo in corso, attendere...')
                time.sleep(random.randint(2,5))
                print('Il prodotto è: ' + num + ' x ' + num2 + ' = ' + num3)
                print('--------------------------------------------------')
    if operazione == 'Divisione' or operazione == 'divisione':
        print('Scegli il dividendo: ')
        num = input()
        if num.isdigit() is True:
            print('Scegli il divisore: ')
            num2 = input()
            if num2.isdigit() is True:
                num = int(num)
                num2 = int(num2)
                num3 = num / num2
                num = str(num)
                num2 = str(num2)
                num3 = str(num3)
                print('Calcolo in corso, attendere...')
                time.sleep(random.randint(2,5))
                print('Il quoziente è: ' + num + ' : ' + num2 + ' = ' + num3)
                print('--------------------------------------------------')
    if operazione == 'Potenza' or operazione == 'potenza':
        print('Scegli la base: ')
        num = input()
        if num.isdigit() is True:
            print("Scegli l'esponente: ")
            num2 = input()
            if num2.isdigit() is True:
                num = int(num)
                num2 = int(num2)
                num3 = num ** num2
                num = str(num)
                num2 = str(num2)
                num3 = str(num3)
                print('Calcolo in corso, attendere...')
                time.sleep(random.randint(2,5))
                print('La potenza è: ' + num + '^' + num2 + ' = ' + num3)
                print('--------------------------------------------------')

            if num.isdigit() is False or num2.isdigit() is False:
                print('Non valido! Restart della calcolatrice in corso...') 
                print('--------------------------------------------------')