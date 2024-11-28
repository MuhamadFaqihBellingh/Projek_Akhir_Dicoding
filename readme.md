# Projek Akhir Dicoding - Dashboard Visualisasi Data Bike Sharing

Dibuat oleh: **Muhamad Faqih**  
Mahasiswa Universitas Terbuka

## Deskripsi
Proyek ini adalah sebuah aplikasi dashboard visualisasi data untuk **Bike Sharing**. Menggunakan data sepeda yang dikumpulkan untuk analisis dan visualisasi, aplikasi ini dibuat dengan menggunakan **Streamlit**.

## Fitur
- Menampilkan visualisasi data menggunakan grafik.
- Interaksi dengan berbagai filter untuk eksplorasi data lebih dalam.
- Aplikasi yang responsif dan mudah digunakan untuk menganalisis data bike sharing.

## Teknologi yang Digunakan
- **Python 3.9.20**
- **Streamlit**: Framework untuk membuat aplikasi web interaktif.
- **Pandas**: Untuk manipulasi dan analisis data.
- **Matplotlib** / **Seaborn**: Untuk visualisasi data.
- **Conda**: Manajer paket untuk lingkungan virtual.

## Persyaratan
Sebelum menjalankan aplikasi ini, pastikan Anda telah menginstal **Conda** dan menyiapkan lingkungan virtual.

### Instalasi dan Menjalankan Proyek

### 1. Clone Repository
Clone repository ini ke komputer lokal Anda:
```bash
git clone https://github.com/MuhamadFaqihBellingh/Projek_Akhir_Dicoding.git
cd Projek_Akhir_Dicoding

### 2. Mengaktifkan Virtual Environment dengan Anaconda

conda create --name main-ds python=3.9.20
conda activate main-ds
pip install -r requirements.txt

streamlit run dashboard.py

### Penjelasan:
- **Clone Repository**: Langkah pertama untuk meng-clone repository menggunakan Git.
- **Membuat dan Mengaktifkan Virtual Environment**: Langkah untuk membuat environment **`main-ds`** dengan Python 3.9.20 menggunakan Conda.
- **Instalasi Dependensi**: Menginstal dependensi yang diperlukan untuk aplikasi.
- **Menjalankan Aplikasi**: Menjalankan aplikasi **Streamlit** dengan perintah `streamlit run`.
