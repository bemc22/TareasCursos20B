import numpy as np
import matplotlib.pyplot as plt


def X1(x, A1, k1):
    return 2 * 1j * A1 * np.sin(k1 * x)


def X2(x, a, L, B2, k1, k2):
    return - 2 * 1j * B2 * np.exp(1j * 2 * k2 * (L - 2 * a)) * np.sin(k2 * (x - L)) * (
                (1 + k2 / k1) + (1 - k2 / k1) * np.exp(-1j * 2 * k1 * a)) / (
                       (1 - k2 / k1) + (1 + k2 / k1) * np.exp(-1j * 2 * k1 * a))


# Normal

a = 5
L = 2 * a

A1 = 1
B2 = 1

k1 = 1
k2 = 1

x = np.linspace(0, L, 2000)

y1 = X1(x, A1, k1)
y2 = X2(x, a, L, B2, k1, k2)

plt.figure()
plt.plot(x[:1000], np.real(y1[:1000]))
plt.plot(x[1000:], np.real(y2[1000:]))
plt.xlim([0, L]), plt.ylim([-10, 10])
plt.show()

print('fin')
