# 🚨 Crowd Sentinel AI

> AI-powered real-time crowd monitoring and risk prediction system to prevent overcrowding and stampedes.

---

## 🧠 Overview

**Crowd Sentinel AI** is a smart surveillance system that uses **Computer Vision + Machine Learning** to:

* Detect crowd density in real time
* Generate heatmaps of high-risk zones
* Predict dangerous crowd situations
* Send alerts to authorities

🚀 Built for **smart cities, public safety, and large-scale event management**

---

## 🎯 Problem Statement

Managing large crowds in places like:

* Festivals (Kumbh Mela 🎪)
* Stadiums 🏟️
* रेलवे स्टेशन 🚉

is challenging and often **reactive**.

❌ Traditional CCTV systems only monitor
✅ Crowd Sentinel AI predicts and prevents

---

## ⚙️ Features

### 🔍 Real-time Crowd Detection

* Detect people using AI (YOLO)
* Count individuals in live video feed

### 🔥 Crowd Density Heatmaps

* Visual representation of crowded zones
* Red = High risk, Green = Safe

### ⚡ AI Risk Prediction

* Predict overcrowding situations
* Detect abnormal movement patterns

### 📊 Admin Dashboard

* Live video feed
* Analytics & charts
* Crowd trends

### 🚨 Smart Alerts

* Threshold-based alerts
* Notification system (SMS / App)

### 🧪 Simulation Mode *(Advanced)*

* Crowd movement simulation
* Emergency evacuation planning

---

## 🏗️ System Architecture

```bash
Camera Feed
   ↓
AI Detection Model (YOLOv8)
   ↓
Crowd Density Analyzer
   ↓
Prediction Model (ML)
   ↓
Backend API (FastAPI / Node.js)
   ↓
Frontend Dashboard (React / Next.js)
   ↓
Alerts & Notifications
```

---

## 🛠️ Tech Stack

### 👁️ AI / ML

* YOLOv8 / YOLOv5
* OpenCV
* PyTorch / TensorFlow

### ⚙️ Backend

* FastAPI / Node.js
* WebSockets

### 📊 Frontend

* React / Next.js
* Tailwind CSS
* Chart.js / Recharts

### 🗄️ Database

* MongoDB / PostgreSQL

### ☁️ Deployment

* AWS / Firebase / Vercel

---

## 📂 Project Structure

```bash
crowd-sentinel-ai/
│
├── backend/
│   ├── api/
│   ├── models/
│   └── services/
│
├── ai-model/
│   ├── detection/
│   ├── training/
│   └── utils/
│
├── frontend/
│   ├── components/
│   ├── pages/
│   └── charts/
│
├── data/
└── README.md
```

---

## 🚀 Getting Started

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/crowd-sentinel-ai.git
cd crowd-sentinel-ai
```

### 2️⃣ Setup Backend

```bash
cd backend
pip install -r requirements.txt
uvicorn main:app --reload
```

### 3️⃣ Setup Frontend

```bash
cd frontend
npm install
npm run dev
```

---

## 🧪 Demo Workflow

1. Upload or stream video feed
2. AI detects people in frames
3. System calculates crowd density
4. Heatmap is generated
5. Risk prediction model evaluates danger
6. Alerts triggered if threshold exceeded

---

## 📈 Future Improvements

* 📱 Mobile app for authorities
* 🌍 GIS map integration
* 🛰️ Drone-based monitoring
* 🧠 Reinforcement learning for better prediction

---

## 🧑‍💻 Contributors

* Your Name
* Team Members

---

## 📄 License

This project is licensed under the MIT License.

---

## ⭐ Support

If you like this project, give it a ⭐ on GitHub!

---

## 🤝 Acknowledgements

* OpenCV
* YOLO
* PyTorch
* Open-source community ❤️

---
##  Team 
Apex Dynamics 
