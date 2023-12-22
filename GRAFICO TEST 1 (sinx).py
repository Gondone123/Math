from matplotlib import pyplot as grafico
from scipy.interpolate import interp1d
import numpy 
import math

#VALORI PICCOLI = CURVA PIU' VISIBILE
x = numpy.arange(0, 20, 0.1)
y = numpy.sin(x)
z = numpy.cos(x)
grafico.plot(x, y, color="orange")
grafico.plot(x, z, color="red")
grafico.axhline(y=0, color='black', linestyle='dashdot')
grafico.title("Grafico di sin(x), arancione, e cos(x), rosso, con y=0 per delimitare i valori positivi e negativi")
grafico.xlabel("X")
grafico.ylabel("Y")
grafico.show()

#RIGUARDO ARRANGE: prendo un valore di inizio (in questo caso, 0) e di fine (in questo caso, 20); 0.1
#indicherebbe che lo facciamo ogni 0.1 valore, dando quindi l'illusione di una curva. 
