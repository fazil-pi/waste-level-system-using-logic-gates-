#!/usr/bin/env python3
"""
Verification Script and Truth Table Generator for:
4-Bit Flash ADC Smart Garbage Bin Level Indicator (Hardware Logic Only)
"""

import csv
import sys

def simulate_adc():
    rows = []
    # Headers
    headers = [
        "Level",
        "Fill_Percent",
        "Distance_cm",
        "Sensor_V",
        "Comp_Active_Count",
        "U1_Inputs_I7_I0",
        "U1_EO",
        "U1_GS",
        "U1_A2_A1_A0",
        "U2_Inputs_I7_I0",
        "U2_EI",
        "U2_A2_A1_A0",
        "B3",
        "B2",
        "B1",
        "B0",
        "Binary_Code",
        "Hex_Code"
    ]

    for level in range(16):
        fill_pct = f"{round((level / 15) * 100)}%"
        # Distance: Level 0 = 80 cm, Level 15 = 10 cm
        dist_cm = round(80 - (level / 15) * 70, 1)
        # Voltage: Level 0 = 0.4V, Level 15 = 2.8V
        v_sensor = round(0.40 + (level / 15) * 2.40, 2)
        
        # 15 comparators:
        # Comp k is active (pulls LOW = 0) if level >= k. Else HIGH (1).
        comp = [0 if level >= k else 1 for k in range(1, 16)] # comp[0] is comp1, comp[14] is comp15
        
        # U1 (High order, inputs 8 to 15):
        # I7 = comp15, I6 = comp14, ..., I0 = comp8
        u1_in = [comp[14 - i] for i in range(8)]
        u1_in_str = "".join(str(b) for b in u1_in)
        
        # U1 enable input EI is permanently grounded (0)
        u1_ei = 0
        
        # Priority encoder logic for U1:
        # Highest active input (index 7 down to 0 with value 0)
        u1_active_idx = None
        for i in range(7, -1, -1):
            if u1_in[7 - i] == 0: # I_i is active LOW
                u1_active_idx = i
                break
                
        if u1_active_idx is not None:
            u1_gs = 0 # Active LOW
            u1_eo = 1 # HIGH (disables U2)
            # A2, A1, A0 are active LOW representations of active index
            # Index 7 -> 000, Index 6 -> 001, ..., Index 0 -> 111
            u1_a = [(~(u1_active_idx >> shift) & 1) for shift in (2, 1, 0)]
        else:
            u1_gs = 1
            u1_eo = 0 # LOW (enables U2)
            u1_a = [1, 1, 1]
            
        u1_a_str = "".join(str(b) for b in u1_a)
        
        # U2 (Low order, inputs 0 to 7):
        # I7 = comp7, I6 = comp6, ..., I1 = comp1, I0 = VCC (1)
        u2_in = [comp[6 - i] for i in range(7)] + [1]
        u2_in_str = "".join(str(b) for b in u2_in)
        
        # U2 EI is connected to U1 EO
        u2_ei = u1_eo
        
        if u2_ei == 0: # Enabled
            u2_active_idx = None
            for i in range(7, -1, -1):
                if u2_in[7 - i] == 0:
                    u2_active_idx = i
                    break
            if u2_active_idx is not None:
                u2_a = [(~(u2_active_idx >> shift) & 1) for shift in (2, 1, 0)]
            else:
                u2_a = [1, 1, 1]
        else:
            # Disabled: all outputs are 1
            u2_a = [1, 1, 1]
            
        u2_a_str = "".join(str(b) for b in u2_a)
        
        # 74HC00 NAND Combiner:
        # B3 = NOT(U1_GS) = NAND(U1_GS, U1_GS)
        b3 = 1 if u1_gs == 0 else 0
        # Bn = NAND(U1_An, U2_An)
        b2 = 1 if not (u1_a[0] == 1 and u2_a[0] == 1) else 0
        b1 = 1 if not (u1_a[1] == 1 and u2_a[1] == 1) else 0
        b0 = 1 if not (u1_a[2] == 1 and u2_a[2] == 1) else 0
        
        bin_code = f"{b3}{b2}{b1}{b0}"
        val = (b3 << 3) | (b2 << 2) | (b1 << 1) | b0
        hex_code = f"0x{val:X}"
        
        assert val == level, f"Verification failed at level {level}: got {val}"
        
        rows.append([
            level,
            fill_pct,
            f"{dist_cm} cm",
            f"{v_sensor:.2f} V",
            level,
            u1_in_str,
            u1_eo,
            u1_gs,
            u1_a_str,
            u2_in_str,
            u2_ei,
            u2_a_str,
            b3,
            b2,
            b1,
            b0,
            bin_code,
            hex_code
        ])
        
    return headers, rows

if __name__ == "__main__":
    headers, rows = simulate_adc()
    
    # Save CSV
    csv_path = "simulations/truth_table.csv"
    with open(csv_path, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(headers)
        writer.writerows(rows)
        
    print(f"Successfully generated and verified 16-state truth table: {csv_path}")
    print("\nVerified Binary Outputs:")
    for r in rows:
        print(f"Level {r[0]:2d} ({r[1]:>4s}) | Dist: {r[2]:>7s} | Vin: {r[3]:>6s} | Binary: {r[16]} | Hex: {r[17]}")
