import os
import joblib
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report

# ==== 配置路径 ====
base_path = '/Users/wangxinyu/Downloads/final_data/pose_data'
label_folders = {
    'good': 'deadlift_good',
    'wideleg': 'deadlift_wideleg',
    'shoulderpress': 'shoulderpress',
    'shoulderpress_bad1': 'shoulderpress_bad1',
    'flyes': 'flyes',
    'flyes_bad': 'flyes_bad'
}

# ==== 加载数据函数 ====
def load_labeled_data(folder_path, label):
    dfs = []
    for fname in os.listdir(folder_path):
        if fname.endswith('.csv'):
            path = os.path.join(folder_path, fname)
            try:
                df = pd.read_csv(path, encoding='ISO-8859-1')
                df['label'] = label
                dfs.append(df)
            except Exception as e:
                print(f"❗Skipped: {path} ({e})")
    return dfs

# ==== 加载所有数据 ====
all_dfs = []
for label, folder_name in label_folders.items():
    folder_path = os.path.join(base_path, folder_name)
    all_dfs.extend(load_labeled_data(folder_path, label))

# ==== 合并与清洗 ====
all_data = pd.concat(all_dfs, ignore_index=True)
all_data = all_data.drop(columns=[col for col in all_data.columns if 'Unnamed' in col], errors='ignore')

# ==== 特征 / 标签 ====
X = all_data.drop(columns=['label', 'timestamp'], errors='ignore')
y = all_data['label']

# ==== 划分训练集 / 测试集 ====
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

# ==== 训练模型 ====
clf = RandomForestClassifier(n_estimators=100, random_state=42)
clf.fit(X_train, y_train)

# ==== 输出评估 ====
y_pred = clf.predict(X_test)
print("\n📊 分类报告:")
print(classification_report(y_test, y_pred))

# ==== 保存模型 ====
model_path = os.path.join(base_path, 'pose_classifier.pkl')
joblib.dump(clf, model_path)
print(f"\n✅ 模型已保存至：{model_path}")
