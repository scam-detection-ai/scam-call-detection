import streamlit as st
import pickle

with open("model.pkl", "rb") as f:
    model = pickle.load(f)

st.title("AI Based Scam Call Detection")

duration = st.number_input("Call Duration", min_value=0)
frequency = st.number_input("Frequency", min_value=0)
complaints = st.number_input("Complaints", min_value=0)

if st.button("Check"):
    result = model.predict([[duration, frequency, complaints]])

    if result[0] == 1:
        st.error("⚠️ Scam Call Detected")
    else:
        st.success("✅ Safe Call")

