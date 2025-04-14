📊 Dasbor Analisis Penyewaan Sepeda

📌 Deskripsi

Aplikasi ini adalah dasbor interaktif berbasis Streamlit yang digunakan untuk menganalisis pola penyewaan sepeda berdasarkan dataset harian (day.csv) dan per jam (hour.csv). Dasbor ini menampilkan berbagai visualisasi untuk membantu memahami faktor-faktor yang memengaruhi jumlah penyewaan sepeda.

🚀 Fitur Utama

Menampilkan Dataset: Menampilkan data harian dan per jam dalam bentuk tabel interaktif.
Heatmap Korelasi: Memvisualisasikan hubungan antar variabel dalam dataset harian.
Analisis Pola Waktu:
1. Rata-rata penyewaan sepeda berdasarkan jam.
2. Pola penyewaan berdasarkan hari dalam minggu.
3. Pola penyewaan berdasarkan musim.


🛠️ Instalasi dan Menjalankan Aplikasi
0. python -m venv venv
1. pip install pandas
2. pip install numpy
3. pip install matplotlib
4. pip install seaborn
5. pip install streamlit
6. pip install plotly.express

Run
python -m streamlit run dasbord.py

📊 Contoh Visualisasi

Heatmap Korelasi: Menampilkan hubungan antar variabel.
Tren Penyewaan per Jam: Memvisualisasikan jumlah penyewaan berdasarkan jam dalam sehari.
Penyewaan Berdasarkan Hari dan Musim: Memahami pola penggunaan sepeda berdasarkan hari dan musim.


💻 Dibuat oleh Agil Aryanusa