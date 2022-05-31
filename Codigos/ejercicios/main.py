import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt


# DE function

def Ecuacdif(y, x):
    dydx = -(200 * y ** 2 + y + x + 1)
    return dydx


# initial condition
y0 = 3

# x points
x = np.linspace(0, 0.2, 100)

# solve DE
y = odeint(Ecuacdif, y0, x)

# plot results
plt.axhline(y=0, color='k', linestyle=':')
plt.axvline(x=0, color='k', linestyle=':')
plt.plot(x, y)
plt.xlabel('x')
plt.ylabel('y(t)')
plt.show()

print('Fin')
