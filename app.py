import pickle
from flask import Flask, request, app, jsonify, url_for, render_template
import numpy as np
import pandas as pd

app = Flask(__name__)
model=pickle.load(open("model.pkl", "rb"))
scaler=pickle.load(open("scale.pkl", "rb"))

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/predict_api", methods=['POST'])
def predict_api():
    data=request.json['data']
    data=np.array(list(data.values())).reshape(1,-1)
    new_Data = scaler.transform(data)
    print(new_Data)
    out = model.predict(new_Data)
    return jsonify(out[0])

if __name__ =="__main__":
    app.run(debug=True)