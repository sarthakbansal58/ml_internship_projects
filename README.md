#  ML Internship Projects

This repository contains all the projects completed during my Machine Learning & Full Stack Development internship. Each project focuses on solving a real-world problem using modern technologies such as Python, Streamlit, MERN Stack, Computer Vision, and Generative AI.

---

## 📂 Projects

### 1️ AI Story Generator

An AI-powered web application that generates engaging stories based on user inputs such as genre, theme, characters, and story length. The application also allows users to export stories as PDF files and convert them into speech.

####  Features

* Generate AI-powered stories
* Multiple story genres
* Adjustable story length
* PDF export
* Text-to-Speech support
* Clean Streamlit interface

####  Technologies Used

* Python
* Streamlit
* Google Gemini API
* LangChain
* gTTS
* FPDF

#### 📁 Project Structure

```text
story_gen_app/
│
├── app.py
├── chains/
├── prompts/
├── utils/
├── requirements.txt
└── README.md
```

---

### 2️ AI Sign Language Predictor

A real-time sign language recognition system that detects hand landmarks using MediaPipe and predicts sign language gestures using a trained Machine Learning model.

####  Features

* Real-time webcam detection
* MediaPipe hand landmark extraction
* Machine Learning gesture prediction
* Easy dataset expansion
* Custom vocabulary training
* Fast inference

#### 🛠️ Technologies Used

* Python
* OpenCV
* MediaPipe
* Scikit-learn
* Pandas
* NumPy
* Pickle

#### Machine Learning Workflow

```
Collect Images
       │
       ▼
Extract Hand Landmarks
       │
       ▼
Create coords.csv
       │
       ▼
Train Classification Model
       │
       ▼
Save body_language.pkl
       │
       ▼
Real-Time Prediction
```

#### 📁 Project Structure

```text
sign_language_predictor/
│
├── ai_action_predictor/
├── data/
├── models/
├── scripts/
├── coords.csv
├── body_language.pkl
└── README.md
```

---

# 🛠 Installation

Clone the repository:

```bash
git clone https://github.com/sarthakbansal58/ml_internship_projects.git
```

Move into the repository:

```bash
cd ml_internship_projects
```

---

## Run AI Story Generator

```bash
cd story_gen_app

pip install -r requirements.txt

streamlit run app.py
```

---

##  Run Sign Language Predictor

```bash
cd sign_language_predictor

pip install -r requirements.txt

 contains the logic.ipynb to run refer readme.md of that folder
```

> Ensure your webcam is connected before running the Sign Language Predictor.

---

# Skills Demonstrated

* Machine Learning
* Computer Vision
* Generative AI
* Prompt Engineering
* Streamlit Development
* OpenCV
* MediaPipe
* LangChain
* Python Development
* API Integration

---

# Author

**Sarthak Bansal**

GitHub: https://github.com/sarthakbansal58

---

## ⭐ If you found these projects useful, consider giving this repository a star!
