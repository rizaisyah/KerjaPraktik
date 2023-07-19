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
        plt.plot(data['Konsentrasi'])
        plt.xlabel('Baku Mutu')
        plt.ylabel('pH Value')
        plt.title('Variasi pH')
        plt.show()

    elif selected_plot == "Sungai Code Jembatan Sayidan":
        plt.plot(data['Konsentrasi'])
        plt.xlabel('Baku Mutu')
        plt.ylabel('pH Value')
        plt.title('Variasi pH')
        plt.show()

    elif selected_plot == "Sungai Code Petinggen":
        plt.plot(data['Konsentrasi'])
        plt.xlabel('Baku Mutu')
        plt.ylabel('pH Value')
        plt.title('Variasi pH')
        plt.show()
    elif selected_plot == "Sungai Code Wirogunan":
        plt.plot(data['Konsentrasi'])
        plt.xlabel('Baku Mutu')
        plt.ylabel('pH Value')
        plt.title('Variasi pH')
        plt.show()
    elif selected_plot == "Sungai Code Wirosaban":
        plt.plot(data['Konsentrasi'])
        plt.xlabel('Baku Mutu')
        plt.ylabel('pH Value')
        plt.title('Variasi pH')
        plt.show()
        
    elif selected_plot == "Sungai Code Semua Tikik (DIY)":
        plt.plot(data['Konsentrasi'])
        plt.xlabel('Baku Mutu')
        plt.ylabel('pH Value')
        plt.title('Variasi pH')
        plt.show()

