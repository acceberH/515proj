from flask import Flask, request, jsonify
from flask_cors import CORS
import joblib
import numpy as np

app = Flask(__name__)
CORS(app)

MODEL_PATH = 'pose_classifier.pkl'
LABEL_MAP = {
    'good': 'Deadlift: Correct',
    'wideleg': 'Deadlift: Legs Too Wide',
    'shoulderpress': 'Shoulder Press: Correct',
    'shoulderpress_bad1': 'Shoulder Press: Incorrect Form',
    'flyes': 'Flyes: Correct',
    'flyes_bad': 'Flyes: Incorrect Arm Position'
}

clf = joblib.load(MODEL_PATH)

# Store latest IMU data in memory
global_imu_data = {
    'accel': [0, 0, 0],
    'gyro': [0, 0, 0],
    'temp': 0.0
}

@app.route('/classify', methods=['POST'])
def classify():
    data = request.json
    keypoints = np.array(data['keypoints']).reshape(1, -1)
    label = clf.predict(keypoints)[0]
    feedback = LABEL_MAP.get(label, f"类别: {label}")
    return jsonify({'result': feedback})

@app.route('/imu-data', methods=['POST'])
def imu_data():
    data = request.json
    print('Received IMU:', data)  # Debug print to verify incoming data
    # Expecting keys: accel, gyro, temp
    global global_imu_data
    global_imu_data = {
        'accel': data.get('accel', [0, 0, 0]),
        'gyro': data.get('gyro', [0, 0, 0]),
        'temp': data.get('temp', 0.0)
    }
    return jsonify({'status': 'ok'})

@app.route('/imu-latest', methods=['GET'])
def imu_latest():
    return jsonify(global_imu_data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5051) 