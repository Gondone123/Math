from matplotlib import pyplot as grafico
import numpy 
import math

x = numpy.linspace(-10, 10, 500)
y = numpy.divide(numpy.cos(x), numpy.sin(x))
grafico.plot(x, y, color="orange")
grafico.axhline(y=0, color='grey', linestyle='solid')
grafico.axvline(x=0, color='grey', linestyle='solid')
grafico.xlabel("X")
grafico.ylabel("Y")
grafico.title("Grafico di 1/sin(x)")
grafico.show()