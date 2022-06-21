import numpy as np
import matplotlib.pyplot as plt


def X1(x, A1, A2, k1):
    return A1 * np.cos(k1 * x) + A2 * np.sin(k1 * x)


def X2(x, B1, B2, k1):
    return B1 * np.cos(k1 * x) + B2 * np.sin(k1 * x)


# Normal

L = 5

B1 = 4
B2 = 1.5

k1 = 3
k2 = 2

A1 = B1
A2 = k2 / k1

x = np.linspace(-L, L, 2000)

y1 = X1(x, A1, A2, k1)
y2 = X2(x, B1, B2, k2)

plt.figure()
plt.plot(x[:1000], np.real(y1[:1000]))
plt.plot(x[1000:], np.real(y2[1000:]))
plt.xlim([-L, L]), plt.ylim([-10, 10])
plt.show()

# Fixed extremes

L = 5

# B1 = 3
# B2 = -B1 / np.tan(k2 * L)

k1 = 1
k2 = 2

B1 = 1250 / 709
B2 = 5000 / 9589
A2 = 11250 / 709
A1 = 5000 / 9589

# A1 = -A2 * np.tan(-k1 * L)  # B1
# A2 = k2 / k1

# A1 = (k2 / k1) * (np.tan(- k1 * L) / np.tan(k2 * L)) * B1
# A2 = (np.tan(k2 * L) / np.tan(- k1 * L)) * B2

x = np.linspace(-L, L, 2000)

y1 = X1(x, A1, A2, k1)
y2 = X2(x, B1, B2, k2)

plt.figure()
plt.plot(x[:1000], np.real(y1[:1000]))
plt.plot(x[1000:], np.real(y2[1000:]))
# plt.xlim([-L, L]), plt.ylim([-10, 10])
plt.show()

print('fin')
