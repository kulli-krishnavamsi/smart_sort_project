<<<<<<< HEAD
from flask import Flask, render_template, request, redirect, url_for
=======

from flask import Flask, render_template, request
>>>>>>> c030f53de01d33ec72498363afc1ad8e30dd6703
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np
import os

app = Flask(__name__)
model = load_model('healthy_vs_rotten.h5')

classes = sorted(os.listdir('dataset/train'))

prediction_result = None

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

@app.route("/about", methods=["GET"])
def about():
    return render_template("about.html")

@app.route("/predict", methods=["GET", "POST"])
def predict():
    global prediction_result
    if request.method == "POST":
        img_file = request.files["file"]
        img_path = os.path.join("static", img_file.filename)
        img_file.save(img_path)

        img = image.load_img(img_path, target_size=(150, 150))
        img_array = image.img_to_array(img)
        img_array = np.expand_dims(img_array, axis=0) / 255.0

        prediction = model.predict(img_array)
        class_index = np.argmax(prediction)
        prediction_result = classes[class_index]

        return redirect(url_for('result'))
    return render_template("predict.html")

@app.route("/result")
def result():
    global prediction_result
    return render_template("result.html", result=prediction_result)

if __name__ == "__main__":
    app.run(debug=True)
