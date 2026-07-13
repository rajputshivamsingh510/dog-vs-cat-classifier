# 🐶🐱 Dog vs Cat Image Classifier

A Deep Learning-based image classification project that predicts whether an uploaded image is a **Dog** or a **Cat** using a Convolutional Neural Network (CNN). The project includes model training, image preprocessing, and a user-friendly web interface built with Flask.

---

## 📌 Project Overview

This project demonstrates the implementation of a Binary Image Classification model using Deep Learning. The model is trained on thousands of dog and cat images to learn distinguishing visual features and accurately classify unseen images.

The application allows users to upload an image and instantly receive the prediction.

---

## 🚀 Features

- Binary Image Classification (Dog vs Cat)
- Image Upload Interface
- Deep Learning CNN Model
- Image Preprocessing
- Real-time Prediction
- Flask Web Application
- Simple and Responsive UI

---

## 🛠️ Tech Stack

- Python
- TensorFlow / Keras
- Flask
- OpenCV
- NumPy
- HTML
- CSS

---

## 📂 Project Structure

```
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
├── app.py
├── train_model.py
├── requirements.txt
├── README.md
└── dataset/
```

---

## 🧠 Model Architecture

The project uses a **Convolutional Neural Network (CNN)** consisting of:

- Convolution Layers
- ReLU Activation
- Max Pooling
- Flatten Layer
- Dense Layers
- Dropout
- Sigmoid Output Layer

The output layer predicts:

- 🐶 Dog
- 🐱 Cat

---

## 📊 Dataset

The model is trained using the **Dogs vs Cats** dataset containing images of dogs and cats.

Dataset Structure:

```
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

Clone the repository

```bash
git clone https://github.com/rajputshivamsingh510/dog-vs-cat-classifier.git
```

Navigate into the project

```bash
cd dog-vs-cat-classifier
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Project

Start the Flask application

```bash
python app.py
```

Open your browser

```
http://127.0.0.1:5000
```

---

## 🖼️ How to Use

1. Open the application.
2. Upload an image.
3. Click **Predict**.
4. The model will classify the image as:

- 🐶 Dog
- 🐱 Cat

---

## 📈 Workflow

```
Image Upload
      │
      ▼
Image Preprocessing
      │
      ▼
CNN Model
      │
      ▼
Prediction
      │
      ▼
Dog or Cat
```

---

## 💡 Future Improvements

- Mobile Responsive UI
- Drag & Drop Image Upload
- Confidence Score
- Transfer Learning (ResNet50 / EfficientNet)
- Docker Deployment
- Cloud Deployment (Render/AWS)

---

## 📸 Screenshots

Add screenshots of your application here.

Example:

```
screenshots/

Home Page
Prediction Result
```

---

## 🎯 Learning Outcomes

Through this project I learned:

- Deep Learning Fundamentals
- CNN Architecture
- Image Preprocessing
- TensorFlow/Keras
- Flask Integration
- Model Deployment
- Computer Vision Basics

---

## 🤝 Contributing

Contributions are welcome.

If you have suggestions or improvements, feel free to fork the repository and submit a Pull Request.

---

## 📜 License

This project is licensed under the MIT License.

---

## 👨‍💻 Author

**Shivam Singh**

AI & Machine Learning Engineer

GitHub:
https://github.com/rajputshivamsingh510

LinkedIn:
(Add your LinkedIn profile here)

---

⭐ If you found this project useful, don't forget to star the repository.
