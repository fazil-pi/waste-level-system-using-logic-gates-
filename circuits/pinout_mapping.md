# Complete IC Pinout & Interconnection Guide

This document provides the exact pin connections for all ICs in the **4-Bit Flash ADC Smart Waste Level Indicator**.

---

## 1. Integrated Circuit Summary

| Designator | Part Number | Package | Function | Quantity |
|:---:|:---:|:---:|:---:|:---:|
| **U1** | 74HC148N | DIP-16 | High-Order 8-to-3 Priority Encoder (Levels 8–15) | 1 |
| **U2** | 74HC148N | DIP-16 | Low-Order 8-to-3 Priority Encoder (Levels 0–7) | 1 |
| **U3** | LM339N | DIP-14 | Quad Comparator #1 (Comparators 1 to 4) | 1 |
| **U4** | LM339N | DIP-14 | Quad Comparator #2 (Comparators 5 to 8) | 1 |
| **U5** | LM339N | DIP-14 | Quad Comparator #3 (Comparators 9 to 12) | 1 |
| **U6** | LM339N | DIP-14 | Quad Comparator #4 (Comparators 13 to 15, 1 spare) | 1 |
| **U7** | 74HC00N | DIP-14 | Quad 2-Input NAND Gate (Combiner & Inverter) | 1 |
| **REG1** | LM7805 | TO-220 | +5.0V Linear Voltage Regulator | 1 |

---

## 2. LM339 Pinout & Channel Assignments (DIP-14)

### Standard LM339 Pin Configuration
* **Pin 3:** $V_{CC}$ (+5V Supply)
* **Pin 12:** GND (Ground)
* **Section 1:** Pin 4 = $1\text{IN}^-$, Pin 5 = $1\text{IN}^+$, Pin 2 = $1\text{OUT}$
* **Section 2:** Pin 6 = $2\text{IN}^-$, Pin 7 = $2\text{IN}^+$, Pin 1 = $2\text{OUT}$
* **Section 3:** Pin 8 = $3\text{IN}^-$, Pin 9 = $3\text{IN}^+$, Pin 14 = $3\text{OUT}$
* **Section 4:** Pin 10 = $4\text{IN}^-$, Pin 11 = $4\text{IN}^+$, Pin 13 = $4\text{OUT}$

*(Note: Every comparator output requires a $10\text{ k}\Omega$ pull-up resistor to +5V).*

### LM339 #1 (U3) — Comparators 1 to 4 (0.40V to 1.04V)
* **Pin 3:** +5V
* **Pin 12:** GND
* **Comp 1 (0.56V):** Pin 4 = $V_{\text{sensor}}$, Pin 5 = Ladder Node 1, Pin 2 = Output $\rightarrow$ U2 Pin 11 ($\overline{I_1}$)
* **Comp 2 (0.72V):** Pin 6 = $V_{\text{sensor}}$, Pin 7 = Ladder Node 2, Pin 1 = Output $\rightarrow$ U2 Pin 12 ($\overline{I_2}$)
* **Comp 3 (0.88V):** Pin 8 = $V_{\text{sensor}}$, Pin 9 = Ladder Node 3, Pin 14 = Output $\rightarrow$ U2 Pin 13 ($\overline{I_3}$)
* **Comp 4 (1.04V):** Pin 10 = $V_{\text{sensor}}$, Pin 11 = Ladder Node 4, Pin 13 = Output $\rightarrow$ U2 Pin 1 ($\overline{I_4}$)

### LM339 #2 (U4) — Comparators 5 to 8 (1.20V to 1.68V)
* **Pin 3:** +5V
* **Pin 12:** GND
* **Comp 5 (1.20V):** Pin 4 = $V_{\text{sensor}}$, Pin 5 = Ladder Node 5, Pin 2 = Output $\rightarrow$ U2 Pin 2 ($\overline{I_5}$)
* **Comp 6 (1.36V):** Pin 6 = $V_{\text{sensor}}$, Pin 7 = Ladder Node 6, Pin 1 = Output $\rightarrow$ U2 Pin 3 ($\overline{I_6}$)
* **Comp 7 (1.52V):** Pin 8 = $V_{\text{sensor}}$, Pin 9 = Ladder Node 7, Pin 14 = Output $\rightarrow$ U2 Pin 4 ($\overline{I_7}$)
* **Comp 8 (1.68V):** Pin 10 = $V_{\text{sensor}}$, Pin 11 = Ladder Node 8, Pin 13 = Output $\rightarrow$ U1 Pin 10 ($\overline{I_0}$)

### LM339 #3 (U5) — Comparators 9 to 12 (1.84V to 2.32V)
* **Pin 3:** +5V
* **Pin 12:** GND
* **Comp 9 (1.84V):** Pin 4 = $V_{\text{sensor}}$, Pin 5 = Ladder Node 9, Pin 2 = Output $\rightarrow$ U1 Pin 11 ($\overline{I_1}$)
* **Comp 10 (2.00V):** Pin 6 = $V_{\text{sensor}}$, Pin 7 = Ladder Node 10, Pin 1 = Output $\rightarrow$ U1 Pin 12 ($\overline{I_2}$)
* **Comp 11 (2.16V):** Pin 8 = $V_{\text{sensor}}$, Pin 9 = Ladder Node 11, Pin 14 = Output $\rightarrow$ U1 Pin 13 ($\overline{I_3}$)
* **Comp 12 (2.32V):** Pin 10 = $V_{\text{sensor}}$, Pin 11 = Ladder Node 12, Pin 13 = Output $\rightarrow$ U1 Pin 1 ($\overline{I_4}$)

### LM339 #4 (U6) — Comparators 13 to 15 (2.48V to 2.80V)
* **Pin 3:** +5V
* **Pin 12:** GND
* **Comp 13 (2.48V):** Pin 8 = $V_{\text{sensor}}$, Pin 9 = Ladder Node 13, Pin 14 = Output $\rightarrow$ U1 Pin 2 ($\overline{I_5}$)
* **Comp 14 (2.64V):** Pin 6 = $V_{\text{sensor}}$, Pin 7 = Ladder Node 14, Pin 1 = Output $\rightarrow$ U1 Pin 3 ($\overline{I_6}$)
* **Comp 15 (2.80V):** Pin 4 = $V_{\text{sensor}}$, Pin 5 = Ladder Node 15, Pin 2 = Output $\rightarrow$ U1 Pin 4 ($\overline{I_7}$)
* **Spare Comp 16:** Pin 10 ($V^-$) $\rightarrow$ +5V, Pin 11 ($V^+$) $\rightarrow$ GND, Pin 13 (Out) $\rightarrow$ Unconnected

---

## 3. 74HC148 Priority Encoders Pinout (DIP-16)

### Standard 74HC148 Pin Configuration
* **Pin 16:** $V_{CC}$ (+5V)
* **Pin 8:** GND
* **Pin 5:** $\overline{EI}$ (Enable Input, Active LOW)
* **Pin 15:** $\overline{EO}$ (Enable Output, Active LOW)
* **Pin 14:** $\overline{GS}$ (Group Select / Active Input Detected, Active LOW)
* **Inputs:** Pin 10 = $\overline{I_0}$, Pin 11 = $\overline{I_1}$, Pin 12 = $\overline{I_2}$, Pin 13 = $\overline{I_3}$, Pin 1 = $\overline{I_4}$, Pin 2 = $\overline{I_5}$, Pin 3 = $\overline{I_6}$, Pin 4 = $\overline{I_7}$
* **Outputs:** Pin 9 = $\overline{A_0}$ (LSB), Pin 7 = $\overline{A_1}$, Pin 6 = $\overline{A_2}$ (MSB)

### U1 Connections (High-Order: Levels 8 to 15)
* **Pin 5 ($\overline{EI}$):** Tie to **GND** (Permanently Enabled)
* **Pin 15 ($\overline{EO}$):** Connect to **U2 Pin 5 ($\overline{EI}$)** (Cascade Line)
* **Pin 14 ($\overline{GS}$):** Connect to **U7 Pins 12 & 13** (Inverted for $B_3$)
* **Pin 9 ($\overline{A_0}$):** Connect to **U7 Pin 1**
* **Pin 7 ($\overline{A_1}$):** Connect to **U7 Pin 4**
* **Pin 6 ($\overline{A_2}$):** Connect to **U7 Pin 9**

### U2 Connections (Low-Order: Levels 0 to 7)
* **Pin 5 ($\overline{EI}$):** Connect from **U1 Pin 15 ($\overline{EO}$)**
* **Pin 10 ($\overline{I_0}$):** Tie to **+5V** (Inactive; Level 0 is active when all inputs are inactive)
* **Pin 15 ($\overline{EO}$):** Unconnected / Test Point
* **Pin 14 ($\overline{GS}$):** Unconnected / Test Point
* **Pin 9 ($\overline{A_0}$):** Connect to **U7 Pin 2**
* **Pin 7 ($\overline{A_1}$):** Connect to **U7 Pin 5**
* **Pin 6 ($\overline{A_2}$):** Connect to **U7 Pin 10**

---

## 4. 74HC00 Quad 2-Input NAND Gate Pinout (DIP-14)

* **Pin 14:** $V_{CC}$ (+5V)
* **Pin 7:** GND

| Gate | Input 1 | Input 2 | Output Pin | Signal Destination |
|:---:|:---:|:---:|:---:|:---:|
| **Gate 1** | Pin 1 ($\overline{A_{0,\text{U1}}}$) | Pin 2 ($\overline{A_{0,\text{U2}}}$) | **Pin 3** | $B_0$ (LSB) $\rightarrow 330\Omega \rightarrow$ LED0 |
| **Gate 2** | Pin 4 ($\overline{A_{1,\text{U1}}}$) | Pin 5 ($\overline{A_{1,\text{U2}}}$) | **Pin 6** | $B_1 \rightarrow 330\Omega \rightarrow$ LED1 |
| **Gate 3** | Pin 9 ($\overline{A_{2,\text{U1}}}$) | Pin 10 ($\overline{A_{2,\text{U2}}}$) | **Pin 8** | $B_2 \rightarrow 330\Omega \rightarrow$ LED2 |
| **Gate 4** | Pin 12 ($\overline{GS}_{\text{U1}}$) | Pin 13 ($\overline{GS}_{\text{U1}}$) | **Pin 11** | $B_3$ (MSB) $\rightarrow 330\Omega \rightarrow$ LED3 |

---

## 5. Power & Sensor Pinout

### Sharp GP2Y0A21YK0F Sensor (JST 3-Pin)
* **Red Wire (Pin 1 - VCC):** Connect to **+5V Rail**
* **Black Wire (Pin 2 - GND):** Connect to **System GND**
* **Yellow Wire (Pin 3 - Vo):** Connect through **$10\text{ k}\Omega$ resistor** to $V_{\text{sensor}}$ Analog Bus.
* **Capacitor across Pin 1 & 2:** Solder $47\,\mu\text{F}$ Electrolytic and $0.1\,\mu\text{F}$ Ceramic directly across the connector pins.

### LM7805 Regulator (TO-220)
* **Pin 1 (Input):** +9V Battery (+) terminal
* **Pin 2 (GND / Tab):** Battery (-) terminal & System Ground
* **Pin 3 (Output):** +5.0V Regulated Rail
