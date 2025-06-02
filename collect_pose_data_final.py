import cv2
import mediapipe as mp
import csv
import os
from datetime import datetime

# ===== 自定义参数（每次录制前输入） =====
LABEL = input("请输入动作标签（如 deadlift_good / deadlift_bad_back / deadlift_bad_knee）：").strip()
PERSON = input("请输入使用者编号（如 user5）：").strip()
SAVE_DIR = f"pose_data/{LABEL}"  # 分类保存到子目录中
FRAMES_TO_COLLECT = 50    # 每组动作录制多少帧
INTERVAL_MS = 100         # 幀率对应的时间间隔（ms）→ 10Hz = 100ms

# 初始化 MediaPipe Pose
mp_pose = mp.solutions.pose
pose = mp_pose.Pose(static_image_mode=False, min_detection_confidence=0.5)
mp_drawing = mp.solutions.drawing_utils

# 创建保存目录
os.makedirs(SAVE_DIR, exist_ok=True)

# 打开摄像头
cap = cv2.VideoCapture(0)
frame_count = 0
data = []

print(f"\n🟡 准备采集 [{LABEL}] 的动作数据，按 's' 开始，'q' 退出。\n")

recording = False

while True:
    ret, frame = cap.read()
    if not ret:
        break
    image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = pose.process(image)

    # 显示骨架
    annotated = frame.copy()
    if results.pose_landmarks:
        mp_drawing.draw_landmarks(annotated, results.pose_landmarks, mp_pose.POSE_CONNECTIONS)

    cv2.putText(annotated, f"Recording: {'Yes' if recording else 'No'}", (10, 30),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255) if recording else (255, 255, 255), 2)
    cv2.imshow("Pose Capture", annotated)

    key = cv2.waitKey(1)
    if key == ord('s'):
        print("▶️ 开始录制...")
        recording = True
        frame_count = 0
        data = []
    elif key == ord('q'):
        print("⏹ 退出程序。")
        break

    if recording and results.pose_landmarks:
        row = [frame_count * INTERVAL_MS]
        for lm in results.pose_landmarks.landmark:
            row.extend([lm.x, lm.y, lm.z, lm.visibility])
        data.append(row)
        frame_count += 1

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

            print(f"✅ 录制完成：{filepath}\n")
            recording = False

cap.release()
cv2.destroyAllWindows()
