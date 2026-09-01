# 🚗 Car Price Prediction System – MSRP Estimation

![Python](https://img.shields.io/badge/Python-3.x-blue)
![Machine Learning](https://img.shields.io/badge/Machine%20Learning-Regression-orange)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-ML-green)
![Status](https://img.shields.io/badge/Project-Completed-success)

## 📌 Project Overview

The **Car Price Prediction System** is a Machine Learning project designed to predict the **Manufacturer's Suggested Retail Price (MSRP)** of a vehicle based on its specifications and characteristics.

The system uses vehicle attributes such as brand, model, manufacturing year, engine specifications, fuel type, transmission, drivetrain, MPG, vehicle style, and popularity to estimate the car's price.

This project demonstrates the practical application of **Supervised Machine Learning and Regression** techniques in automotive price prediction.

---

## 🎯 Problem Statement

The automobile market contains a wide variety of vehicles with different brands, specifications, and features, making accurate price estimation challenging.

The goal of this project is to answer:

> **Can we predict the price of a car based on its features such as engine specifications, fuel type, brand, and other attributes?**

---

## 🎯 Objective

The main objective is to build a **regression-based Machine Learning model** that can predict a vehicle's MSRP using its numerical and categorical features.

---

## 📊 Dataset

The project uses the **CAR_MSRP** dataset.

### Dataset Characteristics

* **Domain:** Automotive / Pricing Analytics
* **Records:** Thousands of car entries
* **Features:** 10–15+ input features
* **Feature Types:** Numerical and Categorical
* **Target Variable:** MSRP

---

## 🧾 Features

| Feature           | Description                           | Type        |
| ----------------- | ------------------------------------- | ----------- |
| Make              | Brand/manufacturer of the car         | Categorical |
| Model             | Specific vehicle model                | Categorical |
| Year              | Manufacturing year                    | Numerical   |
| Engine Fuel Type  | Type of fuel used                     | Categorical |
| Engine HP         | Engine horsepower                     | Numerical   |
| Engine Cylinders  | Number of engine cylinders            | Numerical   |
| Transmission Type | Automatic or Manual                   | Categorical |
| Driven Wheels     | FWD, RWD, AWD                         | Categorical |
| Number of Doors   | Number of doors                       | Numerical   |
| Vehicle Size      | Compact, Midsize, Large               | Categorical |
| Vehicle Style     | Sedan, SUV, Coupe, Hatchback, etc.    | Categorical |
| Highway MPG       | Highway fuel efficiency               | Numerical   |
| City MPG          | City fuel efficiency                  | Numerical   |
| Popularity        | Brand popularity score                | Numerical   |
| MSRP              | Manufacturer's Suggested Retail Price | **Target**  |

---

## 🔄 Project Workflow

```text
Data Collection
      ↓
Data Cleaning
      ↓
Exploratory Data Analysis
      ↓
Data Preprocessing
      ↓
Feature Engineering
      ↓
Encoding Categorical Variables
      ↓
Feature Selection
      ↓
Model Training
      ↓
Model Evaluation
      ↓
MSRP Prediction
```

---

## 🔍 Exploratory Data Analysis

Exploratory Data Analysis was performed to understand:

* Distribution of car prices
* Relationship between car features and MSRP
* Impact of engine horsepower on price
* Impact of manufacturing year on price
* Relationship between MPG and price
* Brand-wise price differences
* Correlation between numerical features
* Outliers and missing values

---

## 🛠️ Technologies Used

### Programming Language

* Python

### Libraries

* Pandas
* NumPy
* Matplotlib
* Seaborn
* Scikit-learn

### Machine Learning

* Supervised Learning
* Regression
* Data Preprocessing
* Feature Engineering
* Model Evaluation

---

## 🤖 Machine Learning Approach

Since **MSRP is a continuous numerical variable**, this project is treated as a **Regression problem**.

The general machine learning process includes:

1. Loading the dataset
2. Understanding the data
3. Handling missing values
4. Performing exploratory data analysis
5. Preparing numerical and categorical features
6. Encoding categorical variables
7. Splitting data into training and testing sets
8. Training the regression model
9. Evaluating model performance
10. Predicting MSRP for new vehicles

---

## 📈 Model Evaluation

The trained regression model can be evaluated using commonly used regression metrics such as:

* **Mean Absolute Error (MAE)**
* **Mean Squared Error (MSE)**
* **Root Mean Squared Error (RMSE)**
* **R² Score**

These metrics help determine how accurately the model predicts vehicle prices.

> Add your actual model performance values here after training the final model.

Example:

```text
R² Score: XX.XX
RMSE: XXXXX
MAE: XXXXX
```

---

## 💡 Business Applications

A car price prediction system can be useful for:

* 🚘 Helping customers make informed purchasing decisions
* 🏪 Supporting dealerships with pricing strategies
* 📊 Competitive market analysis
* 🏭 Automotive product positioning
* 🤝 Vehicle recommendation systems
* 💰 Automated price estimation

---

## 📂 Project Structure

```text
Car-Price-Prediction/
│
├── dataset/
│   └── CAR_MSRP.csv
│
├── notebooks/
│   └── Car_Price_Prediction.ipynb
│
├── app/
│   └── app.py
│
├── requirements.txt
├── README.md
└── .gitignore
```

> Modify the folder and file names according to the actual structure of your repository.

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/koushik-badineni/Car-Price-Prediction.git
```

### 2. Navigate to the project directory

```bash
cd Car-Price-Prediction
```

### 3. Create a virtual environment

```bash
python -m venv venv
```

### 4. Activate the virtual environment

**Windows:**

```bash
venv\Scripts\activate
```

**Mac/Linux:**

```bash
source venv/bin/activate
```

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ How to Run

If the project contains a Jupyter Notebook:

```bash
jupyter notebook
```

Open the project notebook and execute the cells.

If the project contains a Streamlit application:

```bash
streamlit run app.py
``

---

## 🚀 Future Improvements

Some possible improvements include:

* Hyperparameter tuning
* Feature selection optimization
* Testing multiple regression algorithms
* Ensemble learning
* Improving model accuracy
* Deploying the model as a web application
* Adding real-time vehicle price prediction
* Creating a user-friendly dashboard

---

## 👨‍💻 Author

**Manikanta Koushik**

This project was developed as part of my Machine Learning learning journey to gain practical experience in **Regression, Data Preprocessing, Exploratory Data Analysis, and Model Building**.

---

## ⭐ Acknowledgment

If you found this project useful, consider giving the repository a ⭐ on GitHub.

---

## 📜 License

This project is intended for educational and learning purposes.
