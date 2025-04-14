import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import numpy as np

# Load data
file_path_all = 'all_data.csv'
df_all = pd.read_csv(file_path_all)

file_path_day = 'day.csv'
df_day = pd.read_csv(file_path_day)

file_path_hour = 'hour.csv'
df_hour = pd.read_csv(file_path_hour)

for col in ['cnt_x', 'cnt_y', 'temp_x', 'atemp_x', 'hum_x', 'windspeed_x']:
    if col in df_all.columns:
        df_all[col] = pd.to_numeric(df_all[col], errors='coerce')

# Hanya memilih kolom numerik untuk korelasi
numeric_df_all = df_all.select_dtypes(include=['number'])
numeric_df_day = df_day.select_dtypes(include=['number'])
numeric_df_hour = df_hour.select_dtypes(include=['number'])

# Streamlit app
st.title("Analisis Penyewaan Sepeda")

# Menampilkan data
if st.checkbox("Tampilkan data mentah (all_data)"):
    st.write(df_all.head())
if st.checkbox("Tampilkan data mentah (day)"):
    st.write(df_day.head())
if st.checkbox("Tampilkan data mentah (hour)"):
    st.write(df_hour.head())

# Korelasi antara fitur dan jumlah penyewaan
st.subheader("Faktor yang Mempengaruhi Jumlah Penyewaan Sepeda")
corr_matrix = numeric_df_all.corr()
fig, ax = plt.subplots(figsize=(10, 6))
sns.heatmap(corr_matrix[['cnt_x']].sort_values(by='cnt_x', ascending=False), annot=True, cmap='coolwarm', ax=ax)
st.pyplot(fig)

# Perhitungan korelasi antara cnt_x dan cnt_y
st.subheader("Perhitungan Korelasi cnt_x dan cnt_y")
if 'cnt_x' in numeric_df_all.columns and 'cnt_y' in numeric_df_all.columns:
    correlation = numeric_df_all[['cnt_x', 'cnt_y']].corr().iloc[0, 1]
    st.write(f"Korelasi antara cnt_x dan cnt_y: {correlation:.2f}")
else:
    st.write("Kolom cnt_x atau cnt_y tidak ditemukan dalam dataset.")

# Heatmap korelasi antar variabel di dataset harian
st.subheader("Korelasi Antar Variabel di Dataset Harian")
fig, ax = plt.subplots(figsize=(10,6))
sns.heatmap(numeric_df_day.drop(columns=['instant'], errors='ignore').corr(), annot=True, cmap="coolwarm", fmt=".2f", ax=ax)
st.pyplot(fig)

# Pola penggunaan berdasarkan waktu
st.subheader("Pola Penggunaan Sepeda")
time_options = ["hr", "weekday_x", "season_x"]
option = st.selectbox("Pilih faktor waktu", time_options)

fig = px.box(df_all, x=option, y="cnt_x", title=f"Distribusi Penyewaan Berdasarkan {option.capitalize()}", color=option)
st.plotly_chart(fig)

# Tren harian penyewaan sepeda
st.subheader("Tren Penyewaan Sepeda Harian")
df_all['date'] = pd.to_datetime(df_all['dteday'], errors='coerce')
df_all = df_all.dropna(subset=['date'])
daily_rentals = df_all.groupby('date')['cnt_x'].sum().reset_index()
fig = px.line(daily_rentals, x='date', y='cnt_x', title='Tren Penyewaan Sepeda Harian')
st.plotly_chart(fig)

# Rata-rata penyewaan sepeda berdasarkan jam
st.subheader("Rata-rata Penyewaan Sepeda Berdasarkan Jam")
fig, ax = plt.subplots(figsize=(10,6))
sns.lineplot(data=df_hour, x="hr", y="cnt", estimator='mean', ci=None)
plt.title("Rata-rata Penyewaan Sepeda Berdasarkan Jam")
plt.xlabel("Jam")
plt.ylabel("Jumlah Penyewaan")
plt.xticks(range(0,24))
plt.grid()
st.pyplot(fig)

# Tren penyewaan sepeda berdasarkan tahun
df_day['yr'] = df_day['yr'].map({0: 2011, 1: 2012})
yearly_rentals = df_day.groupby('yr')['cnt'].sum().reset_index()
fig, ax = plt.subplots(figsize=(8,5))
ax.bar(yearly_rentals['yr'], yearly_rentals['cnt'], color=['blue', 'green'])
plt.xlabel('Tahun')
plt.ylabel('Total Penyewaan Sepeda')
plt.title('Total Penyewaan Sepeda per Tahun')
plt.xticks(yearly_rentals['yr'])
st.pyplot(fig)

st.write("Dasbor ini membantu memahami faktor yang mempengaruhi jumlah penyewaan sepeda serta pola penggunaannya berdasarkan waktu.")
st.caption('Copyright © AGIL ARYANUSA')
