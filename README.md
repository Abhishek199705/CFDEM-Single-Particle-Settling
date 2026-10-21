# Single-Particle Settling Simulation

## Overview

Investigation of the settling behavior of a spherical particle in a stationary fluid using CFD-DEM coupling.

The simulation is based on the `settlingTestMPI` tutorial from CFDEMcoupling. The objective was to understand how a 
particle accelerates and approaches its terminal velocity.

## Software and Numerical Methods

- **OpenFOAM 6:**Fluid-phase simulation
- **LIGGGHTS-PUBLIC 3.8.0:** Particle dynamics
- **CFDEMcoupling 3.8.1:** Two-way fluidâ€“particle coupling
- **Python:** Data analysis and visualization
- **Docker:** Linux simulation environment

**CFD solver:** `cfdemSolverPiso`  
**DEM:** LIGGGHTS  
**Drag model:** Di Felice

## Simulation Setup

### Particle Properties

| Parameter | Value |
|---|---|
| Number of particles | 1 |
| Particle diameter | 0.0001 m |
| Particle density | 3000 kg/m³ |
| Initial particle position | (0.05, 0.025, 0.05) m |
| Initial particle velocity | 0 m/s |

### Fluid Properties

| Parameter | Value |
|---|---|
| Fluid density | 10 kg/m³ |
| Kinematic viscosity | 0.00001 m²/s |
| Initial fluid velocity | (0, 0, 0) m/s |
| Flow model | Laminar |

Gravity acts in the negative y-direction at 9.81 m/s².

### Computational Domain

| Parameter | Value |
|---|---|
| Domain dimensions | 0.01 0.05 0.01 m |
| Mesh resolution | (4 20 4) |
| Total CFD cells | 320 |
| MPI processes | 2 |
| Simulation duration | 0.15 s |
| DEM timestep | 0.00001 s |

## Results and Discussion

The simulated vertical velocity approaches approximately **0.129 m/s**.

The velocity curve becomes nearly constant after approximately 0.06 s.

### Terminal-Velocity Comparison

Two analytical drag models are considered:

**Stokes' Law**

$$
v_t=-\frac{(\rho_p-\rho_f)gd_p^2}{18\mu}
$$

**Schillerâ€“Naumann Correlation**

$$
C_D=\frac{24}{Re_p}\left(1+0.15Re_p^{0.687}\right)
$$

| Method | Terminal Velocity |
|---|---|
| Stokes | 0.163 m/s |
| Schillerâ€“Naumann | Approximately 0.137 m/s |
| CFDâ€“DEM (Di Felice) | Approximately 0.129 m/s |

The CFD-DEM prediction differs by approximately **6%** from the Schiller-Naumann terminal-velocity estimate.

The simulated particle Reynolds number is approximately **1.29**, which is outside the strict creeping-flow regime assumed by Stokes' law.

The closer agreement with Schiller-Naumann is consistent with the importance of finite-Reynolds-number drag corrections.

## Acknowledgements

The starting case is adapted from the `settlingTestMPI` example distributed with CFDEMcoupling/LIGGGHTS.

Original tutorial files and software remain attributable to their respective authors and license terms.

The simulation execution, troubleshooting, Python analysis, and validation discussion document the work carried out in this project.
