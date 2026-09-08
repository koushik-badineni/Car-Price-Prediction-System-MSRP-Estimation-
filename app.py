import streamlit as st
import pandas as pd
import joblib


# -----------------------------
# Load model and preprocessor
# -----------------------------

pipeline = joblib.load("car_price_pipeline.pkl")


# -----------------------------
# Page configuration
# -----------------------------

st.set_page_config(
    page_title="Car Price Prediction",
    page_icon="🚗",
    layout="wide"
)


# -----------------------------
# Title
# -----------------------------

st.title("🚗 Car Price Prediction System")
st.write("Predict the Manufacturer's Suggested Retail Price (MSRP) of a car.")


# -----------------------------
# Input section
# -----------------------------

st.subheader("Enter Car Details")


col1, col2 = st.columns(2)


# Categorical inputs

with col1:

    make = st.text_input("Make", "BMW")

    model_name = st.text_input("Model", "1 Series")

    fuel_type = st.text_input(
        "Engine Fuel Type",
        "premium unleaded (required)"
    )

    transmission = st.text_input(
        "Transmission Type",
        "MANUAL"
    )

    driven_wheels = st.text_input(
        "Driven Wheels",
        "rear wheel drive"
    )

    market_category = st.text_input(
        "Market Category",
        "Luxury"
    )

    vehicle_size = st.text_input(
        "Vehicle Size",
        "Compact"
    )

    vehicle_style = st.text_input(
        "Vehicle Style",
        "Coupe"
    )


# Numerical inputs

with col2:

    year = st.number_input(
        "Year",
        min_value=1980,
        max_value=2026,
        value=2011
    )

    engine_hp = st.number_input(
        "Engine HP",
        min_value=0.0,
        value=300.0
    )

    engine_cylinders = st.number_input(
        "Engine Cylinders",
        min_value=0.0,
        value=6.0
    )

    number_of_doors = st.number_input(
        "Number of Doors",
        min_value=2.0,
        max_value=6.0,
        value=4.0
    )

    highway_mpg = st.number_input(
        "Highway MPG",
        min_value=0.0,
        value=28.0
    )

    city_mpg = st.number_input(
        "City MPG",
        min_value=0.0,
        value=20.0
    )

    popularity = st.number_input(
        "Popularity",
        min_value=0,
        value=3916
    )


# -----------------------------
# Prediction
# -----------------------------

if st.button("🔮 Predict Price"):

    input_data = pd.DataFrame({
        "Make": [make],
        "Model": [model_name],
        "Year": [year],
        "Engine Fuel Type": [fuel_type],
        "Engine HP": [engine_hp],
        "Engine Cylinders": [engine_cylinders],
        "Transmission Type": [transmission],
        "Driven_Wheels": [driven_wheels],
        "Number of Doors": [number_of_doors],
        "Market Category": [market_category],
        "Vehicle Size": [vehicle_size],
        "Vehicle Style": [vehicle_style],
        "highway MPG": [highway_mpg],
        "city mpg": [city_mpg],
        "Popularity": [popularity]
    })

    prediction = pipeline.predict(input_data)[0]

    st.success(
        f"Estimated MSRP: ${prediction:,.2f}"
    )