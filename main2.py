import numpy as np
import matplotlib.pyplot as plt

a = 0.1382
b = 3.19 * 10**(-5)
R = 8.314

V = np.linspace(b + 10**(-5), 10**(-3), 1000)

t = [-130]

Tk = (8 * a) / (27 * R * b)

def vv(V, T, a, b, R):
    return R * T / (V - b) - a / V**2


P_specific = vv(V, 143.15, a, b, R)


dP_dV = np.diff(P_specific) / np.diff(V)


extrema_indices = np.where(np.diff(np.sign(dP_dV)) != 0)[0]


V_extrema = V[extrema_indices + 1]

d2P_dV2 = np.diff(dP_dV) / np.diff(V[1:])
if d2P_dV2[0] < 0:
  V_max = V_extrema[0]
  V_min = V_extrema[1]

else:
  V_max = V_extrema[1]
  V_min = V_extrema[0]

P_max = vv(V_max, 143.15, a, b, R)
P_min = vv(V_min, 143.15, a, b, R)



plt.figure(figsize=(10, 6))
plt.plot(V, P_specific, label='-130°C')
plt.plot(V_max, P_max, 'go')
plt.plot(V_min, P_min, 'ro')
plt.grid(True)
plt.show()