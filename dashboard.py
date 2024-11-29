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
    return pd.read_csv('main.csv')

bikes_df = load_data()

# Agregasi jumlah penyewaan berdasarkan hari dalam seminggu
day_of_week_summary = bikes_df.groupby('day_of_week')['total_rentals'].sum().reset_index()

season_mapping = {
    1: "Spring",
    2: "Summer",
    3: "Fall",
    4: "Winter"
}
bikes_df['season'] = bikes_df['season'].replace(season_mapping)

weather_mapping = {
    1: "Clear",
    2: "Cloudy",
    3: "Rainy",
    4: "Snowy"
}

bikes_df['weather_condition'] = bikes_df['weather_condition'].replace(weather_mapping)


day_of_week_mapping = {
    0: "Monday",
    1: "Tuesday",
    2: "Wednesday",
    3: "Thursday",
    4: "Friday",
    5: "Saturday",
    6: "Sunday"
}
bikes_df['day_of_week'] = bikes_df['day_of_week'].replace(day_of_week_mapping)

month_mapping = {
    1: "January",
    2: "February",
    3: "March",
    4: "April",
    5: "May",
    6: "June",
    7: "July",
    8: "August",
    9: "September",
    10: "October",
    11: "November",
    12: "December"
}
bikes_df['month'] = bikes_df['month'].replace(month_mapping)
bikes_df['is_working_day'] = bikes_df['is_working_day'].replace({1: 'Work', 0: 'No-Work'})

# Filter Data untuk Musim
st.sidebar.subheader("Filter Data Berdasarkan Musim")
selected_season = st.sidebar.selectbox("Pilih Musim", options=bikes_df['season'].unique())
filtered_data = bikes_df[bikes_df['season'] == selected_season]

st.subheader(f"Data Penyewaan untuk Musim: {selected_season}")
st.dataframe(filtered_data)

# Statistik Deskriptif
st.subheader("Statistik Deskriptif")
st.write(filtered_data.describe())


# Visualisasi: Jumlah Penyewaan Berdasarkan Hari dalam Seminggu
st.subheader("Tren Penyewaan Berdasarkan Hari dalam Seminggu")
fig, ax = plt.subplots(figsize=(10, 6))
sns.barplot(x='day_of_week', y='total_rentals', data=day_of_week_summary, palette='Set2', ax=ax)
ax.set_title('Jumlah Penyewaan Sepeda Berdasarkan Hari dalam Seminggu')
ax.set_xlabel('Hari dalam Seminggu')
ax.set_ylabel('Jumlah Penyewaan Sepeda')
ax.set_xticklabels(ax.get_xticklabels(), rotation=45)
st.pyplot(fig)

# Visualisasi Penyewaan Sepeda oleh Casual vs Registered Users
st.subheader("Penyewaan Sepeda: Casual vs Registered Users")
casual_vs_registered = bikes_df.groupby(['casual_users', 'registered_users'])['total_rentals'].sum().reset_index()
fig, ax = plt.subplots(figsize=(10, 6))
sns.barplot(x='casual_users', y='total_rentals', data=casual_vs_registered, color='skyblue', ax=ax, label='Casual Users')
sns.barplot(x='registered_users', y='total_rentals', data=casual_vs_registered, color='orange', ax=ax, label='Registered Users')
ax.set_title('Perbandingan Penyewaan Sepeda: Casual vs Registered Users')
ax.set_xlabel('Jenis Pengguna')
ax.set_ylabel('Jumlah Penyewaan')
plt.legend()
st.pyplot(fig)

# Agregasi jumlah penyewaan berdasarkan status liburan
holiday_summary = bikes_df.groupby('is_holiday')['total_rentals'].sum().reset_index()

# Mengubah kolom is_holiday menjadi label yang lebih mudah dipahami
holiday_summary['is_holiday'] = holiday_summary['is_holiday'].map({0: 'Non-Holiday', 1: 'Holiday'})

# Visualisasi: Jumlah Penyewaan Berdasarkan Status Liburan
st.subheader("Jumlah Penyewaan Berdasarkan Status Liburan")
fig, ax = plt.subplots(figsize=(8, 6))
sns.barplot(x='is_holiday', y='total_rentals', data=holiday_summary, palette='RdBu', ax=ax)
ax.set_title('Jumlah Penyewaan Sepeda Berdasarkan Status Liburan')
ax.set_xlabel('Status Liburan')
ax.set_ylabel('Jumlah Penyewaan Sepeda')
st.pyplot(fig)

# Menampilkan Data Agregasi
st.subheader("Data Agregasi Berdasarkan Status Liburan")
st.write(holiday_summary)

# Agregasi jumlah penyewaan berdasarkan hari kerja
working_day_summary = bikes_df.groupby('is_working_day')['total_rentals'].sum().reset_index()

# Mengubah kolom is_working_day menjadi label yang lebih mudah dipahami
working_day_summary['is_working_day'] = working_day_summary['is_working_day'].map({0: 'Non-Working Day', 1: 'Working Day'})

# Misalnya 'working_day_summary' adalah dataframe yang sudah difilter dan diproses
working_day_summary = bikes_df.groupby('is_working_day')['total_rentals'].sum().reset_index()

# Visualisasi jumlah penyewaan berdasarkan hari kerja
st.subheader("Jumlah Penyewaan Berdasarkan Hari Kerja")
fig, ax = plt.subplots(figsize=(8, 6))
sns.barplot(x='is_working_day', y='total_rentals', data=working_day_summary, palette='Blues', ax=ax)
ax.set_title('Jumlah Penyewaan Sepeda Berdasarkan Hari Kerja')
ax.set_xlabel('Status Hari Kerja')
ax.set_ylabel('Jumlah Penyewaan Sepeda')
st.pyplot(fig)

# Menampilkan Data Agregasi
st.subheader("Data Agregasi Berdasarkan Hari Kerja")
st.write(working_day_summary)

# Statistik Deskriptif untuk Hari Kerja
st.subheader("Statistik Deskriptif Penyewaan Berdasarkan Hari Kerja")
st.write(bikes_df.groupby('is_working_day')['total_rentals'].describe())


# Validasi Kolom
if 'total_rentals' not in bikes_df.columns:
    st.error("Kolom 'total_rentals' tidak ditemukan dalam dataset.")
else:
    # Subheader
    st.subheader("Distribusi Total Penyewaan Sepeda")
    
    # Plot Distribusi
    fig, ax = plt.subplots(figsize=(8, 6))
    sns.histplot(bikes_df['total_rentals'], bins=30, kde=True, color='blue', ax=ax)
    ax.set_title('Distribusi Total Penyewaan Sepeda')
    ax.set_xlabel('Total Rentals')
    ax.set_ylabel('Frequency')
    st.pyplot(fig)
    
    # Statistik Dasar
    st.subheader("Statistik Dasar Total Penyewaan")
    stats = bikes_df['total_rentals'].describe()
    st.write(stats)

# Mapping Kolom Kategorik
season_mapping = {1: "Spring", 2: "Summer", 3: "Autumn", 4: "Winter"}
weather_mapping = {1: "Clear", 2: "Cloudy", 3: "Rainy"}
working_day_mapping = {0: "Non-Working Day", 1: "Working Day"}
holiday_mapping = {0: "Non-Holiday", 1: "Holiday"}
day_of_week_mapping = {0: "Monday", 1: "Tuesday", 2: "Wednesday", 3: "Thursday", 4: "Friday", 5: "Saturday", 6: "Sunday"}
year_mapping = {0: 2011, 1: 2012}

# Mapping kategori ke dataframe
bikes_df['season'] = bikes_df['season'].map(season_mapping)
bikes_df['weather_condition'] = bikes_df['weather_condition'].map(weather_mapping)
bikes_df['is_working_day'] = bikes_df['is_working_day'].map(working_day_mapping)
bikes_df['is_holiday'] = bikes_df['is_holiday'].map(holiday_mapping)
bikes_df['day_of_week'] = bikes_df['day_of_week'].map(day_of_week_mapping)
bikes_df['year'] = bikes_df['year'].map(year_mapping)

# Dropdown untuk memilih kategori
category = st.selectbox("Pilih Kategori Data:", ['Season', 'Weather Condition', 'Working Day', 'Holiday', 'Day of Week', 'Year'])

# Menampilkan data berdasarkan kategori yang dipilih
if category == 'Season':
    selected_data = bikes_df['season'].value_counts()
    
    # Membuat plot
    fig, ax = plt.subplots(figsize=(8, 6))
    sns.barplot(x=selected_data.index, y=selected_data.values, ax=ax, palette='Set2')
    ax.set_title('Jumlah Penyewaan Berdasarkan Season')
    ax.set_xlabel('Season')
    ax.set_ylabel('Jumlah Penyewaan')
    st.pyplot(fig)

elif category == 'Weather Condition':
    selected_data = bikes_df['weather_condition'].value_counts()

    # Membuat plot
    fig, ax = plt.subplots(figsize=(8, 6))
    sns.barplot(x=selected_data.index, y=selected_data.values, ax=ax, palette='coolwarm')
    ax.set_title('Jumlah Penyewaan Berdasarkan Weather Condition')
    ax.set_xlabel('Weather Condition')
    ax.set_ylabel('Jumlah Penyewaan')
    st.pyplot(fig)

elif category == 'Working Day':
    selected_data = bikes_df['is_working_day'].value_counts()

    # Membuat plot
    fig, ax = plt.subplots(figsize=(8, 6))
    sns.barplot(x=selected_data.index, y=selected_data.values, ax=ax, palette='Pastel1')
    ax.set_title('Jumlah Penyewaan Berdasarkan Working Day')
    ax.set_xlabel('Working Day (0 = Non-Working, 1 = Working)')
    ax.set_ylabel('Jumlah Penyewaan')
    st.pyplot(fig)

elif category == 'Holiday':
    selected_data = bikes_df['is_holiday'].value_counts()

    # Membuat plot
    fig, ax = plt.subplots(figsize=(8, 6))
    sns.barplot(x=selected_data.index, y=selected_data.values, ax=ax, palette='RdBu')
    ax.set_title('Jumlah Penyewaan Berdasarkan Holiday')
    ax.set_xlabel('Holiday (0 = Non-Holiday, 1 = Holiday)')
    ax.set_ylabel('Jumlah Penyewaan')
    st.pyplot(fig)

elif category == 'Day of Week':
    selected_data = bikes_df['day_of_week'].value_counts()

    # Membuat plot
    fig, ax = plt.subplots(figsize=(8, 6))
    sns.barplot(x=selected_data.index, y=selected_data.values, ax=ax, palette='Set2')
    ax.set_title('Jumlah Penyewaan Berdasarkan Day of Week')
    ax.set_xlabel('Day of Week')
    ax.set_ylabel('Jumlah Penyewaan')
    st.pyplot(fig)

elif category == 'Year':
    selected_data = bikes_df['year'].value_counts()

    # Membuat plot
    fig, ax = plt.subplots(figsize=(8, 6))
    sns.barplot(x=selected_data.index, y=selected_data.values, ax=ax, palette='viridis')
    ax.set_title('Jumlah Penyewaan Berdasarkan Year')
    ax.set_xlabel('Year')
    ax.set_ylabel('Jumlah Penyewaan')
    st.pyplot(fig)

    # Lisensi
st.sidebar.markdown("""
### Lisensi
Hak cipta © 2024 oleh Muhamad Faqih
""")

# Judul Dashboard
st.title("Analisis Penyewaan Sepeda")
st.markdown("""
Dashboard ini menyajikan kesimpulan dan rekomendasi berdasarkan pola penyewaan sepeda.  
Dikembangkan oleh **Muhamad Faqih**.
""")

# Seksi Kesimpulan
st.header("Kesimpulan dan Rekomendasi")
st.subheader("1. Pengaruh Liburan (Holiday)")
st.markdown("""
- **Kesimpulan**: Liburan (holiday) memengaruhi peningkatan penyewaan sepeda. Permintaan lebih tinggi di hari libur.  
- **Rekomendasi**:  
  - Pengelolaan armada sepeda dan promosi khusus untuk hari libur harus dilakukan.
  - Penyesuaian pada ketersediaan sepeda dan layanan sebaiknya dilakukan lebih awal.
""")

st.subheader("2. Penyewaan di Hari Kerja")
st.markdown("""
- **Kesimpulan**: Di hari kerja, sepeda lebih banyak digunakan untuk keperluan transportasi, terutama pada pagi dan sore hari.
- **Rekomendasi**:  
  - Pastikan ketersediaan sepeda pada jam-jam sibuk (pagi dan sore).  
  - Fokuskan promosi atau event pada hari libur untuk menarik lebih banyak pengguna casual.
""")

st.subheader("3. Tren Penyewaan Sepeda")
st.markdown("""
- **Kesimpulan**: Penyewaan sepeda cenderung meningkat dari tahun ke tahun, menunjukkan peningkatan kesadaran masyarakat.  
- **Rekomendasi**:  
  - Perencanaan jangka panjang diperlukan, termasuk:  
    - Penambahan jumlah sepeda.  
    - Penyempurnaan sistem operasional untuk mengikuti tren yang meningkat.
""")

st.subheader("4. Pola Penyewaan Berdasarkan Waktu dan Cuaca")
st.markdown("""
- **Kesimpulan**: Memahami pola penyewaan sepeda berdasarkan waktu (jam, hari, bulan, tahun) dan kondisi cuaca penting untuk pengelolaan.  
- **Rekomendasi**:  
  - Optimalkan ketersediaan sepeda pada:  
    - Jam sibuk, hari libur, dan periode dengan cuaca cerah.
""")

# Footer
st.markdown("""
---
Dashboard ini dirancang untuk membantu pengelola armada sepeda dalam memahami pola penyewaan dan membuat keputusan yang lebih tepat.  
Hak cipta © 2024 oleh Muhamad Faqih.
""")