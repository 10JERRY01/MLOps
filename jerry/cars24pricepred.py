import pandas as pd
import streamlit as st
import datetime
import pickle

cars_df = pd.read_excel('jerry/cars24-car-price.xlsx')

st.write(
    """
     # Cars24 Used Cars Price Prediction
    """
)
st.dataframe(cars_df.head())