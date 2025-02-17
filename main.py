import numpy as np
import matplotlib.pyplot as plt

a = 0.1382
b = 3.19*10**(-5)
R = 8.314

V = np.linspace(b + 10**(-5), 10**(-3), 1000)

t = [-140, -130, -120, -110, -100]

Tk = (8 * a) / (27 * R * b)

def vv(V, T, a, b, R):
    return R * T / (V - b) - a / V ** 2

plt.figure(figsize=(10, 6))

for t_cel in t:
    T = t_cel + 273.15
    P = vv(V, T, a, b, R)

    if T >= Tk:
        plt.plot(V, P, label={t_cel}, color='red')
    else:
        plt.plot(V, P, label={t_cel})


plt.legend()
plt.grid(True)
plt.show()

