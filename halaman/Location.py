import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

# Membaca data dari file CSV
df = pd.read_csv("data.csv")

# Mengubah kolom 'Tanggal' menjadi tipe data datetime dan ambil tahunnya saja
df['Tahun'] = pd.to_datetime(df['Tahun'])

# Menampilkan menu sidebar untuk memilih lokasi dan tahun
selected_location = st.sidebar.selectbox("Pilih Lokasi", df['Nama Lokasi'].unique())
selected_year = st.sidebar.selectbox("Pilih Tahun", df['Tahun'].dt.year.unique())

# Filter data berdasarkan lokasi dan tahun yang dipilih
filtered_data = df[(df['Nama Lokasi'] == selected_location) & (df['Tahun'].dt.year == selected_year)]

# Menampilkan visualisasi untuk setiap parameter yang dipilih
for parameter in filtered_data['Parameter'].unique():
    plt.figure(figsize=(10, 5))
    fig, ax = plt.subplots()
    ax.plot(filtered_data[filtered_data['Parameter'] == parameter]['Tahun'].dt.month, filtered_data[filtered_data['Parameter'] == parameter]['Konsentrasi'])
    ax.set_xlabel('Bulan')
    ax.set_ylabel('Konsentrasi')
    ax.set_title(f'Grafik {parameter} di Lokasi {selected_location} pada Tahun {selected_year}')
    ax.set_xticks(range(1, 13))
    ax.set_xticklabels(['Jan', 'Feb', 'Mar', 'Apr', 'Mei', 'Jun', 'Jul', 'Ags', 'Sep', 'Okt', 'Nov', 'Des'])
    st.pyplot(fig)

    # Hapus plot untuk mencegah tumpang tindih pada plot berikutnya
    plt.clf()
