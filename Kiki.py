import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

import seaborn as sns


#load data
data = pd.read_csv("combined.csv")

def main():
    st.header("Sungai Code")
    st.sidebar.header("Sungai Code")
    plot_options = ["Sungai Code Jembatan Gondolayu", "Sungai Code Jembatan Sayidan", "Sungai Code Petinggen", "Sungai Code Wirogunan"
                    , "Sungai Code Wirosaban", "Sungai Code Semua Tikik (DIY)"]
    selected_plot = st.sidebar.selectbox("Pilih Titik Pengukuran", plot_options)
    
    if selected_plot == "Sungai Code Jembatan Gondolayu":

