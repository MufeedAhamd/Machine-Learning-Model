import streamlit as st
import pandas as pd
import joblib

# load pipeline
model = joblib.load("weather_model.pkl")

st.title("🌦️ Weather Temperature Prediction")

# inputs
latitude = st.number_input("Latitude (north or south(°)) :")
longitude = st.number_input("Longitude (east or west(°)) :")

timezone = st.selectbox("Timezone", ["Asia/Kolkata"])

condition = st.selectbox("Condition", ["Sunny", "Cloudy", "Partly cloudy"])

wind_kph = st.number_input("Wind Speed (kph)")
pressure_in = st.number_input("Pressure (in)")
humidity = st.slider("Humidity", 0, 100)
cloud = st.slider("Cloud", 0, 100)

# predict
if st.button("Predict Temperature"):

    live = pd.DataFrame({
        'latitude':[latitude], 
        'longitude':[longitude], 
        'timezone':[timezone],
        'condition_text':[condition], 
        'wind_kph':[wind_kph], 
        'pressure_in':[pressure_in], 
        'humidity':[humidity], 
        'cloud':[cloud]
    })

    prediction = model.predict(live)

    st.success(f"🌡️ Predicted Temperature: {prediction[0]:.2f} °C")