# 🍕 AI Food Classification API & Dashboard

![Python](https://img.shields.io/badge/Python-3.11-blue.svg?style=for-the-badge&logo=python)
![TensorFlow](https://img.shields.io/badge/TensorFlow-2.x-orange.svg?style=for-the-badge&logo=tensorflow)
![Flask](https://img.shields.io/badge/Flask-REST_API-green.svg?style=for-the-badge&logo=flask)
![SQLite](https://img.shields.io/badge/SQLite-Database-lightgrey.svg?style=for-the-badge&logo=sqlite)
![Docker](https://img.shields.io/badge/Docker-Containerized-blue.svg?style=for-the-badge&logo=docker)

## 📖 Project Overview
I built this project to learn how machine learning models can be integrated into a real web application.

The application allows users to upload an image of food, runs it through a deep learning model, and returns a prediction in real time. Each prediction is also stored in a database so it can be viewed later through a simple dashboard.

While building this project, I focused on connecting the ML model, backend API, database, and frontend interface into a single working system.

## ⚙️ What This Project Does
* Upload an image of food
* Run inference using a deep learning model
* Return the predicted label
* Store prediction history in a database
* Display previous predictions in a dashboard

## 🧠 How It Works
1. A user uploads an image from the web interface.
2. The Flask backend receives the image through the `/predict` API.
3. The image is preprocessed and passed to a MobileNetV2 model.
4. The model returns the predicted label.
5. The result is saved in a SQLite database.
6. The frontend displays the prediction instantly.

## 🔧 Features I Implemented
* **REST API Backend:** I built a Flask API endpoint that processes uploaded images and returns predictions.
* **Machine Learning Inference:** The app uses TensorFlow 2 and MobileNetV2 to classify food images.
* **Prediction Logging:** Every prediction is saved in SQLite with the filename and timestamp.
* **History Dashboard:** A `/history` page displays all previous predictions.
* **Safe File Handling:** The app validates uploads and deletes temporary files after processing.

## 🛠️ Tech Stack
* **Backend:** Python, Flask, Werkzeug
* **Machine Learning:** TensorFlow 2.x, Keras, MobileNetV2 (ImageNet weights), NumPy, Pillow
* **Database:** SQLite3
* **Frontend:** HTML5, CSS3, Bootstrap 5, Vanilla JS (Fetch API)
* **DevOps:** Docker

## 📌 Future Improvements
* Add confidence scores for predictions
* Improve UI feedback
* Deploy to cloud
* Fine-tune model on a specific food dataset

## 🚀 How to Run Locally

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/zeuspavilion/AI-Food-Classifier.git](https://github.com/zeuspavilion/AI-Food-Classifier.git)
   cd AI-Food-Classifier
   
   Create a virtual environment & install dependencies:
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   pip install -r requirements.txt

2. **Run the Application:**
   ```bash
   python Food_app.py
   
3. **Access the App:**
Open your browser and navigate to http://127.0.0.1:5000

🐳 How to Run with Docker
This application is fully containerized. If you have Docker installed, you can run it instantly without configuring a local Python environment.

# Build the image
   ```bash
docker build -t food-classifier .

# Run the container
   ```bash
   docker run -p 5000:5000 food-classifier

