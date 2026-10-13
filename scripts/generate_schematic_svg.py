#!/usr/bin/env python3
"""
Generates a clean, professional SVG schematic diagram for the
4-Bit Flash ADC Smart Garbage Bin Level Indicator.
"""

def generate_schematic_svg():
    width = 1400
    height = 920

    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="100%" height="100%" style="background-color: #0f172a; font-family: 'Segoe UI', -apple-system, BlinkMacSystemFont, Roboto, sans-serif;">
  <defs>
    <linearGradient id="gradHeader" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#38bdf8"/>
      <stop offset="100%" stop-color="#818cf8"/>
    </linearGradient>
    <filter id="shadow" x="-5%" y="-5%" width="110%" height="110%">
      <feDropShadow dx="0" dy="4" stdDeviation="6" flood-color="#000" flood-opacity="0.4"/>
    </filter>
  </defs>

  <!-- Title & Header Bar -->
  <rect x="20" y="20" width="1360" height="70" rx="10" fill="#1e293b" filter="url(#shadow)" stroke="#334155" stroke-width="1.5"/>
  <text x="50" y="52" fill="url(#gradHeader)" font-size="22" font-weight="bold" letter-spacing="1">4-BIT FLASH ADC SMART WASTE LEVEL INDICATOR (HARDWARE LOGIC)</text>
  <text x="50" y="74" fill="#94a3b8" font-size="13">Sharp GP2Y0A21YK0F  •  15x LM339 Comparators  •  2x 74HC148 Encoders  •  1x 74HC00 NAND Combiner  •  LM7805 5V PSU</text>

  <!-- SECTION 1: POWER & SENSOR BLOCK (Top-Left) -->
  <g transform="translate(30, 110)">
    <rect width="320" height="220" rx="8" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5" filter="url(#shadow)"/>
    <rect width="320" height="32" rx="8" fill="#0284c7"/>
    <text x="15" y="22" fill="#ffffff" font-size="13" font-weight="bold">STAGE 1: POWER &amp; IR DISTANCE SENSOR</text>

    <!-- LM7805 Regulator Box -->
    <rect x="20" y="50" width="120" height="70" rx="4" fill="#0f172a" stroke="#64748b" stroke-width="1"/>
    <text x="45" y="75" fill="#38bdf8" font-size="12" font-weight="bold">LM7805</text>
    <text x="35" y="95" fill="#94a3b8" font-size="10">+5V REGULATOR</text>
    
    <!-- Power Lines -->
    <text x="25" y="145" fill="#ef4444" font-size="11" font-weight="bold">+9V Batt In</text>
    <line x1="80" y1="120" x2="80" y2="135" stroke="#ef4444" stroke-width="2"/>
    <text x="100" y="170" fill="#10b981" font-size="11" font-weight="bold">+5V VCC Rail</text>
    <line x1="140" y1="85" x2="200" y2="85" stroke="#10b981" stroke-width="2"/>

    <!-- Sharp Sensor Box -->
    <rect x="180" y="110" width="120" height="90" rx="4" fill="#0f172a" stroke="#f59e0b" stroke-width="1"/>
    <text x="195" y="132" fill="#f59e0b" font-size="11" font-weight="bold">Sharp IR Sensor</text>
    <text x="195" y="148" fill="#94a3b8" font-size="9">GP2Y0A21YK0F</text>
    <text x="195" y="165" fill="#38bdf8" font-size="9">Range: 10-80 cm</text>
    <text x="195" y="182" fill="#10b981" font-size="9">Out: 0.4V - 2.8V</text>

    <!-- Decoupling Note -->
    <text x="20" y="200" fill="#64748b" font-size="9">Capacitors: 47µF + 0.1µF across sensor</text>
  </g>

  <!-- SECTION 2: 16-RESISTOR LADDER DIVIDER (Bottom-Left) -->
  <g transform="translate(30, 350)">
    <rect width="320" height="540" rx="8" fill="#1e293b" stroke="#34d399" stroke-width="1.5" filter="url(#shadow)"/>
    <rect width="320" height="32" rx="8" fill="#059669"/>
    <text x="15" y="22" fill="#ffffff" font-size="13" font-weight="bold">STAGE 2: PRECISION RESISTOR LADDER</text>

    <text x="30" y="60" fill="#ef4444" font-size="11" font-weight="bold">+5V Rail</text>
    <line x1="85" y1="55" x2="85" y2="75" stroke="#ef4444" stroke-width="2"/>

    <!-- Top Trimpot -->
    <rect x="60" y="75" width="50" height="30" fill="#0f172a" stroke="#f59e0b" stroke-width="1"/>
    <text x="68" y="94" fill="#f59e0b" font-size="10">P_top</text>
    <text x="120" y="94" fill="#94a3b8" font-size="10">10kΩ Pot (Sets 2.8V)</text>

    <!-- Resistor Ladder Graphic -->
    <line x1="85" y1="105" x2="85" y2="445" stroke="#34d399" stroke-width="2.5"/>
    
    <!-- Taps Sample -->
    <circle cx="85" cy="125" r="4" fill="#38bdf8"/>
    <text x="95" y="130" fill="#38bdf8" font-size="10">Node 15 (2.80V) -> Comp 15 V+</text>

    <circle cx="85" cy="165" r="4" fill="#38bdf8"/>
    <text x="95" y="170" fill="#38bdf8" font-size="10">Node 14 (2.64V) -> Comp 14 V+</text>

    <circle cx="85" cy="205" r="4" fill="#38bdf8"/>
    <text x="95" y="210" fill="#38bdf8" font-size="10">Node 13 (2.48V) -> Comp 13 V+</text>

    <text x="80" y="250" fill="#64748b" font-size="18" font-weight="bold">:</text>
    <text x="100" y="250" fill="#94a3b8" font-size="10">16x 1kΩ 1% Matched Resistors (ΔV = 0.15V)</text>
    <text x="80" y="275" fill="#64748b" font-size="18" font-weight="bold">:</text>

    <circle cx="85" cy="315" r="4" fill="#38bdf8"/>
    <text x="95" y="320" fill="#38bdf8" font-size="10">Node 2  (0.56V) -> Comp 2 V+</text>

    <circle cx="85" cy="355" r="4" fill="#38bdf8"/>
    <text x="95" y="360" fill="#38bdf8" font-size="10">Node 1  (0.40V) -> Comp 1 V+</text>

    <!-- Bottom Trimpot -->
    <rect x="60" y="390" width="50" height="30" fill="#0f172a" stroke="#f59e0b" stroke-width="1"/>
    <text x="68" y="409" fill="#f59e0b" font-size="10">P_bot</text>
    <text x="120" y="409" fill="#94a3b8" font-size="10">5kΩ Pot (Sets 0.4V)</text>

    <line x1="85" y1="420" x2="85" y2="445" stroke="#64748b" stroke-width="2"/>
    <line x1="70" y1="445" x2="100" y2="445" stroke="#64748b" stroke-width="3"/>
    <line x1="75" y1="450" x2="95" y2="450" stroke="#64748b" stroke-width="2"/>
    <line x1="80" y1="455" x2="90" y2="455" stroke="#64748b" stroke-width="1"/>
    <text x="105" y="455" fill="#64748b" font-size="10">GND</text>
    
    <rect x="20" y="480" width="280" height="45" rx="4" fill="#0f172a"/>
    <text x="30" y="498" fill="#facc15" font-size="10" font-weight="bold">Calibration Note:</text>
    <text x="30" y="514" fill="#94a3b8" font-size="9">P_bot sets 0% level (0.4V), P_top sets 100% level (2.8V)</text>
  </g>

  <!-- SECTION 3: 15 COMPARATORS (Center) -->
  <g transform="translate(380, 110)">
    <rect width="360" height="780" rx="8" fill="#1e293b" stroke="#818cf8" stroke-width="1.5" filter="url(#shadow)"/>
    <rect width="360" height="32" rx="8" fill="#4f46e5"/>
    <text x="15" y="22" fill="#ffffff" font-size="13" font-weight="bold">STAGE 3: 15x LM339 COMPARATORS (4x ICs)</text>

    <!-- Signal Bus Info -->
    <rect x="20" y="45" width="320" height="50" rx="4" fill="#0f172a" stroke="#6366f1" stroke-width="1"/>
    <text x="30" y="65" fill="#a5b4fc" font-size="10" font-weight="bold">Common Inverting Bus (V-):</text>
    <text x="30" y="82" fill="#38bdf8" font-size="10">Sharp Sensor Signal (0.4V - 2.8V) -> ALL 15 V- pins</text>

    <!-- Comparator Block Cards -->
    <!-- U6 (LM339 #4) -->
    <rect x="20" y="110" width="320" height="130" rx="6" fill="#0f172a" stroke="#475569" stroke-width="1"/>
    <text x="30" y="130" fill="#c084fc" font-size="11" font-weight="bold">LM339 #4 (U6): Levels 15, 14, 13</text>
    <text x="30" y="150" fill="#94a3b8" font-size="9">Comp 15: V+ = 2.80V | V- = V_sensor | Out = Pin 2  -> ~I7 (U1)</text>
    <text x="30" y="170" fill="#94a3b8" font-size="9">Comp 14: V+ = 2.64V | V- = V_sensor | Out = Pin 1  -> ~I6 (U1)</text>
    <text x="30" y="190" fill="#94a3b8" font-size="9">Comp 13: V+ = 2.48V | V- = V_sensor | Out = Pin 14 -> ~I5 (U1)</text>
    <text x="30" y="215" fill="#64748b" font-size="9">Comp 16 Unused (Inputs tied to safe rails)</text>

    <!-- U5 (LM339 #3) -->
    <rect x="20" y="260" width="320" height="145" rx="6" fill="#0f172a" stroke="#475569" stroke-width="1"/>
    <text x="30" y="280" fill="#c084fc" font-size="11" font-weight="bold">LM339 #3 (U5): Levels 12, 11, 10, 9</text>
    <text x="30" y="300" fill="#94a3b8" font-size="9">Comp 12: V+ = 2.32V | V- = V_sensor | Out = Pin 13 -> ~I4 (U1)</text>
    <text x="30" y="320" fill="#94a3b8" font-size="9">Comp 11: V+ = 2.16V | V- = V_sensor | Out = Pin 14 -> ~I3 (U1)</text>
    <text x="30" y="340" fill="#94a3b8" font-size="9">Comp 10: V+ = 2.00V | V- = V_sensor | Out = Pin 1  -> ~I2 (U1)</text>
    <text x="30" y="360" fill="#94a3b8" font-size="9">Comp 9:  V+ = 1.84V | V- = V_sensor | Out = Pin 2  -> ~I1 (U1)</text>
    <text x="30" y="385" fill="#10b981" font-size="9">Outputs pulled up to +5V with 10kΩ SIP array</text>

    <!-- U4 (LM339 #2) -->
    <rect x="20" y="425" width="320" height="145" rx="6" fill="#0f172a" stroke="#475569" stroke-width="1"/>
    <text x="30" y="445" fill="#c084fc" font-size="11" font-weight="bold">LM339 #2 (U4): Levels 8, 7, 6, 5</text>
    <text x="30" y="465" fill="#94a3b8" font-size="9">Comp 8:  V+ = 1.68V | V- = V_sensor | Out = Pin 13 -> ~I0 (U1)</text>
    <text x="30" y="485" fill="#38bdf8" font-size="9">---------------- Boundary between U1 &amp; U2 ----------------</text>
    <text x="30" y="505" fill="#94a3b8" font-size="9">Comp 7:  V+ = 1.52V | V- = V_sensor | Out = Pin 14 -> ~I7 (U2)</text>
    <text x="30" y="525" fill="#94a3b8" font-size="9">Comp 6:  V+ = 1.36V | V- = V_sensor | Out = Pin 1  -> ~I6 (U2)</text>
    <text x="30" y="545" fill="#94a3b8" font-size="9">Comp 5:  V+ = 1.20V | V- = V_sensor | Out = Pin 2  -> ~I5 (U2)</text>

    <!-- U3 (LM339 #1) -->
    <rect x="20" y="590" width="320" height="145" rx="6" fill="#0f172a" stroke="#475569" stroke-width="1"/>
    <text x="30" y="610" fill="#c084fc" font-size="11" font-weight="bold">LM339 #1 (U3): Levels 4, 3, 2, 1</text>
    <text x="30" y="630" fill="#94a3b8" font-size="9">Comp 4:  V+ = 1.04V | V- = V_sensor | Out = Pin 13 -> ~I4 (U2)</text>
    <text x="30" y="650" fill="#94a3b8" font-size="9">Comp 3:  V+ = 0.88V | V- = V_sensor | Out = Pin 14 -> ~I3 (U2)</text>
    <text x="30" y="670" fill="#94a3b8" font-size="9">Comp 2:  V+ = 0.72V | V- = V_sensor | Out = Pin 1  -> ~I2 (U2)</text>
    <text x="30" y="690" fill="#94a3b8" font-size="9">Comp 1:  V+ = 0.56V | V- = V_sensor | Out = Pin 2  -> ~I1 (U2)</text>
    <text x="30" y="715" fill="#34d399" font-size="9">Open Collector: Inverts Vin > Vth directly to Active-LOW (0V)</text>

    <text x="30" y="760" fill="#facc15" font-size="10" font-weight="bold">Thermometer Code -> Active-LOW Priority Logic</text>
  </g>

  <!-- SECTION 4: DIGITAL LOGIC (PRIORITY ENCODERS & NAND COMBINER) (Right) -->
  <g transform="translate(770, 110)">
    <rect width="590" height="780" rx="8" fill="#1e293b" stroke="#f43f5e" stroke-width="1.5" filter="url(#shadow)"/>
    <rect width="590" height="32" rx="8" fill="#e11d48"/>
    <text x="15" y="22" fill="#ffffff" font-size="13" font-weight="bold">STAGE 4: 74HC148 ENCODERS &amp; 74HC00 COMBINER &amp; LED DISPLAY</text>

    <!-- U1: High Order 74HC148 -->
    <rect x="25" y="55" width="240" height="230" rx="6" fill="#0f172a" stroke="#38bdf8" stroke-width="1.5"/>
    <rect x="25" y="55" width="240" height="26" rx="6" fill="#0284c7"/>
    <text x="35" y="73" fill="#ffffff" font-size="11" font-weight="bold">U1: 74HC148 (High: 8-15)</text>
    
    <text x="35" y="105" fill="#94a3b8" font-size="9">Pin 5  (~EI)  ---> GND (Enabled)</text>
    <text x="35" y="125" fill="#94a3b8" font-size="9">Pin 4  (~I7)  &lt;--- Comp 15</text>
    <text x="35" y="145" fill="#94a3b8" font-size="9">Pin 3  (~I6)  &lt;--- Comp 14</text>
    <text x="35" y="165" fill="#94a3b8" font-size="9">Pin 2  (~I5)  &lt;--- Comp 13</text>
    <text x="35" y="185" fill="#94a3b8" font-size="9">Pin 1  (~I4)  &lt;--- Comp 12</text>
    <text x="35" y="205" fill="#94a3b8" font-size="9">Pin 13 (~I3)  &lt;--- Comp 11</text>
    <text x="35" y="225" fill="#94a3b8" font-size="9">Pin 12 (~I2)  &lt;--- Comp 10</text>
    <text x="35" y="245" fill="#94a3b8" font-size="9">Pin 11 (~I1)  &lt;--- Comp 9</text>
    <text x="35" y="265" fill="#94a3b8" font-size="9">Pin 10 (~I0)  &lt;--- Comp 8</text>

    <!-- U2: Low Order 74HC148 -->
    <rect x="25" y="320" width="240" height="230" rx="6" fill="#0f172a" stroke="#38bdf8" stroke-width="1.5"/>
    <rect x="25" y="320" width="240" height="26" rx="6" fill="#0284c7"/>
    <text x="35" y="338" fill="#ffffff" font-size="11" font-weight="bold">U2: 74HC148 (Low: 0-7)</text>

    <text x="35" y="370" fill="#f43f5e" font-size="9" font-weight="bold">Pin 5  (~EI)  &lt;--- U1 Pin 15 (~EO)</text>
    <text x="35" y="390" fill="#94a3b8" font-size="9">Pin 4  (~I7)  &lt;--- Comp 7</text>
    <text x="35" y="410" fill="#94a3b8" font-size="9">Pin 3  (~I6)  &lt;--- Comp 6</text>
    <text x="35" y="430" fill="#94a3b8" font-size="9">Pin 2  (~I5)  &lt;--- Comp 5</text>
    <text x="35" y="450" fill="#94a3b8" font-size="9">Pin 1  (~I4)  &lt;--- Comp 4</text>
    <text x="35" y="470" fill="#94a3b8" font-size="9">Pin 13 (~I3)  &lt;--- Comp 3</text>
    <text x="35" y="490" fill="#94a3b8" font-size="9">Pin 12 (~I2)  &lt;--- Comp 2</text>
    <text x="35" y="510" fill="#94a3b8" font-size="9">Pin 11 (~I1)  &lt;--- Comp 1</text>
    <text x="35" y="530" fill="#10b981" font-size="9" font-weight="bold">Pin 10 (~I0)  ---> +5V (Tied Inactive)</text>

    <!-- Cascading Line Indicator -->
    <path d="M 265 175 L 290 175 L 290 370 L 265 370" fill="none" stroke="#f43f5e" stroke-width="2" stroke-dasharray="4"/>
    <text x="295" y="275" fill="#f43f5e" font-size="10" font-weight="bold">Cascade: ~EO_1 -> ~EI_2</text>

    <!-- Combiner: 74HC00 Quad NAND -->
    <rect x="340" y="55" width="220" height="260" rx="6" fill="#0f172a" stroke="#a855f7" stroke-width="1.5"/>
    <rect x="340" y="55" width="220" height="26" rx="6" fill="#9333ea"/>
    <text x="350" y="73" fill="#ffffff" font-size="11" font-weight="bold">U7: 74HC00 QUAD NAND</text>

    <!-- Gates -->
    <text x="350" y="105" fill="#c084fc" font-size="10" font-weight="bold">Gate 1: Bit 0 (LSB)</text>
    <text x="350" y="122" fill="#94a3b8" font-size="9">Pins 1 &amp; 2: ~A0_U1, ~A0_U2</text>
    <text x="350" y="137" fill="#38bdf8" font-size="9">Pin 3 Output -> B0</text>

    <text x="350" y="160" fill="#c084fc" font-size="10" font-weight="bold">Gate 2: Bit 1</text>
    <text x="350" y="177" fill="#94a3b8" font-size="9">Pins 4 &amp; 5: ~A1_U1, ~A1_U2</text>
    <text x="350" y="192" fill="#38bdf8" font-size="9">Pin 6 Output -> B1</text>

    <text x="350" y="215" fill="#c084fc" font-size="10" font-weight="bold">Gate 3: Bit 2</text>
    <text x="350" y="232" fill="#94a3b8" font-size="9">Pins 9 &amp; 10: ~A2_U1, ~A2_U2</text>
    <text x="350" y="247" fill="#38bdf8" font-size="9">Pin 8 Output -> B2</text>

    <text x="350" y="270" fill="#c084fc" font-size="10" font-weight="bold">Gate 4: Bit 3 (MSB)</text>
    <text x="350" y="287" fill="#94a3b8" font-size="9">Pins 12 &amp; 13: ~GS_U1 (Inverter)</text>
    <text x="350" y="302" fill="#38bdf8" font-size="9">Pin 11 Output -> B3</text>

    <!-- FINAL 4-BIT LED DISPLAY PANEL -->
    <rect x="340" y="340" width="220" height="210" rx="6" fill="#0f172a" stroke="#10b981" stroke-width="1.5"/>
    <rect x="340" y="340" width="220" height="26" rx="6" fill="#059669"/>
    <text x="350" y="358" fill="#ffffff" font-size="11" font-weight="bold">4-BIT BINARY LED DISPLAY</text>

    <!-- LED 3 (MSB) -->
    <circle cx="375" cy="405" r="14" fill="#ef4444" stroke="#fca5a5" stroke-width="2"/>
    <text x="367" y="410" fill="#ffffff" font-size="11" font-weight="bold">D3</text>
    <text x="405" y="402" fill="#ef4444" font-size="11" font-weight="bold">LED 3 (MSB, 2³ = 8)</text>
    <text x="405" y="417" fill="#94a3b8" font-size="9">From Pin 11 (B3) via 330Ω</text>

    <!-- LED 2 -->
    <circle cx="375" cy="445" r="14" fill="#f59e0b" stroke="#fde68a" stroke-width="2"/>
    <text x="367" y="450" fill="#ffffff" font-size="11" font-weight="bold">D2</text>
    <text x="405" y="442" fill="#f59e0b" font-size="11" font-weight="bold">LED 2 (2² = 4)</text>
    <text x="405" y="457" fill="#94a3b8" font-size="9">From Pin 8 (B2) via 330Ω</text>

    <!-- LED 1 -->
    <circle cx="375" cy="485" r="14" fill="#3b82f6" stroke="#93c5fd" stroke-width="2"/>
    <text x="367" y="490" fill="#ffffff" font-size="11" font-weight="bold">D1</text>
    <text x="405" y="482" fill="#3b82f6" font-size="11" font-weight="bold">LED 1 (2¹ = 2)</text>
    <text x="405" y="497" fill="#94a3b8" font-size="9">From Pin 6 (B1) via 330Ω</text>

    <!-- LED 0 (LSB) -->
    <circle cx="375" cy="525" r="14" fill="#10b981" stroke="#86efac" stroke-width="2"/>
    <text x="367" y="530" fill="#ffffff" font-size="11" font-weight="bold">D0</text>
    <text x="405" y="522" fill="#10b981" font-size="11" font-weight="bold">LED 0 (LSB, 2⁰ = 1)</text>
    <text x="405" y="537" fill="#94a3b8" font-size="9">From Pin 3 (B0) via 330Ω</text>

    <!-- MAGNETIC LEVITATION BANNER IN BOX -->
    <rect x="25" y="580" width="535" height="175" rx="6" fill="#0f172a" stroke="#eab308" stroke-width="1.5"/>
    <rect x="25" y="580" width="535" height="26" rx="6" fill="#ca8a04"/>
    <text x="35" y="598" fill="#ffffff" font-size="11" font-weight="bold">MEMBER 3 &amp; 4: MAGNETIC SUSPENSION &amp; PACKAGING INTEGRATION</text>
    <text x="40" y="625" fill="#facc15" font-size="10" font-weight="bold">• Earnshaw's Theorem Resolution:</text>
    <text x="50" y="642" fill="#cbd5e1" font-size="9">Passive N52 Neodymium Ring Magnets arranged in vertical repulsion (North to North).</text>
    <text x="50" y="658" fill="#cbd5e1" font-size="9">Radial Earnshaw instability bypassed using a central polished acrylic guide rod &amp; low-friction PTFE bushing.</text>
    
    <text x="40" y="680" fill="#facc15" font-size="10" font-weight="bold">• Magnetic Isolation &amp; Noise Protection:</text>
    <text x="50" y="697" fill="#cbd5e1" font-size="9">Optical triangulation sensor (Sharp GP2Y0A21YK0F) is placed &gt;15cm away from base magnets (zero magnetic interference).</text>
    <text x="50" y="713" fill="#cbd5e1" font-size="9">Lightweight PLA 3D printed housing ensures buoyant magnetic suspension without exceeding magnetic lift limit.</text>
    <text x="50" y="730" fill="#cbd5e1" font-size="9">Local bypass network (10kΩ series + 1µF low-pass) prevents threshold jitter and LED chattering.</text>
  </g>
</svg>
"""
    with open("circuits/schematic_diagram.svg", "w") as f:
        f.write(svg)
    print("Generated circuits/schematic_diagram.svg successfully!")

if __name__ == "__main__":
    generate_schematic_svg()
