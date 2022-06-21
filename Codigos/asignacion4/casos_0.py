import numpy as np
import matplotlib.pyplot as plt


def X1(x, A1, A2, k1):
    return A1 * np.exp(1j * k1 * x) + A2 * np.exp(-1j * k1 * x)


def X2(x, B1, B2, k2):
    return B1 * np.exp(1j * k2 * x) + B2 * np.exp(-1j * k2 * x)


# Normal

a = 10
L = 2 * a

B1 = 1
B2 = 5

k1 = 1
k2 = 1

A1 = (1 / 2) * (B1 * (1 + k2 / k1) * np.exp(1j * (k2 - k1) * a) + B2 * (1 - k2 / k1) * np.exp(-1j * (k2 + k1) * a))
A2 = (1 / 2) * (B1 * (1 - k2 / k1) * np.exp(1j * (k2 + k1) * a) + B2 * (1 + k2 / k1) * np.exp(-1j * (k2 - k1) * a))

x = np.linspace(0, L, 2000)

y1 = X1(x, A1, A2, k1)
y2 = X2(x, B1, B2, k2)

plt.figure()
plt.plot(x[:250], np.real(y1[:1000]))
plt.plot(x[250:], np.real(y2[1000:]))
plt.xlim([0, L]), plt.ylim([-10, 10])
plt.show()

# Fixed extremes

k1 = 1
k2 = 1

B1 = 1
B2 = - B1 * np.exp(1j * 2 * k2 * L)
# B2 = ((np.exp(1j * k2 * L) - (1 + k2 / k1) * np.exp(1j * (k2 - k1) * a) - (1 - k2 / k1) * np.exp(
#     1j * (k2 + k1) * a)) / ((1 - k2 / k1) * np.exp(-1j * (k2 + k1) * a)) + (1 + k2 / k1) * np.exp(
#     -1j * (k2 - k1) * a) - np.exp(1j * k2 * L)) * B1

# A1 = (1 / 2) * (B1 * (1 + k2 / k1) * np.exp(1j * (k2 - k1) * a) + B2 * (1 - k2 / k1) * np.exp(-1j * (k2 + k1) * a))
# A2 = (1 / 2) * (B1 * (1 - k2 / k1) * np.exp(1j * (k2 + k1) * a) + B2 * (1 + k2 / k1) * np.exp(-1j * (k2 - k1) * a))
# A2 = (1 / 2) * (B1 * (1 - k2 / k1) * np.exp(1j * (k2 + k1) * a) + B2 * (1 + k2 / k1) * np.exp(-1j * (k2 - k1) * a))
A1 = -(1 / 2) * (B1 * (1 - k2 / k1) * np.exp(1j * (k2 + k1) * a) - B1 * (1 + k2 / k1) * np.exp(
    -1j * (k2 * (a - 2 * L) - k1 * a)))
A2 = -(1 / 2) * (- B2 * (1 + k2 / k1) * np.exp(1j * (k2 * (a - 2 * L) - k1 * a)) + B2 * (1 - k2 / k1) * np.exp(
    -1j * (k2 + k1) * a))
# A2 = - A1

y1 = X1(x, A1, A2, k1)
y2 = X2(x, B1, B2, k2)

plt.figure()
plt.plot(x[:1000], np.real(y1[:1000]))
plt.plot(x[1000:], np.real(y2[1000:]))
plt.xlim([0, L]), plt.ylim([-10, 10])
plt.axhline(0)
plt.show()

print('fin')
