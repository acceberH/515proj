# 515proj
# 515 Final Project

This project uses an Arduino-compatible board to collect and display sensor data in real-time. It reads motion and orientation data from an IMU (ICM-20948) and displays key information on an OLED screen.

---

## Preparation

- Seeed Studio XIAO ESP32-C3
- IMU sensor (ICM-20948)
- OLED Display (SSD1306)

2. Open the .ino file in Arduino IDE:
Launch Arduino IDE

Go to File > Open... and select 515_sensor_code.ino

3. Install Required Libraries:
In the Arduino IDE, go to Tools > Manage Libraries... and install:

Adafruit ICM20948 or ICM20948_WE

Adafruit SSD1306 or Adafruit SSD1331 (depending on your OLED)

Adafruit GFX Library

Wire

4. Set Your Board & Port:
Tools > Board > Select your board (e.g., "Seeed XIAO ESP32C3")

Tools > Port > Select the correct COM port

5. Upload the Code:
Click the ✅✔️ Upload button to flash the code onto your board.

🖥️ What You Should See
The OLED screen will display real-time sensor data (e.g., acceleration, gyro, temperature)

Data refreshes continuously
