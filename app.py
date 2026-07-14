import os
os.environ["TF_CPP_MIN_LOG_LEVEL"] = "3"

import base64
import numpy as np
import cv2
from flask import Flask, render_template, request

try:
    import tflite_runtime.interpreter as tflite
except ImportError:
    # Fallback if tflite_runtime isn't available
    import tensorflow.lite as tflite

app = Flask(__name__)

# Load TFLite model once at startup
interpreter = tflite.Interpreter(model_path="model.tflite")
interpreter.allocate_tensors()

input_details = interpreter.get_input_details()
output_details = interpreter.get_output_details()


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():
    file = request.files["image"]

    file_bytes = np.frombuffer(file.read(), np.uint8)
    img = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)

    if img is None:
        return render_template("index.html", prediction="⚠️ Invalid image file.")

    resized = cv2.resize(img, (128, 128))
    resized = resized.astype("float32") / 255.0
    resized = np.expand_dims(resized, axis=0)

    interpreter.set_tensor(input_details[0]['index'], resized)
    interpreter.invoke()
    prediction = interpreter.get_tensor(output_details[0]['index'])[0][0]

    result = "🐶 Dog" if prediction > 0.5 else "🐱 Cat"

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
