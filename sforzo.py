import numpy as np

def calc_sigma(massa=0.001):
    M_lama = 0.5
    R_sasso = (3*massa / (4*np.pi*2400))**(1/3)          # calcolo del raggio per una sfera perfetta assumendo densità 2400 Kg/m^3
    v_lama = 134
    v_sasso = v_lama * 2*M_lama / (M_lama+massa)

    dt = 2*R_sasso/v_lama
    Js = massa*v_sasso
    F_m = Js/dt
    S_max = np.pi*((R_sasso)**2)

    sigma = F_m/S_max
    return sigma


masses = np.linspace(0.001, 0.1, 50)
sforzi = []
for val in masses:
    sforzo = calc_sigma(val)
    sforzi.append(sforzo*1e-6)

import matplotlib.pyplot as plt
plt.xlabel('massa (Kg)')
plt.ylabel('sforzo (MPa)')
plt.plot(masses, sforzi)
plt.show()