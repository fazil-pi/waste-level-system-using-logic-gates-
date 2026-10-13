# Falstad Interactive Simulation & Video Recording Guide

This directory contains the simulation file for the **4-Bit Flash ADC Smart Garbage Bin Level Indicator**.

---

## 1. Quick Launch (In-Browser Simulation)

You can run this interactive simulation directly in any modern web browser without installing software:

1. Open **[Falstad Circuit Simulator](https://www.falstad.com/circuit/)**.
2. Click **File** $\rightarrow$ **Open File...** (or **File** $\rightarrow$ **Import From Text**).
3. Copy and paste the contents of [`falstad_circuit.txt`](./falstad_circuit.txt) into the dialog and click **OK**.
4. The simulation will immediately start running with animated current flow and real-time voltage monitoring.

---

## 2. Interactive Testing & Verification

1. Locate the **Sensor Voltage Slider** on the right/bottom panel (labeled `Sensor_Slider_(0.4V-2.8V)`).
2. **Empty Bin ($0.40\text{V}$):** All 4 LEDs are OFF (`0000`).
3. Slowly drag the slider upward:
   * At $\approx 0.56\text{V}$ (Level 1), **LED0** lights up (`0001`).
   * At $\approx 0.72\text{V}$ (Level 2), **LED1** lights up and LED0 turns off (`0010`).
   * At $\approx 1.68\text{V}$ (Level 8), **LED3** lights up (`1000`).
   * At $\approx 2.80\text{V}$ (Level 15 / Bin 100% Full), all 4 LEDs light up (`1111`).
4. Watch the priority encoders dynamically switch control: when the input crosses Level 8, U1 asserts its group select line $\overline{GS}$ and disables U2 via $\overline{EO}$, instantly turning on the MSB LED ($B_3$).

---

## 3. How to Record the Simulation Video

To create the project demo video for presentations or submissions:

### Option A: Using Built-in Screen Recorders (Free & Fast)
* **Windows:** Press `Windows Key + Alt + R` (Xbox Game Bar Screen Recorder).
* **macOS:** Press `Cmd + Shift + 5`, select the browser window, and click **Record**.
* **Linux (Ubuntu/GNOME):** Press `Ctrl + Alt + Shift + R` or `Print Screen` $\rightarrow$ Screen Record mode.

### Option B: Using OBS Studio (High Quality)
1. Open [OBS Studio](https://obsproject.com/).
2. Add a **Window Capture** source and select your browser running Falstad.
3. Start recording.
4. Smoothly drag the slider from $0.40\text{V}$ to $2.80\text{V}$ over 15–20 seconds to show the 4 LEDs counting in binary from `0000` to `1111`.
5. Drag it back down to demonstrate descending level detection.
6. Stop recording and export your `.mp4` video.
