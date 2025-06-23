import streamlit as st
import pandas as pd
import pickle


with open("rf_reg_model.pkl", "rb") as file:
    model = pickle.load(file)

with open("encoders.pkl", "rb") as file:
    encoders = pickle.load(file)


st.title(" Second-Hand Selling Price Prediction")


brand = st.text_input("Brand")
model_name = st.text_input("Model")
color = st.text_input("Color")
memory = st.text_input("Memory")  
storage = st.text_input("Storage")  
rating = st.number_input("Rating", min_value=0.0, max_value=5.0, step=0.1)
original_price = st.number_input("Original Price", min_value=0, step=100)


def encode_input(value, encoder):
    if value in encoder.classes_:
        return encoder.transform([value])[0]
    else:
        return -1  

if st.button("Predict Selling Price"):
    input_data = pd.DataFrame([[brand, model_name, color, memory, storage, rating, original_price]],
                              columns=["Brand", "Model", "Color", "Memory", "Storage", "Rating", "Original Price"])
    
    
    for col in ["Brand", "Model", "Color", "Memory", "Storage"]:
        input_data[col] = encode_input(input_data[col][0], encoders[col])

    prediction = model.predict(input_data)[0]
    
    st.success(f"Predicted Selling Price: ${prediction:.2f}")

