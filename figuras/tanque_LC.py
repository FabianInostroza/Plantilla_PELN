#!/usr/bin/env python

import numpy as np
from scipy import integrate
from matplotlib import pyplot as plt
import math

L = 10e-6
C = 10e-6
R = 5

# Al agregar fuentes nuevas se debe borrar la cache de matplotlib,
# o sea borrar el archivo fontList.cache de la carpeta ~/.cache/matplotlib
# la carpeta de cache puede ser encontrada con import matplotlib; matplotlib.get_cachedir()
#plt.rc('font',**{'family':'sans-serif','sans-serif':['Minion Pro']})
#plt.rc('font',**{'family':'serif','serif':['Minion Pro']})
plt.rc('font',**{'family':'sans-serif','sans-serif':['URWPalladioL']})
plt.rc('font',**{'family':'serif','serif':['URWPalladioL']})

# LC paralelo
# X[0] = V
# X[1] = I
def fun(X, t):
    return [-X[1]/C, X[0]/L]
    #return [-X[1], X[0]]
    #return [X[1], -2*X[0] - X[1]]

# LCR paralelo
# X[0] = V
# X[1] = I
def fun2(X, t):
    return [-X[0]/(R*C)-X[1]/C, X[0]/L]

#  ----R----
#  |        |
#  C        L
#  |________|
# X[0] = V
# X[1] = I
def fun3(X, t):
    return [-X[1]/C, (X[0]-X[1]*R)/L]

# robertson chemical reaction
def fstiff(X, t):
    return [-0.04*X[0]+10e4*X[1]*X[2], 
            0.04*X[0]-10e4*X[1]*X[2]-3e7*X[1]**2,
            3e7*X[1]**2]

t = np.arange(0, 0.0003, 0.000001)
sol, _ = integrate.odeint(fun2, [1, 0], t, full_output=1)

#t = np.arange(0, 10e6, 10)
#sol, _ = integrate.odeint(fstiff, [1, 0 , 0], t, full_output=1)

freq = math.sqrt(1/(L*C))/(2*math.pi)
T0 = 1/freq

print freq, T0

plt.plot(t, sol)
#ax = plt.gca()
#ax.ticklabel_format(axis='x', style='sci', scilimits=(-2,2))
plt.legend(['V(t)', 'I(t)'])
plt.grid()
plt.savefig('LC.pdf', transparent=True)
plt.show()