import streamlit as st
import requests

st.title("Zoologist front")

st.header("Enter penguin characteristics")

island = st.selectbox("Island", ["Biscoe", "Dream", "Torgersen"])
bill_length_mm = st.number_input("Bill length (mm)", value=40.0)
bill_depth_mm = st.number_input("Bill depth (mm)", value=18.0)
flipper_length_mm = st.number_input("Flipper length (mm)", value=200.0)
body_mass_g = st.number_input("Body mass (g)", value=4000.0)
sex = st.selectbox("Sex", ["Male", "Female"])

url = f"{st.secrets['API_URL']}/predict"

params = {
    "island": island,
    "bill_length_mm": bill_length_mm,
    "bill_depth_mm": bill_depth_mm,
    "flipper_length_mm": flipper_length_mm,
    "body_mass_g": body_mass_g,
    "sex": sex,
}

if st.button("Predict"):
    response = requests.get(url, params=params)
    if response.status_code == 200:
        prediction = response.json()
        st.success(f"Prediction: {prediction}")
    else:
        st.error(f"API Error: {response.status_code}")
