# 515proj
# 515 Final Project

This project uses an Arduino-compatible board to collect and display sensor data in real-time. It reads motion and orientation data from an IMU (ICM-20948) and displays key information on an OLED screen.

---

## 🛠 Preparation

### Required Components
- **Seeed Studio XIAO ESP32-C3**
- **IMU sensor**: ICM-20948
- **OLED Display**: SSD1306

<p align="center">
  <img src="./circuit_image.png" alt="Circuit Diagram" width="500"/>
</p>

---

## 🚀 How to Run the Code

### 1. Open the `.ino` file in Arduino IDE
- Launch Arduino IDE  
- Go to `File > Open...` and select [`515_sensor_code.ino`](./515_sensor_code.ino)

### 2. Install Required Libraries  
Go to `Tools > Manage Libraries...`, then install the following:
- `Adafruit ICM20948` or `ICM20948_WE`
- `Adafruit SSD1306` or `Adafruit SSD1331` (depending on your OLED)
- `Adafruit GFX Library`
- `Wire`

### 3. Set Your Board & Port  
- Go to `Tools > Board > Select your board` (e.g., **"Seeed XIAO ESP32C3"**)  
- Go to `Tools > Port > Select the correct COM port`

### 4. Upload the Code  
Click the ✅ **Upload** button to flash the code to your board.

---

## 🖥️ What You Should See

The OLED screen will display real-time sensor data, such as:
- Acceleration
- Gyroscope readings
- Temperature

Data refreshes continuously.
