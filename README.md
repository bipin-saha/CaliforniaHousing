---
title: California Housing Price Prediction Web App
emoji: 🐳
colorFrom: purple
colorTo: gray
sdk: docker
app_port: 7860
---
Check out the configuration reference at [https://huggingface.co/docs/hub/spaces-config-reference](https://huggingface.co/spaces/bipinsaha/Docker_ClaiforniaHouse)

This repository contains code for a web application built with FastAPI that predicts housing prices in California based on various features. The application is deployed using Hugging Face with a CI/CD pipeline set up using GitHub Actions.

## Code Documentation

### Libraries Used:
- `pickle`: For serializing and deserializing Python objects.
- `numpy`: For numerical computations.
- `FastAPI`: For building APIs quickly and easily.
- `Jinja2Templates`: For HTML templating.
- `sklearn.datasets`: For fetching the California housing dataset.
- `sklearn.model_selection`: For splitting the dataset into training and testing sets.
- `sklearn.preprocessing`: For scaling the data.
- `sklearn.ensemble`: For implementing the Extra Trees Regressor model.

### Steps:
1. **Data Loading and Preprocessing**:
   - The California housing dataset is fetched.
   - The dataset is split into training and testing sets.
   - Data is scaled using StandardScaler.

2. **Model Training**:
   - An Extra Trees Regressor model is trained on the training data.

3. **Web Application Setup**:
   - FastAPI is initialized.
   - Jinja2Templates is configured for rendering HTML templates.

4. **Routes**:
   - `GET "/"`: Renders the home page template.
   - `POST "/predict"`: Accepts form data for housing features, predicts the price, and renders the home page template with the predicted price.

### Dockerfile:
- The Dockerfile specifies the environment setup for running the FastAPI application inside a Docker container.
- It's based on the Python 3.11.8-bullseye image.
- It creates a directory `/code` to store application files and sets it as the working directory.
- It copies all files from the current directory into the container's `/code` directory.
- It installs dependencies specified in `requirements.txt`.
- Exposes port 7860 for accessing the FastAPI application.
- Specifies the command to run the FastAPI application using uvicorn.

## Docker Documentation

### Image Base:
- The Dockerfile uses the official Python 3.11.8-bullseye image as the base image.

### Directory Setup:
- It creates a directory named `/code` inside the container to store application files.

### Dependency Installation:
- It installs dependencies listed in the `requirements.txt` file using `pip install -r requirements.txt`.

### Port Exposing:
- It exposes port 7860, which is the port on which the FastAPI application will be running.

### Command:
- The CMD instruction specifies the command to run when the container starts.
- It runs the FastAPI application using uvicorn, specifying the host as "0.0.0.0" and port as "7860".

### CI/CD Pipeline with GitHub Actions:
- The repository is set up with a CI/CD pipeline using GitHub Actions.
- The pipeline automates the deployment process to Hugging Face whenever changes are pushed to the main branch.

