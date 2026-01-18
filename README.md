# 🐄 Deteksi Dini Penyakit Mata *Pink Eye* pada Sapi
### **Berbasis Citra Digital Menggunakan YOLOv4-Tiny**

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Framework-Flask-lightgrey.svg)](https://flask.palletsprojects.com/)
[![YOLOv4-Tiny](https://img.shields.io/badge/Model-YOLOv4--Tiny-green.svg)](https://github.com/AlexeyAB/darknet)
[![License](https://img.shields.io/badge/License-Academic-orange.svg)](#)

This web application is an early detection system for Pink Eye disease (Infectious Bovine Keratoconjunctivitis) in cattle. Developed as an Undergraduate Thesis Project, this system leverages Artificial Intelligence (AI) technology to assist farmers in monitoring cattle eye health in a fast, automated, and accurate manner through digital image analysis.

---

## 📌 Background
**Pink Eye** is a contagious eye infection commonly affecting cattle. The impacts of this disease include:
* **Decreased Productivity:** Weight loss due to pain while eating.
* **Visual Impairment:** Risk of permanent blindness if not treated promptly.
* **Economic Losses:** High treatment costs for the livestock industry.

This system is proposed as a Computer Vision–based solution to objectively detect early symptoms without requiring direct involvement of experts at the initial stage.

---

## 🎯 System Objectives
1. **Automation:** Replace manual visual inspection with an AI-based system.
2. **Speed:** Deliver detection results within seconds.
3. **Accessibility:** Provide ease of use through a simple and responsive web interface.

---

## 🧠 Methodology & Technology

### **Detection Method**
* **Algorithm:** YOLOv4-Tiny.
* **Inference Engine:** OpenCV DNN (Deep Neural Networks).
* **Pipeline:** Pre-processing → Object Detection → Non-Maximum Suppression (NMS) → Visual Output.

### **Tech Stack**
* **Backend:** Python, Flask
* **AI/CV:** OpenCV, NumPy, Pillow
* **Frontend:** HTML5, Tailwind CSS

---

## 📂 Struktur Folder Project
```text
project-root/
├── app.py              # Main Flask logic and AI inference
├── configs/            # Model configuration files (.cfg)
├── weights/            # Model weight files (.weights) - *Must be added manually*
├── fonts/              # Fonts for detection labels
├── static/             # Image storage directory (Input/Output)
├── templates/          # HTML templates (index.html, etc.)
├── coco.names          # Class label list
└── README.md           # Project documentation
```
---

## ⚙️ Detection Parameters Explanation
This application allows users to configure two main parameters to optimize detection results:

**Confidence Threshold:** The minimum confidence score required for a detection to be displayed.
Example: If set to 0.5, the system will only display objects with confidence scores above 50%.

**NMS (Non-Maximum Suppression) Threshold:** Used to eliminate overlapping bounding boxes.
Lower values result in stricter suppression of duplicate boxes for the same object.
---

## 🚀 How to Run the Application
Method 1: Local Installation
Clone Repositori:
```git clone [https://github.com/fachriramdhan/project-pink-eye.git](https://github.com/username/project-pink-eye.git)
cd project-pink-eye
```

Install Dependencies:
```
pip install flask opencv-python pillow numpy
```

Prepare the Model: Ensure the .weights file is placed inside the weights/.
Run the app:
```
python app.py
```

Access the application via your browser at: http://localhost:5000

Method 2: Using Docker
To run the application in an isolated environment:
Build Image:
```
docker build -t pinkeye-detection .
```

Run Container:
```
docker run -p 5000:5000 pinkeye-detection
```

---

## 🔄 System Workflow
The detection process follows these stages:

1. **Upload:** Users upload an image of a cow’s eye through the web interface.
2. **Processing:** The system performs preprocessing and image inference using OpenCV DNN with the YOLOv4-Tiny architecture.
3. **Filtering:** Raw detections are filtered using Confidence Score and Non-Maximum Suppression (NMS).
4. **Result:** The system displays the output image with bounding boxes, confidence labels, and inference time information.

## 🎓 Academic Notes
This project was developed as part of an undergraduate thesis research. The main focus is the implementation of lightweight Deep Learning models, enabling high-performance and accurate object detection on devices with low-to-medium computational resources, without relying on high-end GPUs.

## 📄 License & Contribution
This project is open-source and intended for educational and scientific development purposes.
If you use or extend this code for academic research, please provide proper attribution or citation to this repository.

Author: [Fachri Ramdhan]
