import pickle
import os
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from flask import Flask, request, app, jsonify, url_for, render_template

app = Flask(__name__)
model = pickle.load(open('uncompressed_forest.pkl', 'rb'))
scaler = StandardScaler()


@app.route('/')
def home():
    return render_template("index.html")

@app.route('/predict', methods=['POST'])
def predict_api():
    data = request.json['data']
    print(data)
    new_data = scaler.fit_transform(np.array(list(data.values())).reshape(1, -1))
    print(new_data)
    output = model.predict(new_data)
    print(output[0])
    return jsonify(output[0])



if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)