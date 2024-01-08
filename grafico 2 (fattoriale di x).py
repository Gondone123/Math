from matplotlib import pyplot as grafico
from scipy.special import factorial
import numpy 
import math

x = numpy.arange(-5, 5.001, 0.001)
y = factorial(x)
z = factorial(numpy.negative(x))
grafico.plot(x, y, color="orange")
grafico.plot(x, z, color='orange')
#COSTRUIAMO "ASSI DI SIMMETRIA" (no frecce)
grafico.axhline(y=0, color='grey', linestyle='solid')
grafico.axvline(x=0, color='grey', linestyle='solid')
grafico.title("Grafico di x!, costruito anche con -x")
grafico.xlabel("X")
grafico.ylabel("Y")
grafico.show()