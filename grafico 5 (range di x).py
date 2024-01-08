from matplotlib import pyplot as grafico
import numpy 
import math

x = numpy.arange(-10, 10.001, 0.001)
y = numpy.square(x[x<0])
z = numpy.sqrt(x[x>=0])
#x[x/simbolo/numero]: fa sì che si operi per x nel range contenuto in []
grafico.plot(x[x<0], y, color="orange")
grafico.plot(x[x>=0], z, color='orange')
grafico.axhline(y=0, color='grey', linestyle='solid')
grafico.axvline(x=0, color='grey', linestyle='solid')
grafico.title("Operare con due range di x: y=x^2 con x<0, y=√x con x≥0")
grafico.xlabel("X")
grafico.ylabel("Y")
grafico.show()
