# AFDA-WEB

## 🌟 Project Overview
AFDA-WEB is an innovative AI-powered web application designed to assist in the early detection of Alzheimer's Disease through audio analysis.
Using **TensorFlow**, **FastAPI**, and **Docker**, this project enables users to upload 4-second audio clips for analysis,
providing a prediction based on our deep learning model, which achieves **78% validation accuracy**.
The Repo for the model is the next one:
[![GitHub Repo](https://img.shields.io/badge/GitHub-Repository-blue?style=for-the-badge&logo=github)](https://github.com/HanamDavid/AFDA)


## 🛠️ Tech Stack
- **Machine Learning**: TensorFlow for deep learning model
- **Backend**: FastAPI for API development
- **Frontend**: Bootstrap for responsive UI
- **Containerization**: Docker for seamless deployment

## 🚀 Features
✅ Upload and analyze short audio recordings 🎙️
✅ AI-powered Alzheimer’s prediction 🤖
✅ User-friendly web interface with Bootstrap ✨
✅ Fully containerized using Docker 🐳

## 📂 Project Structure
```
├── backend
│   ├── Dockerfile
│   ├── main.py
│   ├── model.py
│   ├── models
│   │   └── audio_classification.keras
│   ├── requirements.txt
│   └── temp
│       ├── <uploaded_audio_files>
├── docker-compose.yml
├── frontend
│   ├── css
│   │   └── styles.css
│   ├── Dockerfile
│   ├── images
│   │   └── AFDA_Logo.png
│   ├── index.html
│   └── js
│       └── app.js
└── README.md
```

## 🏗️ Installation & Usage
### 🔧 Prerequisites
Ensure you have **Docker** and **Docker Compose** installed.

### 📦 Setup & Run
```bash
git clone https://github.com/HanamDavid/AFDA-WEB
cd AFDA-WEB
docker-compose up --build
```
Then, access the web interface at **http://localhost:8000**


## 📜 License
This project is licensed under the **MIT License**.

---

🌟 _Contributions are welcome! Feel free to fork, improve, and submit PRs._ 🛠️💡


