# 🚗 Car Price Prediction System (MSRP Estimation)

A machine learning web application that predicts the Manufacturer's
Suggested Retail Price (MSRP) of a car from its specifications.

## 🌐 Live Demo

**Streamlit App:** https://bkkegcp7lgqzgrc3oduv9k.streamlit.app/

## 📌 Project Overview

This project builds a regression model to estimate vehicle MSRP using
manufacturer, model, engine, transmission, drivetrain, fuel type,
vehicle size, and vehicle style information.

The final solution uses a Random Forest Regressor inside a complete
scikit-learn pipeline.

## ✨ Features

-   🚘 Predict car MSRP from vehicle specifications
-   🔤 One-hot encoding for categorical features
-   📊 Standard scaling for numerical features
-   🎯 Feature selection using SelectPercentile
-   🌲 Random Forest regression
-   🔄 Complete preprocessing + feature selection + model pipeline
-   🌐 Interactive Streamlit application
-   ☁️ Streamlit Community Cloud deployment

## 🧰 Technologies Used

-   Python
-   Pandas
-   NumPy
-   Scikit-learn
-   Joblib
-   Streamlit
-   Google Colab
-   GitHub
-   Streamlit Community Cloud

## 📊 Dataset

### Input Features

**Categorical** - Make - Model - Engine Fuel Type - Transmission Type -
Driven_Wheels - Market Category - Vehicle Size - Vehicle Style

**Numerical** - Year - Engine HP - Engine Cylinders - Number of Doors -
highway MPG - city mpg - Popularity

**Target** - MSRP

## 🔄 Machine Learning Workflow

``` text
Raw Dataset
    ↓
Data Cleaning
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
Streamlit Web App
    ↓
Streamlit Community Cloud
```

## 🤖 Final Model

``` python
RandomForestRegressor(
    n_estimators=200,
    max_depth=20,
    random_state=42
)
```

The complete preprocessing, feature selection, and model are stored in:

``` text
car_price_pipeline.pkl
```

## 📈 Model Performance

  Metric            Score
  ---------- ------------
  R² Score         0.9498
  MAE          \$2,683.31

## 🖥️ Streamlit Application

The app accepts raw car details and returns an estimated MSRP.

The saved pipeline is loaded with Joblib:

``` python
pipeline = joblib.load("car_price_pipeline.pkl")
prediction = pipeline.predict(input_data)[0]
```

## 📁 Repository Structure

``` text
Car-Price-Prediction-System-MSRP-Estimation-
│
├── app.py
├── car_price_pipeline.pkl
├── requirements.txt
├── README.md
├── Regression_project_EDA.ipynb
├── car_MSRP.csv
└── cleaned_csv.CSV
```

## ⚙️ Installation

``` bash
git clone https://github.com/koushik-badineni/Car-Price-Prediction-System-MSRP-Estimation-.git
cd Car-Price-Prediction-System-MSRP-Estimation-
pip install -r requirements.txt
```

## ▶️ Run Locally

``` bash
streamlit run app.py
```

## 📦 Requirements

``` text
streamlit
pandas
numpy
scikit-learn==1.6.1
joblib
```

## ☁️ Deployment

The application is deployed using Streamlit Community Cloud.

Deployment configuration: - Repository:
`koushik-badineni/Car-Price-Prediction-System-MSRP-Estimation-` -
Branch: `main` - Main file: `app.py` - Python: `3.12`

## 🎯 Learning Outcomes

-   Exploratory Data Analysis
-   Data cleaning
-   Feature preprocessing
-   One-hot encoding
-   Feature scaling
-   Feature selection
-   Regression modeling
-   Random Forest
-   Model evaluation
-   ML pipeline creation
-   Joblib model serialization
-   Streamlit development
-   GitHub version control
-   Cloud deployment

## 👨‍💻 Author

**Koushik Badineni**

GitHub: https://github.com/koushik-badineni

------------------------------------------------------------------------

⭐ If you find this project useful, consider starring the repository.
