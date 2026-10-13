# Antigravity Mechanics: Magnetic Suspension System

This document outlines the mechanical design, magnetics, and physics for the levitating smart garbage bin base.

---

## 1. Physics & Earnshaw's Theorem

**Earnshaw's Theorem (1842)** mathematically proves that it is impossible to achieve stable static equilibrium in all three spatial dimensions using only permanent static magnetic fields (or electrostatic charges). 

If permanent magnets are placed in vertical repulsion:
* Vertical axis ($Z$): Restoring repulsive force (stable).
* Horizontal axes ($X, Y$): The floating magnet seeks the lowest potential energy state and will flip sideways or slide off laterally (unstable).

### Engineering Resolution: Mechanical Constraint with Low Friction
To overcome Earnshaw's instability **without active electromagnets or microcontrollers**:
* The vertical axis ($Z$) remains supported entirely by magnetic repulsion.
* The horizontal axes ($X, Y$) and tilt ($\theta_x, \theta_y$) are constrained by a **central non-magnetic guide rod** running through a **low-friction bushing**.

```
                   +------------------------+
                   |  Floating Bin Base     |
                   |  (3D Printed PLA)      |
                   +--[Mag]----------[Mag]--+
                      ( S )          ( S )
                        |              |
                      ( N )          ( N )
                     /\/\/\         /\/\/\   <-- Magnetic Repulsion Gap
                      ( N )          ( N )
                        |              |
                      ( S )          ( S )
                   +--[Mag]----------[Mag]--+
                   |  [PTFE Bushing]        |
===================|========||==============|=================== Guide Rod
                   |  Stationary Base       |
                   |  (PSU & Circuitry)     |
                   +------------------------+
```

---

## 2. Magnet Selection & Arrangement

1. **Magnet Type:** N52 Grade Neodymium (NdFeB) Ring Magnets.
   * Dimensions: Outer Diameter: $25\text{ mm}$, Inner Diameter: $10\text{ mm}$, Thickness: $5\text{ mm}$.
   * Surface Field: $\approx 0.35\text{ Tesla}$ ($3500\text{ Gauss}$).
2. **Polarity Arrangement:**
   * **Base Plate:** 4 to 6 ring magnets mounted around the perimeter with **North pole facing UP**.
   * **Bin Plate:** 4 to 6 matching ring magnets mounted directly opposite with **North pole facing DOWN**.
   * Repulsion creates an equilibrium levitation gap of $\approx 10\text{ to }20\text{ mm}$ depending on bin weight.
3. **Weight Budget:**
   * Maximum floating payload: $250\text{ to }350\text{ grams}$.
   * Construct the bin using lightweight 3D printed PLA (single-perimeter spiral vase mode) or $2\text{ mm}$ balsa wood sheets.

---

## 3. Guide Rod & Bushing Assembly

1. **Guide Rod Material:**
   * Must be **strictly non-ferromagnetic** so it does not attract or distort the magnetic field lines.
   * Recommended: $6\text{ mm}$ or $8\text{ mm}$ polished optical acrylic rod, brass tube, or carbon fiber rod.
2. **Bushing / Sleeve:**
   * PTFE (Teflon) sleeve or dry POM (Delrin) sleeve press-fitted into the center of the bin base.
   * Provides ultra-low coefficient of friction ($\mu_k \approx 0.04$) without requiring liquid lubrication that could attract dust.

---

## 4. Magnetic Field Isolation & Sensor Protection

* **Optical Triangulation Sensor (Sharp GP2Y0A21YK0F):**
  * The sensor works using near-infrared light ($850\text{ nm}$) and an internal position-sensitive diode (PSD) array. It has no internal Hall sensors or inductive coils.
  * **Static magnetic fields have zero effect on photons or silicon photodiodes.**
* **Layout Isolation:**
  * Mount the sensor at the upper rim / lid looking downward into the bin.
  * The sensor is separated from the base magnets by at least $25\text{ to }40\text{ cm}$.
  * Signal wiring (Vo, VCC, GND) should run as a twisted trio along the chassis perimeter to prevent induced loop voltages when the bin oscillates vertically.
