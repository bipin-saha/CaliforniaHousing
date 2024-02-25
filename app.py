import pickle
import numpy as np
from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import ExtraTreesRegressor

# Load California housing dataset
califo = fetch_california_housing(data_home="./")
X = califo.data
y = califo.target

# Split data into train and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)

# Scale the data
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Train the model
forest = ExtraTreesRegressor()
forest.fit(X_train, y_train)

# Load the scaler
with open('scaling.pkl', 'rb') as f:
    scalar = pickle.load(f)

# Initialize FastAPI app
app = FastAPI()
templates = Jinja2Templates(directory="templates")

# Define routes
@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "prediction_text": None})

@app.post("/predict")
async def predict(request: Request, 
                  MedInc: float = Form(...), 
                  HouseAge: float = Form(...), 
                  AveRooms: float = Form(...), 
                  AveBedrms: float = Form(...), 
                  Population: float = Form(...), 
                  AveOccup: float = Form(...), 
                  Latitude: float = Form(...), 
                  Longitude: float = Form(...)):
    try:
        data = {
            "MedInc": MedInc,
            "HouseAge": HouseAge,
            "AveRooms": AveRooms,
            "AveBedrms": AveBedrms,
            "Population": Population,
            "AveOccup": AveOccup,
            "Latitude": Latitude,
            "Longitude": Longitude
        }
        new_data = scalar.transform(np.array(list(data.values())).reshape(1, -1))
        output = forest.predict(new_data)[0]
        return templates.TemplateResponse("index.html", {"request": request, "prediction_text": output})
    except Exception as e:
        return templates.TemplateResponse("index.html", {"request": request, "prediction_text": f"Error: {e}"})

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=7860)
