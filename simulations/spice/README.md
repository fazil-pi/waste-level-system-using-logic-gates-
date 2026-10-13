# SPICE Simulation Guide (LTspice / ngspice)

This directory contains the analog SPICE netlist for transient analysis of the Flash ADC ladder and comparator stages.

---

## 1. Running with LTspice
1. Open [LTspice](https://www.analog.com/en/design-center/design-tools-and-calculators/ltspice-simulator.html).
2. Go to **File** $\rightarrow$ **Open** and select `flash_adc_simulation.cir`.
3. Click the **Run** (Running Man) button.
4. Add trace: `V(VSENSOR)` to view the trash level ramp from $0.40\text{V}$ to $2.80\text{V}$.
5. Add traces: `V(C1_OUT)`, `V(C8_OUT)`, `V(C15_OUT)` to observe the sequential active-LOW transitions of the comparators.

---

## 2. Running with ngspice (Command Line)
If you have `ngspice` installed:
```bash
ngspice -b flash_adc_simulation.cir
```
This produces tabular output verifying that each comparator trips cleanly at its calculated threshold.
