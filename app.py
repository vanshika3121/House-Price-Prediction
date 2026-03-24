import streamlit as st
import pickle

# Load model
model = pickle.load(open("model.pkl", "rb"))

# Title
st.title("🏠 House Price Predictor")

st.write("Enter details below:")

# Inputs
area = st.number_input("Area (in sq ft)", min_value=0)
bedrooms = st.number_input("Bedrooms", min_value=0)
bathrooms = st.number_input("Bathrooms", min_value=0)

# Button
if st.button("Predict Price"):
    result = model.predict([[area, bedrooms, bathrooms]])
    st.success(f"Estimated Price: ₹ {int(result[0])}")