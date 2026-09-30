import streamlit as st
import pandas as pd
import joblib


# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="Car Price Prediction",
    page_icon="🚗",
    layout="wide"
)


# ============================================================
# LOAD TRAINED PIPELINE
# ============================================================

@st.cache_resource
def load_pipeline():
    return joblib.load("car_price_pipeline.pkl")


try:
    pipeline = load_pipeline()

except Exception as e:
    st.error("Unable to load the trained model.")
    st.exception(e)
    st.stop()


# ============================================================
# GET CATEGORIES FROM TRAINED PIPELINE
# ============================================================

preprocessor = pipeline.named_steps["preprocessor"]

# Categorical transformer
categorical_encoder = (
    preprocessor
    .named_transformers_["cat"]
)

# Categories learned during training
categories = categorical_encoder.categories_

# Order of categorical columns in the pipeline
categorical_columns = [
    "Make",
    "Model",
    "Engine Fuel Type",
    "Transmission Type",
    "Driven_Wheels",
    "Market Category",
    "Vehicle Size",
    "Vehicle Style"
]

# Create dictionary of valid values
valid_categories = dict(
    zip(categorical_columns, categories)
)


# ============================================================
# PAGE TITLE
# ============================================================

st.title("🚗 Car Price Prediction System")

st.write(
    "Predict the Manufacturer's Suggested Retail Price (MSRP) "
    "of a car using Machine Learning."
)


st.info(
    "Select values from the available options. "
    "Only categories learned during model training are available."
)


# ============================================================
# INPUT SECTION
# ============================================================

st.subheader("Enter Car Details")

col1, col2 = st.columns(2)


# ============================================================
# CATEGORICAL FEATURES
# ============================================================

with col1:

    # Make
    make = st.selectbox(
        "Make",
        valid_categories["Make"]
    )

    # Model
    model_name = st.selectbox(
        "Model",
        valid_categories["Model"]
    )

    # Fuel Type
    fuel_type = st.selectbox(
        "Engine Fuel Type",
        valid_categories["Engine Fuel Type"]
    )

    # Transmission
    transmission = st.selectbox(
        "Transmission Type",
        valid_categories["Transmission Type"]
    )

    # Driven Wheels
    driven_wheels = st.selectbox(
        "Driven Wheels",
        valid_categories["Driven_Wheels"]
    )

    # Market Category
    market_category = st.selectbox(
        "Market Category",
        valid_categories["Market Category"]
    )

    # Vehicle Size
    vehicle_size = st.selectbox(
        "Vehicle Size",
        valid_categories["Vehicle Size"]
    )

    # Vehicle Style
    vehicle_style = st.selectbox(
        "Vehicle Style",
        valid_categories["Vehicle Style"]
    )


# ============================================================
# NUMERICAL FEATURES
# ============================================================

with col2:

    year = st.number_input(
        "Year",
        min_value=1980,
        max_value=2026,
        value=2011,
        step=1
    )

    engine_hp = st.number_input(
        "Engine HP",
        min_value=0.0,
        value=300.0,
        step=1.0
    )

    engine_cylinders = st.number_input(
        "Engine Cylinders",
        min_value=0.0,
        value=6.0,
        step=1.0
    )

    number_of_doors = st.number_input(
        "Number of Doors",
        min_value=0.0,
        value=4.0,
        step=1.0
    )

    highway_mpg = st.number_input(
        "Highway MPG",
        min_value=0.0,
        value=28.0,
        step=1.0
    )

    city_mpg = st.number_input(
        "City MPG",
        min_value=0.0,
        value=20.0,
        step=1.0
    )

    popularity = st.number_input(
        "Popularity",
        min_value=0,
        value=3916,
        step=1
    )


# ============================================================
# PREDICTION
# ============================================================

st.divider()

if st.button(
    "🔮 Predict Price",
    type="primary",
    use_container_width=True
):

    # --------------------------------------------------------
    # Basic validation
    # --------------------------------------------------------

    if number_of_doors <= 0:
        st.error("Number of doors must be greater than 0.")
        st.stop()

    if engine_hp < 0:
        st.error("Engine HP cannot be negative.")
        st.stop()

    if engine_cylinders < 0:
        st.error("Engine cylinders cannot be negative.")
        st.stop()

    if highway_mpg < 0 or city_mpg < 0:
        st.error("MPG values cannot be negative.")
        st.stop()

    if popularity < 0:
        st.error("Popularity cannot be negative.")
        st.stop()


    # --------------------------------------------------------
    # Create input DataFrame
    # --------------------------------------------------------

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


    # --------------------------------------------------------
    # Generate prediction
    # --------------------------------------------------------

    try:

        prediction = pipeline.predict(input_data)[0]

        # Prevent displaying an invalid negative price
        if prediction < 0:

            st.warning(
                "The model generated an unrealistic prediction "
                "for these inputs. Please check the vehicle details."
            )

        else:

            st.success(
                f"💰 Estimated MSRP: ${prediction:,.2f}"
            )

            # ------------------------------------------------
            # Display entered details
            # ------------------------------------------------

            st.subheader("Vehicle Details")

            display_data = input_data.T

            display_data.columns = ["Value"]

            st.dataframe(
                display_data,
                use_container_width=True
            )

    except Exception as e:

        st.error(
            "Prediction failed. Please check the input values."
        )

        st.exception(e)
