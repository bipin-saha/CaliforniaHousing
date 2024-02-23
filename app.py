import pickle
import os
import numpy as np
import pandas as pd
from flask import Flask, request, app, jsonify, url_for, render_template

app = Flask(__name__)
model = pickle.load(open('uncompressed_forest.pkl', 'rb'))
scalar=pickle.load(open('scaling.pkl','rb'))


@app.route('/')
def home():

    return render_template("index.html")

@app.route('/predict_api', methods=['POST'])
def predict_api():
    data = request.json['data']
    new_data = scalar.transform(np.array(list(data.values())).reshape(1,-1))
    output = model.predict(new_data)
    return jsonify(output[0])

@app.route('/predict', methods=['POST'])
def predict():
    data = request.form.to_dict(flat=False)
    data = {key: float(value[0]) for key, value in data.items()}
    new_data = scalar.transform(np.array(list(data.values())).reshape(1,-1))
    print(new_data)
    output = model.predict(new_data)[0]
    return render_template("index.html", prediction_text=output)


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)