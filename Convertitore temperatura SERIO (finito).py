import time

print('Benvenuto al "Converti Temperature", by Cosimo / Gond.')
print('--------------------------------------------')
while True:
    print('Vuoi convertire da gradi Celsius (°C), Fahrenheit (°F) o Kelvin (K)?')
    inizio = input()
    if inizio != "°C" and inizio != "°F" and inizio != "K":
        print('Input errato')
        print()
    else:
        print('Vuoi convertire in gradi Celsius (°C), Fahrenheit (°F) o Kelvin (K)?')
        finale = input()
        if finale != "°C" and finale != "°F" and finale != "K":
            print('Input errato')
            print()
        else:
            try:
                str(inizio)
                str(finale)
            except:
                print('Input errato')
                print()
            else:
#-------------------------------------------------------------------
                if inizio == '°C' and finale == '°F':
                    temperaturaC = input('Inserire temperatura in °C: ')
                    try:
                        float(temperaturaC)
                    except:
                        print('Input errato')
                        print()
                    else:
                        temperaturaC = float(temperaturaC)
                        temperaturaF = (temperaturaC * (9/5)) + 32
                        temperaturaF = str(temperaturaF)
                        temperaturaC = str(temperaturaC)
                        print('Calcolo in corso...')
                        time.sleep(0.4)
                        print(temperaturaC + '°C = ' + temperaturaF + '°F')
                        print()
#---------------------------------------------------------------------
                if inizio == '°F' and finale == '°C':
                    temperaturaF1 = input('Inserire temperatura in °F: ')
                    try:
                        float(temperaturaF1)
                    except:
                        print('Input errato')
                        print()
                    else:
                        temperaturaF1 = float(temperaturaF1)
                        temperaturaC1 = (temperaturaF1 - 32) * (5/9)
                        temperaturaC1 = str(temperaturaC1)
                        temperaturaF1 = str(temperaturaF1)
                        print('Calcolo in corso...')
                        time.sleep(0.4)
                        print(temperaturaF1 + '°F = ' + temperaturaC1 + '°C')
                        print()
#---------------------------------------------------------------------
                if inizio == 'K' and finale == '°C':
                    temperaturaK = input('Inserire temperatura in K: ')
                    try:
                        float(temperaturaK)
                    except:
                        print('Input errato')
                        print()
                    else:
                        temperaturaK = float(temperaturaK)
                        temperaturaC2 = (temperaturaK - 273.15)
                        temperaturaC2 = str(temperaturaC2)
                        temperaturaK = str(temperaturaK)
                        print('Calcolo in corso...')
                        time.sleep(0.4)
                        print(temperaturaK + 'K = ' + temperaturaC2 + '°C')
                        print()
#---------------------------------------------------------------------
                if inizio == '°C' and finale == 'K':
                    temperaturaC3 = input('Inserire temperatura in °C: ')
                    try:
                        float(temperaturaC3)
                    except:
                        print('Input errato')
                        print()
                    else:
                        temperaturaC3 = float(temperaturaC3)
                        temperaturaK1 = (temperaturaC3 + 273.15)
                        temperaturaK1 = str(temperaturaK1)
                        temperaturaC3 = str(temperaturaC3)
                        print('Calcolo in corso...')
                        time.sleep(0.4)
                        print(temperaturaC3 + '°C = ' + temperaturaK1 + 'K')
                        print()
#---------------------------------------------------------------------
                if inizio == '°F' and finale == 'K':
                    temperaturaF2 = input('Inserire temperatura in °F: ')
                    try:
                        float(temperaturaF2)
                    except:
                        print('Input errato')
                        print()
                    else:
                        temperaturaF2 = float(temperaturaF2)
                        temperaturaK2 = ((temperaturaF2 - 32) * (5/9) + 273.15)
                        temperaturaK2 = str(temperaturaK2)
                        temperaturaF2 = str(temperaturaF2)
                        print('Calcolo in corso...')
                        time.sleep(0.4)
                        print(temperaturaF2 + '°F = ' + temperaturaK2 + 'K')
                        print()
#---------------------------------------------------------------------
                if inizio == 'K' and finale == '°F':
                    temperaturaK3 = input('Inserire temperatura in K: ')
                    try:
                        float(temperaturaK3)
                    except:
                        print('Input errato')
                        print()
                    else:
                        temperaturaK3 = float(temperaturaK3)
                        temperaturaF3 = ((temperaturaK3 - 273.15) * (9/5) + 32)
                        temperaturaF3 = str(temperaturaF3)
                        temperaturaK3 = str(temperaturaK3)
                        print('Calcolo in corso...')
                        time.sleep(0.4)
                        print(temperaturaK3 + 'K = ' + temperaturaF3 + '°F')
                        print()