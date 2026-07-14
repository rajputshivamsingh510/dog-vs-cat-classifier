import os
os.environ["TF_CPP_MIN_LOG_LEVEL"] = "3"  # quiet TensorFlow logging

import base64
from flask import Flask, render_template, request
from tensorflow import keras
import tensorflow as tf
import numpy as np
import cv2

# Reduce TF's internal thread/memory overhead on small servers
tf.config.threading.set_intra_op_parallelism_threads(1)
tf.config.threading.set_inter_op_parallelism_threads(1)

app = Flask(__name__)
model = keras.models.load_model("model.keras")


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():
    file = request.files["image"]

    # Read the uploaded file directly into memory — never touches disk
    file_bytes = np.frombuffer(file.read(), np.uint8)
    img = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)

    if img is None:
        return render_template("index.html", prediction="⚠️ Invalid image file.")

    # Preprocess for the model
    resized = cv2.resize(img, (128, 128))
    resized = resized.astype("float32") / 255.0
    resized = np.expand_dims(resized, axis=0)

    prediction = model.predict(resized)[0][0]
    result = "🐶 Dog" if prediction > 0.5 else "🐱 Cat"

    # Encode the original image as base64 so it can still be shown in the browser
    # without ever saving it to disk
    _, buffer = cv2.imencode(".jpg", img)
    encoded_image = base64.b64encode(buffer).decode("utf-8")
    image_data_uri = f"data:image/jpeg;base64,{encoded_image}"

    return render_template(
        "index.html",
        prediction=result,
        image=image_data_uri
    )


if __name__ == "__main__":
    app.run(debug=False)
