# Import the required modules
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

# Input file
velocity_file = Path("../DEM/post/velocity.txt")
data = np.loadtxt(velocity_file, comments="#")

time = data[:, 0]
vy = data[:, 2] 

# Hand calculation results
vt_stokes = -0.1630
vt_sn = -0.13734
vy_final = vy[-1]

# Relative differences
diff_stokes = 100 * abs(vy_final - vt_stokes) / abs(vt_stokes)
diff_sn = 100 * abs(vy_final - vt_sn) / abs(vt_sn)
print(f"Final simulated settling velocity: {vy_final:.5f} m/s")
print(f"Stokes terminal velocity:          {vt_stokes:.5f} m/s")
print(f"Schiller-Naumann terminal velocity:{vt_sn:.5f} m/s")
print(f"Difference vs Stokes:              {diff_stokes:.2f}%")
print(f"Difference vs Schiller-Naumann:    {diff_sn:.2f}%")

plt.figure(figsize=(8, 5))
plt.plot(time, vy, linewidth=2, label="CFD-DEM simulation")
plt.axhline(vt_stokes, linestyle="-", linewidth=2, label="Stokes terminal velocity")
plt.axhline(vt_sn, linestyle="--", linewidth=2, label="Schiller-Naumann terminal velocity")

plt.xlabel("Time [s]")
plt.ylabel("Vertical particle velocity $v_y$ [m/s]")
plt.title("Settling particle velocity: CFD-DEM vs analytical references")
plt.grid(True)
plt.legend()
plt.tight_layout() 
plt.savefig("Evaluation of drag models")
