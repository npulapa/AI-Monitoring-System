# 🤖 AI Monitoring System

## 📌 Project Overview
This project is a basic AI-based monitoring system developed as part of the internship task.  
It demonstrates the use of Computer Vision, Object Detection, Backend APIs, and AI Evaluation.

---

## 🚀 Features

### 👀 1. Face Detection (OpenCV)
- Detects human face using webcam
- Displays bounding box around face
- Detects when face is not present

---

### 🤖 2. Object Detection (YOLOv8)
- Detects objects like person, phone, etc.
- Counts number of people in frame
- Real-time detection using webcam

---

### 🌐 3. Backend API (FastAPI)
- `/test` endpoint → checks API working
- `/submit` endpoint → accepts JSON data
- Returns structured response

---

### 🧠 4. AI Evaluation System (LLM Simulation)
- Takes user answer as input
- Compares with correct answer
- Returns:
  - ✅ correct
  - ❌ wrong

---

## 🛠️ Technologies Used
- Python
- OpenCV
- YOLOv8 (Ultralytics)
- FastAPI
- Uvicorn

---

## ▶️ How to Run

### 1. Install Dependencies
```bash
pip install -r requirements.txt

### 2. Run Face Detection
```bash
python face_detection.py

### 3. Run YOLO Detection
```bash
python yolo_detection.py

### 4. Run FastAPI Server
```bash
uvicorn main:app --reload

Open in browser:

http://127.0.0.1:8000/test
http://127.0.0.1:8000/docs

### 5. Run Evaluation System
```bash
python evaluation.py


## 📸 Output Screenshots
