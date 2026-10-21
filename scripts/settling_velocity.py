# Import the required modules
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path
import numpy as np
# Import velocity data
velocity_path = Path("../DEM/post/velocity.txt")
velocity = pd.read_csv(velocity_path, sep = r'\s+', names = ["time", "Vx", "Vy", "Vz"], skiprows = 1)
print(velocity)
velocity_terminal = velocity.iloc[-1]["Vy"]
print(f"The terminal velocity as per CFD-DEM {velocity_terminal} m/s")

# Plot vertical velocity
plt.figure("Settling velocity")
plt.plot(velocity["time"],velocity["Vy"],label= "Vertical velocity")
plt.xlabel("Time (s)")
plt.ylabel("Settling velocity (m/s)")
plt.legend()

plt.savefig("Settling velocity")

# Particle and fluid properties
rho_p = 3000 
rho_f = 10
dp = 0.0001
g = 9.81
nu = 1e-5
mu = rho_f * nu
v_Stokes = -(rho_p - rho_f)*g*dp**2/18/mu
print(f"The terminal velocity assuming Stokes regime is {v_Stokes} m/s")

# Reynolds number
Re_p = abs(velocity_terminal) * dp /nu
print(f"The Reynolds number is {Re_p}") 

# Function to calculate the Reynold's number
def Reynolds(vt,dp,nu):
    Re = vt*dp/nu
    return Re

# Looping through the velocity dataframe
for idx, row in velocity.iterrows():

    Vy = row["Vy"]

    # Reynolds number (use velocity magnitude)
    Re = Reynolds(abs(Vy), dp, nu)

    if Re == 0:
        continue

    # Drag coefficient: Schiller-Naumann correlation
    if Re < 1000:
        C_D = 24/Re * (1 + 0.15*Re**0.687)
    else:
        C_D = 0.44

    # Drag force
    F_d = 0.5*rho_f*C_D*(np.pi*dp**2/4)*Vy**2

    # Effective gravitational force (weight - buoyancy)
    F_g = (rho_p - rho_f)*(np.pi*dp**3/6)*9.81

    # Check force equilibrium within 1%
    if np.isclose(F_d, F_g, rtol=0.01, atol=0):
        print("Terminal velocity is", Vy, "m/s")
        print("Time =", row["time"], "s")
        break
