# 🐶🐱 Dog vs Cat Image Classifier

[![Python](https://img.shields.io/badge/Python-3.10-blue?logo=python)](https://www.python.org/)
[![TensorFlow](https://img.shields.io/badge/TensorFlow-Deep%20Learning-orange?logo=tensorflow)](https://www.tensorflow.org/)
[![Flask](https://img.shields.io/badge/Flask-Web%20App-black?logo=flask)](https://flask.palletsprojects.com/)
[![Live Demo](https://img.shields.io/badge/Live-Demo-success?style=for-the-badge\&logo=render)](https://dog-vs-cat-classifier-5wbp.onrender.com)

A Deep Learning-based image classification project that predicts whether an uploaded image is a **Dog** or a **Cat** using a Convolutional Neural Network (CNN). The project includes model training, image preprocessing, and a user-friendly web interface built with Flask.

---

## 🌐 Live Demo

🚀 **Try the application here:**

### **👉 https://dog-vs-cat-classifier-5wbp.onrender.com**

> **Note:** This application is deployed on **Render's Free Tier**. If the app has been inactive, the first request may take **30–60 seconds** to wake up.

---

## 📌 Project Overview

This project demonstrates the implementation of a **Binary Image Classification** model using Deep Learning. The CNN model is trained on thousands of dog and cat images to learn distinguishing visual features and accurately classify unseen images.

Users can simply upload an image through the Flask web application and receive an instant prediction.

---

## ✨ Features

* 🐶 Binary Image Classification (Dog vs Cat)
* 📤 Image Upload Interface
* 🧠 Deep Learning CNN Model
* 🖼️ Automatic Image Preprocessing
* ⚡ Real-time Prediction
* 🌐 Flask Web Application
* 📱 Simple & Responsive User Interface
* 🚀 Live Deployment on Render

---

## 🛠️ Tech Stack

* Python
* TensorFlow
* Keras
* Flask
* OpenCV
* NumPy
* HTML5
* CSS3

---

## 📂 Project Structure

```text
Dog-vs-Cat-Classifier/
│
├── static/
│   ├── uploads/
│   └── styles.css
│
├── templates/
│   └── index.html
│
├── model/
│   └── cat_dog_model.keras
│
├── dataset/
│   ├── train/
│   │   ├── cats/
│   │   └── dogs/
│   │
│   └── validation/
│       ├── cats/
│       └── dogs/
│
├── app.py
├── train_model.py
├── requirements.txt
├── README.md
└── screenshots/
```

---

## 🧠 Model Architecture

The Convolutional Neural Network (CNN) consists of:

* Convolution Layers
* ReLU Activation
* Max Pooling Layers
* Flatten Layer
* Fully Connected Dense Layers
* Dropout Layer
* Sigmoid Output Layer

### Prediction Classes

* 🐶 Dog
* 🐱 Cat

---

## 📊 Dataset

The model is trained using the **Dogs vs Cats** dataset.

Dataset Structure:

```text
dataset/

├── train/
│   ├── cats/
│   └── dogs/
│
├── validation/
│   ├── cats/
│   └── dogs/
```

---

## ⚙️ Installation

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/rajputshivamsingh510/dog-vs-cat-classifier.git
```

### 2️⃣ Navigate to the Project Directory

```bash
cd dog-vs-cat-classifier
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Project

Start the Flask application:

```bash
python app.py
```

Open your browser and visit:

```text
http://127.0.0.1:5000
```

---

## 🖼️ How to Use

1. Launch the Flask application.
2. Upload a dog or cat image.
3. Click the **Predict** button.
4. View the prediction instantly.

Possible outputs:

* 🐶 Dog
* 🐱 Cat

---

## 📈 Project Workflow

```text
           Upload Image
                 │
                 ▼
      Image Preprocessing
                 │
                 ▼
        CNN Deep Learning Model
                 │
                 ▼
          Model Prediction
                 │
                 ▼
          🐶 Dog / 🐱 Cat
```

---

## 🚀 Future Improvements

* Confidence Score Display
* Drag & Drop Image Upload
* Mobile Responsive UI
* Transfer Learning (ResNet50 / EfficientNet)
* Docker Containerization
* AWS / Azure / GCP Deployment
* Multi-Class Animal Classification
* Prediction History

---

## 📸 Screenshots

Add screenshots of your application inside the **screenshots/** folder.

Example:

```text
screenshots/

├── homepage.png
├── upload.png
└── prediction.png
```

---

## 🎯 Learning Outcomes

Through this project, I gained hands-on experience in:

* Deep Learning Fundamentals
* Convolutional Neural Networks (CNNs)
* Image Preprocessing Techniques
* TensorFlow & Keras
* Flask Web Development
* Model Deployment
* Computer Vision
* End-to-End Machine Learning Projects

---

## 🤝 Contributing

Contributions are welcome!

If you have suggestions or improvements:

1. Fork the repository.
2. Create a new feature branch.
3. Commit your changes.
4. Open a Pull Request.

---

## 📜 License

This project is licensed under the **MIT License**.

---

## 👨‍💻 Author

### **Shivam Singh**

**AI & Machine Learning Engineer**

### GitHub

https://github.com/rajputshivamsingh510

### LinkedIn

*Add your LinkedIn profile here.*

---

## ⭐ Support

If you found this project useful, please consider giving it a **⭐ Star** on GitHub.

It helps others discover the project and motivates future improvements.
