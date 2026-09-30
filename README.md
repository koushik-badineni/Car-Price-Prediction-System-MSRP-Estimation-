# 🚗 Car Price Prediction System (MSRP Estimation)

A machine learning web application that predicts the Manufacturer's
Suggested Retail Price (MSRP) of a car based on its specifications.

## 🌐 Live Demo

**Streamlit App:** https://bkkegcp7lgqzgrc3oduv9k.streamlit.app/

---

## 📌 Project Overview

This project builds a supervised machine learning regression model to
estimate the Manufacturer's Suggested Retail Price (MSRP) of a vehicle.

The model uses vehicle specifications such as manufacturer, model,
engine details, transmission, drivetrain, fuel type, vehicle size,
vehicle style, mileage, and popularity.

The final solution uses a **Random Forest Regressor** inside a complete
scikit-learn pipeline that includes preprocessing, feature selection,
and model prediction.

The trained pipeline is saved using **Joblib** and integrated into an
interactive **Streamlit web application**.

---

## 🎯 Problem Statement

Car prices vary significantly depending on factors such as brand,
model, engine specifications, fuel type, transmission, drivetrain,
vehicle size, mileage, and popularity.

The objective of this project is to build a machine learning regression
system that can learn relationships between these vehicle attributes
and MSRP and provide an estimated price for a given vehicle.

---

## ✨ Features

- 🚘 Predict car MSRP from vehicle specifications
- 🔤 One-Hot Encoding for categorical features
- 📊 Standard Scaling for numerical features
- 🎯 Feature selection using SelectPercentile
- 🌲 Random Forest Regression
- 🔄 Complete preprocessing + feature selection + model pipeline
- 💾 Model serialization using Joblib
- ✅ Basic input validation
- 🌐 Interactive Streamlit application
- ☁️ Streamlit Community Cloud deployment

---

## 🧰 Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Joblib
- Streamlit
- Google Colab
- GitHub
- Streamlit Community Cloud

---

## 📊 Dataset

The dataset contains vehicle specifications used to predict MSRP.

### Input Features

#### 🔤 Categorical Features

- Make
- Model
- Engine Fuel Type
- Transmission Type
- Driven_Wheels
- Market Category
- Vehicle Size
- Vehicle Style

#### 🔢 Numerical Features

- Year
- Engine HP
- Engine Cylinders
- Number of Doors
- highway MPG
- city mpg
- Popularity

#### 🎯 Target Variable

- MSRP

---

## 🔄 Machine Learning Workflow

```text
Raw Dataset
     ↓
Data Cleaning
     ↓
Exploratory Data Analysis
     ↓
Train-Test Split
     ↓
Categorical / Numerical Feature Separation
     ↓
One-Hot Encoding + Standard Scaling
     ↓
SelectPercentile Feature Selection
     ↓
Random Forest Regressor
     ↓
Complete ML Pipeline
     ↓
Model Evaluation
     ↓
Joblib Serialization
     ↓
Streamlit Web Application
     ↓
Streamlit Community Cloud
