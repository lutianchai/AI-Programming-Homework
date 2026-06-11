from flask import Flask, jsonify, send_from_directory
from ultralytics import YOLO
import os
import cv2

app = Flask(__name__, static_folder='static')

# 初始化YOLO模型
model_path = "yolov8n.pt"
if not os.path.exists(model_path):
    print("请确保 yolov8n.pt 在项目根目录")
model = YOLO(model_path)

@app.route("/")
def home():
    return send_from_directory('static', 'index.html')

@app.route("/detect")
def detect():
    """
    使用本地图片模拟摄像头抓取，返回识别结果和动作指令
    """
    img_path = os.path.expanduser("~/Desktop/phone.png")
    if not os.path.exists(img_path):
        return jsonify({"objects": ["请先把 phone.png 放到桌面"], "action": "idle", "image": ""})

    results = model(img_path)
    objects = []
    for box in results[0].boxes:
        cls = int(box.cls)
        name = results[0].names[cls]
        objects.append(name)

    # 动作决策
    action = "idle"
    if "cell phone" in objects:
        action = "grab_phone"
    elif "bottle" in objects:
        action = "grab_bottle"
    elif "cup" in objects:
        action = "grab_cup"

    # 标注图片
    img = cv2.imread(img_path)
    for box in results[0].boxes.xyxy:
        x1, y1, x2, y2 = map(int, box)
        cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
    output_path = os.path.join("static", "output.png")
    cv2.imwrite(output_path, img)

    return jsonify({
        "objects": objects,
        "action": action,
        "image": "output.png"
    })

@app.route('/<path:path>')
def serve_static(path):
    return send_from_directory('static', path)

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)