import streamlit as 
import pandas as pd 
import joblib 
import lightgbm as lgb 
from geopy.distance import geodesic 

model = joblib.load("fraud_detection_model.jb") 
encoder =joblib.load("label_encoder.jb") 

def haversine (lat1, lon1, lat2, lon2): 
    return geodesic((lat1, lon1), (lat2, lon2)).km 

st.title("Fraud Detection System") 
st.write("Enter the Transaction details Below")