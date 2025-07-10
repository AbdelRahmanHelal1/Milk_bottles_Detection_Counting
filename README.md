# 🍼 Milk Bottles Detection & Counting using YOLOv8

This project uses **YOLOv8 object detection** to detect and count milk bottles as they pass through a predefined line in a video stream. It’s designed for real-time applications like monitoring production lines in factories.

![YOLOv8](https://img.shields.io/badge/YOLOv8-Bottle--Detection-green)
![Python](https://img.shields.io/badge/Python-3.10+-yellow)
![OpenCV](https://img.shields.io/badge/OpenCV-RealTime-blue)

---

## 🎯 Features

- ✅ Real-time detection of milk bottles using YOLOv8
- ✅ Counts bottles as they cross a virtual line
- ✅ Displays counter and tracking visuals on screen
- ✅ Easy to customize for other object types or directions

---

## 📽️ Demo

> A red dot is drawn at the center of each bottle. When the bottle crosses the blue line, the counter increases.

https://www.linkedin.com/posts/abdul-rahman-helal-3630a4259_computerabrvision-automation-ai-activity-7163211659937759233-FeT_?utm_source=share&utm_medium=member_android

---

## 🧠 How It Works

1. Loads YOLOv8 model (`yolov8n.pt`)
2. Processes each frame from a video file
3. Detects objects and extracts bounding boxes and classes
4. Filters for "bottles" class only
5. Draws a line (x=150) and checks if the object’s center passes it
6. If yes, counter is incremented

---

## 📦 Installation

### 1. Clone the Repository

```bash
-> git clone https://github.com/AbdelRahmanHelal1/Milk_bottles_Detection_Counting.git
-> cd Milk_bottles_Detection_Counting
```

# 2. Install Requirements
```
-> pip install -r requirements.txt
```

▶️ Run the Script
Make sure Milk2.mp4 is in the same directory or edit the path.

Run:

``` 
-> python Milk Counting.py

```
# 📂 File Structure

Milk_bottles_Detection_Counting/

├──  Milk Counting.py        # Main detection & counting script

├── Milk2.mp4                 # Sample video input

├── requirements.txt          # Project dependencies

└── README.md                 # This file

# 🔧 Customize
To change the detection class, edit the names dictionary:

```
names = {39: "bottles"}  # Use correct class ID from YOLO model
```
# To adjust the counting line position:

```
line = cv2.line(frame, (150, 170), (150, 280), (255, 0, 0), 3)
```

👨‍💻 Author
Abdelrahman Helal

🎓 Faculty of Artificial Intelligence – Menoufia University

💼 Computer Vision & AI Developer

