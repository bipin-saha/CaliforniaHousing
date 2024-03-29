import pickle
import os
import numpy as np
import pandas as pd
from flask import Flask, request, jsonify, render_template
from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import ExtraTreesRegressor

# Load California housing dataset
califo = fetch_california_housing(data_home="./")
dataset = pd.DataFrame(califo.data, columns=califo.feature_names)
dataset['Price'] = califo.target
X = dataset.iloc[:, :-1]
y = dataset.iloc[:, -1]

# Split data into train and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)

# Scale the data
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Train the model
forest = ExtraTreesRegressor()
forest.fit(X_train, y_train)

# Initialize Flask app
app = Flask(__name__)

# Load the scaler
with open('scaling.pkl', 'rb') as f:
    scalar = pickle.load(f)

# Define routes
@app.route('/')
def home():
    return render_template("index.html")

@app.route('/predict_api', methods=['POST'])
def predict_api():
    data = request.json['data']
    new_data = scalar.transform(np.array(list(data.values())).reshape(1, -1))
    output = forest.predict(new_data)
    return jsonify(output[0])

@app.route('/predict', methods=['POST'])
def predict():
    data = request.form.to_dict(flat=False)
    data = {key: float(value[0]) for key, value in data.items()}
    new_data = scalar.transform(np.array(list(data.values())).reshape(1, -1))
    output = forest.predict(new_data)[0]
    return render_template("index.html", prediction_text=output)

# Run the app
if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=7860)
