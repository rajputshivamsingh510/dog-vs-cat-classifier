from flask import Flask, render_template, request
from tensorflow import keras
import numpy as np
import cv2
import os

app = Flask(__name__)

model = keras.models.load_model("model.keras")

UPLOAD_FOLDER = "static/uploads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():

    file = request.files["image"]

    filepath = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)
    file.save(filepath)

    img = cv2.imread(filepath)
    img = cv2.resize(img, (128, 128))
    img = img.astype("float32") / 255.0
    img = np.expand_dims(img, axis=0)

    prediction = model.predict(img)[0][0]

    if prediction > 0.5:
        result = "🐶 Dog"
    else:
        result = "🐱 Cat"

    return render_template(
        "index.html",
        prediction=result,
        image=filepath
    )


if __name__ == "__main__":
    app.run(debug=True)
    