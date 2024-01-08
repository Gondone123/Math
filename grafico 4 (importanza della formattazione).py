from matplotlib import pyplot as grafico
from scipy.special import factorial
import numpy 
import math

x = numpy.arange(-10, 10.001, 0.001)
y = numpy.square(x/factorial(x))
z = numpy.square(x/factorial(numpy.negative(x)))
y2 = numpy.square(x)/factorial(x)
z2 = numpy.square(x)/factorial(numpy.negative(x))
grafico.plot(x, y, color="orange")
grafico.plot(x, z, color='orange')
grafico.plot(x, y2, color = 'green')
grafico.plot(x, z2, color = 'green')
#COSTRUIAMO "ASSI DI SIMMETRIA" (no frecce)
grafico.axhline(y=0, color='grey', linestyle='solid')
grafico.axvline(x=0, color='grey', linestyle='solid')
grafico.title("L'importanza della formattazione: (x/x!)^2, arancione, e x^2/x!, verde; sia con +x che con -x")
grafico.xlabel("X")
grafico.ylabel("Y")
grafico.show()