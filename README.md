# LiftWell: Real-Time Pose Feedback System

This project is a real-time human motion classification and feedback system designed to assist users during strength training exercises like deadlifts and shoulder presses. It builds on embedded sensor data and adds webcam-based pose classification, providing users with immediate feedback on form accuracy.

## 🧠 Key Features

- **IMU Sensor-Based Tracking**  
  Collects motion data from a 9-DoF IMU sensor (ICM20948) mounted on the body for initial gesture classification.

- **Webcam-Based Pose Classification**  
  Using `MediaPipe` and a trained ML model, the system captures keypoints from webcam video to identify and classify movements in real time.

- **Custom Real-Time Interface**  
  Replaces OLED hardware display with a Python-based desktop interface to show feedback, predictions, and system status.

### 📁 Project Structure

```text
515proj/
├── 515_sensor_code.ino             # Arduino code for ICM20948 sensor
├── breadboard.png                  # Circuit diagram for sensor wiring
├── collect_pose_data_deadlift.py  # Script to capture deadlift pose data via webcam
├── realtime_shoulderpress.py      # Real-time classification using webcam
├── train_classifier_shoulderlift.py  # ML training script for shoulder press
├── pose_classifier.pkl            # Trained ML model
├── final_data/                    # Dataset used for training
├── 515_final enclosure.stl        # Enclosure design for sensor hardware
└── README.md                      # You are here
```



### 🖥️ Software Dependencies

- Python 3.8+
- OpenCV
- MediaPipe
- scikit-learn
- PySerial (for sensor communication)

To install dependencies:

```bash
pip install -r requirements.txt
```

---

### 🚀 How to Run

#### 1. Sensor Mode (Arduino + IMU)

- Flash `515_sensor_code.ino` to your XIAO ESP32-C3 (or equivalent)
- Connect IMU sensor as per `breadboard.png`
- Stream serial data to your Python script *(optional, for legacy use)*

#### 2. Camera Mode (Webcam)

- Run `collect_pose_data_deadlift.py` to collect your own keypoint data
- Train your model via `train_classifier_shoulderlift.py`
- Start real-time classification:

```bash
python realtime_shoulderpress.py
```

---

### ✅ Use Cases

- Gym form tracking  
- At-home workout correction  
- Personal fitness analytics  

---

### 🔧 Hardware Used

- Seeed Studio XIAO ESP32-C3  
- ICM20948 9-DoF IMU sensor  
- Laptop webcam  
- Custom 3D-printed enclosure (`515_final enclosure.stl`)

