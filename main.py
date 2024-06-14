import numpy as np


# theta_0 in gradi
def calc_gittata(theta_0, dt=1e-6):
    theta_0 = theta_0 * np.pi/180
    h_0 = 0.05
    pos = np.array([0, h_0], dtype=np.float64)
    v_0 = 267.5
    vel = np.array([np.cos(theta_0), np.sin(theta_0)], dtype=np.float64)*v_0
    mu = 1.945021436e-5    # sfera perfetta
    g = 9.81
    t = 0
    counter = 0
    m = 0.001

    past_positions = []
    past_velocities = []
    print("Inizio calcolo")

    # finché il corpo non ha toccato terra
    while pos[1] >= 0:
        v_mag = np.linalg.norm(vel)         # modulo dell'accelerazione
        a = -mu*v_mag*vel / m               # calcolo dell'accelerazione con i termini in comune ai due componenti
        a[1] += -g                          # aggiunta accelerazione per gravità

        new_pos = pos + dt*vel              # x_{n+1} = x_n + dt * v_n
        new_vel = vel + dt*a                # v_{n+1} = v_n + dt * a_n
        t += dt

        past_positions.append((t, new_pos))     # per fare grafici
        past_velocities.append((t, new_vel))

        vel = new_vel
        pos = new_pos

        counter += 1
        if counter >= 0.5/dt: # ogni 0.5 secondi nella simulazione simulazione aggiorna sullo stato
            counter = 0
            print(f"t:   {t},   y:   {pos[1]},   vel:   {np.linalg.norm(vel)},   x: {pos[0]}")

    print(f"Fine calcolo: \n {past_positions[-1]}")
    return pos[0]

calc_gittata(45, dt=1e-6)