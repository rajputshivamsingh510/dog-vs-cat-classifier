import cv2
import numpy as np
from tensorflow import keras

model = keras.models.load_model("model.keras")

def predict_image(img_path):
    img = cv2.imread(img_path)
    img = cv2.resize(img, (128, 128))
    img = img.astype(np.float32) / 255.0
    img = np.expand_dims(img, axis=0)  # (1, 128, 128, 3)

    pred = model.predict(img)[0][0]
    label = "Dog" if pred > 0.5 else "Cat"
    print(f"Prediction: {label} (raw score: {pred:.4f})")

predict_image("cat2.jpg")