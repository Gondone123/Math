from matplotlib import pyplot as grafico
import numpy 
import math

x = numpy.arange(-10, 10.001, 0.001)
y = numpy.divide(1, numpy.sqrt(x))
y2 = -y #INVERTIAMO: ora abbiamo i valori y negativi
x2 = -x #INVERTIAMO: ora abbiamo i valori x negativi
grafico.plot(x, y, color='orange')
grafico.plot(x2, y2, color="orange") #sarà opposto rispetto all'origine rispetto al grafico precedente
grafico.axhline(y=0, color='grey', linestyle='solid')
grafico.axvline(x=0, color='grey', linestyle='solid')
grafico.xlabel("X")
grafico.ylabel("Y")
grafico.title("Grafico di y=1/√x, simmetrico rispetto all'origine")
grafico.show()