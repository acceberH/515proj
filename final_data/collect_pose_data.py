import cv2
import mediapipe as mp
import csv
import os
from datetime import datetime

# ===== 可自定義參數 =====
LABEL = "deadlift"           # 動作名稱
PERSON = "user1"          # 使用者名稱
SAVE_DIR = "pose_data"    # 輸出資料夾
FRAMES_TO_COLLECT = 50    # 每段動作要錄幾幀
INTERVAL_MS = 100         # 幀率對應時間間隔（ms）→ 10Hz = 100ms

# 初始化 MediaPipe Pose
mp_pose = mp.solutions.pose
pose = mp_pose.Pose(static_image_mode=False, min_detection_confidence=0.5)
mp_drawing = mp.solutions.drawing_utils

# 創建輸出資料夾
os.makedirs(SAVE_DIR, exist_ok=True)

# 啟用攝像頭
cap = cv2.VideoCapture(0)
frame_count = 0
data = []

print(f"開始錄製 {LABEL} 的動作，請做好準備...（按 's' 開始，'q' 離開）")

recording = False

while True:
    ret, frame = cap.read()
    if not ret:
        break
    image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = pose.process(image)

    # 顯示骨架
    annotated = frame.copy()
    if results.pose_landmarks:
        mp_drawing.draw_landmarks(annotated, results.pose_landmarks, mp_pose.POSE_CONNECTIONS)

    cv2.putText(annotated, f"Recording: {'Yes' if recording else 'No'}", (10, 30),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255) if recording else (255, 255, 255), 2)
    cv2.imshow("Pose Capture", annotated)

    key = cv2.waitKey(1)
    if key == ord('s'):
        print("開始錄製...")
        recording = True
        frame_count = 0
        data = []
    elif key == ord('q'):
        break

    if recording and results.pose_landmarks:
        # 建立單幀資料（含 timestamp）
        row = [frame_count * INTERVAL_MS]
        for lm in results.pose_landmarks.landmark:
            row.extend([lm.x, lm.y, lm.z, lm.visibility])
        data.append(row)
        frame_count += 1

        # 錄滿指定幀數就儲存
        if frame_count >= FRAMES_TO_COLLECT:
            timestamp_str = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"{LABEL}_{PERSON}_{timestamp_str}.csv"
            filepath = os.path.join(SAVE_DIR, filename)

            with open(filepath, 'w', newline='') as f:
                writer = csv.writer(f)
                header = ['timestamp']
                for i in range(33):
                    header.extend([f"{i}_x", f"{i}_y", f"{i}_z", f"{i}_v"])
                writer.writerow(header)
                writer.writerows(data)

            print(f"✅ 錄製完成！已保存至 {filepath}")
            recording = False

cap.release()
cv2.destroyAllWindows()
