import numpy as np


# theta_0 in gradi, mass in kg, w in rpm
def calc_gittata(theta_0, mass, w = 3400, dt=1e-6):
    M_lama = 0.5
    r = 0.377
    w *= 2*np.pi/60     # converti
    v_lama = w*r

    theta_0 = theta_0 * np.pi/180
    h_0 = 0.05
    pos = np.array([0, h_0], dtype=np.float64)
    v_0 = 2*M_lama/(M_lama+mass) * v_lama
    vel = np.array([np.cos(theta_0), np.sin(theta_0)], dtype=np.float64)*v_0
    
    R_sasso = (3*mass / (4*np.pi*2400))**(1/3)          # calcolo del raggio per una sfera perfetta assumendo densità 2400 Kg/m^3
    S = np.pi*((R_sasso)**2)                            # area trasversale
    mu = 1.225*S*0.59/2    # sfera perfetta
    
    
    g = 9.81
    t = 0
    counter = 0
    m = 0.001

    past_positions = []
    past_velocities = []
    print("Inizio calcolo")

    # finché il corpo non ha toccato terra
    while pos[1] > R_sasso:
        v_mag = np.linalg.norm(vel)         # modulo dell'accelerazione
        a = -mu*v_mag*vel / m               # calcolo dell'accelerazione con i termini in comune ai due componenti
        a[1] += -g                          # aggiunta accelerazione per gravità

        new_pos = pos + dt*vel              # x_{n+1} = x_n + dt * v_n
        new_vel = vel + dt*a                # v_{n+1} = v_n + dt * a_n
        t += dt

        #past_positions.append((t, new_pos))     # per fare grafici
        #past_velocities.append((t, new_vel))

        vel = new_vel
        pos = new_pos

        counter += 1
        if counter >= 0.5/dt: # ogni 0.5 secondi nella simulazione simulazione aggiorna sullo stato
            counter = 0
            print(f"t:   {t},   y:   {pos[1]},   vel:   {np.linalg.norm(vel)},   x: {pos[0]}")

    return pos[0]

n = 5
vals = []
degs = np.linspace(31/n, 31, n)
for deg in degs:
    x_max = calc_gittata(deg, 0.01, dt=1e-6)
    vals.append(x_max)

import matplotlib.pyplot as plt
plt.xlabel('Angolo di proiezione (gradi)')
plt.ylabel('Gittata massima (m)')
plt.plot(degs, vals)
plt.show()
