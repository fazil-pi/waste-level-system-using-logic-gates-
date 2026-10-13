# Bill of Materials (BOM)

This document lists all electrical, electro-mechanical, and structural components required to build the **4-Bit Flash ADC Smart Waste Level Indicator**.

---

## 1. Integrated Circuits & Active Semiconductor Components

| Item # | Part Number | Description / Specifications | Package | Qty | Reference Designators |
|:---:|:---:|:---|:---:|:---:|:---:|
| 1 | **LM339N** | Quad Open-Collector Voltage Comparator | DIP-14 | 4 | U3, U4, U5, U6 |
| 2 | **74HC148N** | 8-to-3 Line Priority Encoder (CMOS) | DIP-16 | 2 | U1, U2 |
| 3 | **74HC00N** | Quad 2-Input NAND Gate (High-Speed CMOS) | DIP-14 | 1 | U7 |
| 4 | **LM7805** | +5.0V, 1A Positive Voltage Regulator | TO-220 | 1 | REG1 |
| 5 | **GP2Y0A21YK0F** | Sharp Analog IR Distance Sensor (10–80 cm) | Module | 1 | S1 |

---

## 2. Passive Components (Resistors & Capacitors)

| Item # | Value | Description / Tolerance | Rating | Qty | Reference Designators |
|:---:|:---:|:---|:---:|:---:|:---:|
| 6 | **$1.00\text{ k}\Omega$** | Metal Film Resistor, 1% Precision | 0.25W | 16 | R1 – R16 (Resistor Ladder) |
| 7 | **$10\text{ k}\Omega$** | Carbon Film Resistor (or 16-pin bussed SIP) | 0.25W | 15 | R_pull1 – R_pull15 (Pull-ups) |
| 8 | **$10\text{ k}\Omega$** | Carbon Film Resistor (Filter) | 0.25W | 1 | R_filter (Sensor RC low-pass) |
| 9 | **$330\text{ }\Omega$** | Carbon Film Resistor, 5% (LED Limiters) | 0.25W | 4 | R_led0 – R_led3 |
| 10 | **$10\text{ k}\Omega$** | Multi-Turn Cermet Trimpot (Model 3296W) | 0.5W | 1 | P_top (Upper Ladder Trim) |
| 11 | **$5\text{ k}\Omega$** | Multi-Turn Cermet Trimpot (Model 3296W) | 0.5W | 1 | P_bot (Lower Ladder Trim) |
| 12 | **$47\,\mu\text{F}$** | Radial Aluminum Electrolytic Capacitor | 25V | 1 | C_sensor (Sensor Pulse Decoupling) |
| 13 | **$10\,\mu\text{F}$** | Radial Aluminum Electrolytic Capacitor | 25V | 2 | C_in, C_out (LM7805 Bulk Filters) |
| 14 | **$1\,\mu\text{F}$** | Multilayer Ceramic Capacitor (MLCC) | 50V | 1 | C_filter (Sensor Anti-Chatter) |
| 15 | **$0.33\,\mu\text{F}$** | Ceramic Disc / Film Capacitor | 50V | 1 | C_reg_in (Regulator Input) |
| 16 | **$0.1\,\mu\text{F}$** | Monolithic Ceramic Capacitor (100nF) | 50V | 8 | C_dec1 – C_dec8 (IC Decoupling) |

---

## 3. Optoelectronics & Display

| Item # | Component | Description / Color | Package | Qty | Reference Designators |
|:---:|:---:|:---|:---:|:---:|:---:|
| 17 | **LED - Red** | 5mm High-Efficiency LED ($V_f \approx 2.0\text{V}$) | T-1 3/4 | 1 | LED3 ($B_3$ - MSB, Weight 8) |
| 18 | **LED - Yellow** | 5mm Standard LED ($V_f \approx 2.1\text{V}$) | T-1 3/4 | 2 | LED2, LED1 ($B_2, B_1$ - Weights 4, 2) |
| 19 | **LED - Green** | 5mm High-Efficiency LED ($V_f \approx 2.2\text{V}$) | T-1 3/4 | 1 | LED0 ($B_0$ - LSB, Weight 1) |

---

## 4. Hardware, Power & Magnetic Suspension

| Item # | Component | Specifications | Qty | Notes |
|:---:|:---:|:---|:---:|:---|
| 20 | **N52 Ring Magnets** | OD $25\text{mm}$, ID $10\text{mm}$, Thick $5\text{mm}$ | 8–12 | Repulsive magnetic base & bin |
| 21 | **Acrylic Guide Rod** | Polished Cast Acrylic, $\varnothing 8\text{mm} \times 250\text{mm}$ | 1 | Central vertical constraint |
| 22 | **PTFE Bushing** | ID $8\text{mm}$, OD $12\text{mm}$, Length $15\text{mm}$ | 1 | Ultra-low friction sleeve |
| 23 | **Battery Connector** | 9V Heavy-Duty Snap Clip with Leads | 1 | Power connection |
| 24 | **Power Source** | 9V Alkaline Battery or 2S LiPo (7.4V) | 1 | Main circuit power |
| 25 | **Breadboard / PCB** | 830-Point Solderless Breadboard or Stripboard | 2 | Prototyping |
| 26 | **Jumper Wires** | 22 AWG Solid Core Breadboard Wires | 1 pack | Circuit interconnects |
