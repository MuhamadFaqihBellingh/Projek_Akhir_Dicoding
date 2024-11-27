import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Menambahkan judul dan informasi pribadi
st.title("Dashboard Visualisasi Data Bike Sharing")
st.markdown("Dibuat oleh **Muhamad Faqih** Mahasiswa **Universitas Terbuka**")

# Memuat data CSV
@st.cache_data
def load_data():
    return pd.read_csv('main_data.csv')

bikes_df = load_data()

# Menentukan Pertanyaan Bisnis
st.subheader('Pertanyaan Bisnis:')
st.markdown("""
- Apa pengaruh cuaca (weather_condition) terhadap jumlah penyewaan sepeda (total_rentals)?
- Bagaimana pola penyewaan sepeda berubah sepanjang jam (hour) antara pengguna kasual dan pengguna terdaftar?
""")

# 1. Pengaruh Cuaca terhadap Penyewaan Sepeda
st.subheader('Pengaruh Cuaca terhadap Penyewaan Sepeda')
plt.figure(figsize=(8, 6))
sns.barplot(x='weather_condition', y='total_rentals', data=bikes_df, palette='Blues')
plt.title('Pengaruh Cuaca terhadap Penyewaan Sepeda')
plt.xlabel('Kondisi Cuaca')
plt.ylabel('Total Penyewaan Sepeda')
st.pyplot(plt)

# 2. Pola Penyewaan Sepeda Berdasarkan Jam
st.subheader('Perbandingan Penyewaan oleh Pengguna Kasual dan Terdaftar')

# Visualisasi Perbandingan Penyewaan Sepeda oleh Pengguna Kasual dan Terdaftar
plt.figure(figsize=(8, 6))
sns.barplot(x='day_of_week', y='total_rentals', hue='is_working_day', data=bikes_df)

# Menambahkan judul dan label
plt.title('Perbandingan Penyewaan oleh Pengguna Kasual dan Terdaftar', fontsize=14)
plt.xlabel('Hari', fontsize=12)
plt.ylabel('Total Penyewaan Sepeda', fontsize=12)

# Menampilkan plot di Streamlit
st.pyplot(plt)

# Ringkasan Statistik Data
st.subheader('Ringkasan Statistik Data')
selected_column = st.selectbox('Pilih Kolom untuk Menampilkan Statistik Deskriptif', bikes_df.columns)
st.write(f"Statistik Deskriptif untuk kolom: {selected_column}")
st.write(bikes_df[selected_column].describe())

# Filter Data berdasarkan Season dan Weather Condition
season_input = st.selectbox('Pilih Season', bikes_df['season'].unique())
weather_input = st.selectbox('Pilih Weather Condition', bikes_df['weather_condition'].unique())
filtered_data = bikes_df[(bikes_df['season'] == season_input) & (bikes_df['weather_condition'] == weather_input)]

# Statistik Deskriptif untuk data yang difilter
st.write(f"Statistik Deskriptif untuk data Season {season_input} dan Weather Condition {weather_input}:")
st.write(filtered_data[selected_column].describe())

# Visualisasi Penyewaan Berdasarkan Jam setelah Filter
fig, ax = plt.subplots(figsize=(10, 6))
sns.lineplot(x='hour', y='total_rentals', data=filtered_data, ax=ax, marker='o')
ax.set_title('Total Rentals per Hour (Filtered Data)')
ax.set_xlabel('Hour')
ax.set_ylabel('Total Rentals')
st.pyplot(fig)

# Visualisasi Total Penyewaan Berdasarkan Musim
st.subheader("Total Penyewaan Berdasarkan Musim")
season_counts = bikes_df.groupby('season')['total_rentals'].sum().reset_index()
fig, ax = plt.subplots(figsize=(8, 6))
sns.barplot(x='season', y='total_rentals', data=season_counts, ax=ax)
ax.set_title("Total Penyewaan Berdasarkan Musim")
ax.set_xlabel("Musim")
ax.set_ylabel("Total Penyewaan")
st.pyplot(fig)

# Jumlah Entri Berdasarkan Casual dan Registered Users
st.subheader('Jumlah Entri Berdasarkan Casual dan Registered Users')
casual_counts = bikes_df['casual_users'].value_counts()
registered_counts = bikes_df['registered_users'].value_counts()

# Visualisasi jumlah entri berdasarkan Casual Users
fig, ax = plt.subplots(figsize=(8, 6))
sns.barplot(x=casual_counts.index, y=casual_counts.values, ax=ax, palette='Blues_d')
ax.set_title('Jumlah Entri Berdasarkan Casual Users')
ax.set_xlabel('Jumlah Casual Users')
ax.set_ylabel('Jumlah Entri')
st.pyplot(fig)

# Visualisasi jumlah entri berdasarkan Registered Users
fig, ax = plt.subplots(figsize=(8, 6))
sns.barplot(x=registered_counts.index, y=registered_counts.values, ax=ax, palette='Greens_d')
ax.set_xlabel('Jumlah Registered Users')
ax.set_ylabel('Jumlah Entri')
st.pyplot(fig)
