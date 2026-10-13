# Benchtop Calibration & Noise Suppression Guide

This guide describes how to calibrate the dual-trimpot resistor ladder and suppress analog noise in the **4-Bit Flash ADC Smart Waste Level Indicator**.

---

## 1. Required Tools
* Digital Multimeter (DMM) with DC millivolt resolution.
* Ceramic or plastic tuning screwdriver (for trimpots).
* Regulated $+9\text{V}$ battery or bench power supply.
* Flat cardboard / white box target (to test sensor distance reflection).

---

## 2. Resistor Ladder Threshold Calibration

The resistor ladder uses two multi-turn cermet trimpots:
* **$P_{\text{top}}$ ($10\text{ k}\Omega$):** Sets the maximum threshold $V_{\text{top}} = 2.80\text{ V}$ (Full bin, $10\text{ cm}$ distance).
* **$P_{\text{bot}}$ ($5\text{ k}\Omega$):** Sets the minimum threshold $V_{\text{bot}} = 0.40\text{ V}$ (Empty bin, $80\text{ cm}$ distance).

```
 +5V Rail ----[ P_top: 10kΩ ]----+ Node 15 (2.80V)
                                 | [R16: 1kΩ]
                                 :
                                 | [R2: 1kΩ]
 GND ---------[ P_bot: 5kΩ  ]----+ Node 1  (0.40V)
```

### Calibration Steps:
1. **Disconnect Sensor Output:** Disconnect the Yellow signal wire from the Sharp sensor so no fluctuating analog signal reaches the comparators.
2. **Power Up:** Apply $+9\text{V}$ to the LM7805 regulator input. Verify that the $+5\text{V}$ rail reads $+5.00\text{ V} \pm 0.05\text{ V}$ with respect to GND.
3. **Calibrate Lower Baseline ($V_{\text{bot}}$):**
   * Clip the DMM black probe to **GND**.
   * Place the DMM red probe on **Ladder Node 1** (between $R_1$ and $P_{\text{bot}}$).
   * Slowly turn **$P_{\text{bot}}$** until the multimeter reads exactly **$0.40\text{ V}$**.
4. **Calibrate Upper Ceiling ($V_{\text{top}}$):**
   * Place the DMM red probe on **Ladder Node 15** (top of the ladder below $P_{\text{top}}$).
   * Slowly turn **$P_{\text{top}}$** until the multimeter reads exactly **$2.80\text{ V}$**.
5. **Verify Intermediate Thresholds:**
   * Step through Nodes 1 through 15.
   * Each step should increment by $\Delta V \approx \frac{2.80\text{V} - 0.40\text{V}}{16} \approx 0.15\text{ V}$.

| Ladder Tap | Target Voltage ($V$) | Comparator Channel | Trigger Level |
|:---:|:---:|:---:|:---:|
| **Node 1** | $0.40\text{ V}$ | Comp 1 (U3) | Level 1 |
| **Node 2** | $0.56\text{ V}$ | Comp 2 (U3) | Level 2 |
| **Node 3** | $0.72\text{ V}$ | Comp 3 (U3) | Level 3 |
| **Node 4** | $0.88\text{ V}$ | Comp 4 (U3) | Level 4 |
| **Node 5** | $1.04\text{ V}$ | Comp 5 (U4) | Level 5 |
| **Node 6** | $1.20\text{ V}$ | Comp 6 (U4) | Level 6 |
| **Node 7** | $1.36\text{ V}$ | Comp 7 (U4) | Level 7 |
| **Node 8** | $1.52\text{ V}$ | Comp 8 (U4) | Level 8 |
| **Node 9** | $1.68\text{ V}$ | Comp 9 (U5) | Level 9 |
| **Node 10** | $1.84\text{ V}$ | Comp 10 (U5) | Level 10 |
| **Node 11** | $2.00\text{ V}$ | Comp 11 (U5) | Level 11 |
| **Node 12** | $2.16\text{ V}$ | Comp 12 (U5) | Level 12 |
| **Node 13** | $2.32\text{ V}$ | Comp 13 (U6) | Level 13 |
| **Node 14** | $2.48\text{ V}$ | Comp 14 (U6) | Level 14 |
| **Node 15** | $2.80\text{ V}$ | Comp 15 (U6) | Level 15 |

---

## 3. Eliminating Boundary Chatter & Noise

Because pure Flash ADCs without microcontrollers do not have software debouncing or digital averaging, analog voltage noise right at a comparator trip point can cause rapid flickering between adjacent binary codes.

### Hardware Anti-Chatter Solutions:
1. **Sensor RC Low-Pass Filter:**
   * Place a **$10\text{ k}\Omega$ series resistor** on the Sharp sensor signal line, followed by a **$1\,\mu\text{F}$ ceramic capacitor to GND**.
   * Cutoff frequency:
     $$f_c = \frac{1}{2\pi R C} = \frac{1}{2\pi \times 10{,}000 \times 10^{-6}} \approx 15.9\text{ Hz}$$
   * This smooths out high-frequency IR strobe noise while tracking waste accumulation with zero perceptible lag.
2. **Current-Pulse Decoupling:**
   * Sharp GP2Y0A21YK0F distance sensors draw sharp $30\text{ mA}$ pulse currents during emitter strobes.
   * Solder a **$47\,\mu\text{F}$ electrolytic capacitor** directly across the sensor `VCC` and `GND` leads right at the sensor plug.
3. **Decoupling Capacitors per IC:**
   * Solder a **$0.1\,\mu\text{F}$ monolithic ceramic capacitor** as close as possible between pin $V_{CC}$ and pin $\text{GND}$ of each LM339, 74HC148, and 74HC00 IC.
