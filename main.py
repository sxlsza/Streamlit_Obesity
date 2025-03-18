import streamlit as st
import numpy as np
import pickle

model = pickle.load(open('model_obesitas.pkl', 'rb'))

MTRANS_options = {0: "Jalan Kaki", 1: "Kendaraan Umum", 2: "Sepeda", 3: "Sepeda Motor", 4: "Mobil Pribadi"}
NCP_options = {1: "Jarang", 2: "Normal", 3: "Sering", 4: "Sangat Sering"}
CAEC_options = {1: "Tidak Pernah", 2: "Selalu", 3: "Sering", 4: "Kadang"}
CALC_options = {1: "Tidak Pernah", 2: "Selalu", 3: "Sering", 4: "Kadang"}
SCC_options = {0: "Tidak", 1: "Ya"}

st.title("Prediksi Tingkat Obesitas")
st.write("Aplikasi ini memprediksi tingkat obesitas berdasarkan gaya hidup dan riwayat kesehatan.")

gender = st.radio("Jenis Kelamin", options=[0,1], format_func=lambda x: "Perempuan" if x == 0 else "Laki-laki")
age = st.number_input("Masukkan Usia:", min_value=1, max_value=100, value=25, step=1)
height = st.number_input("Masukkan Tinggi Badan (meter):", min_value=1.0, max_value=2.5, value=1.7)
weight = st.number_input("Masukkan Berat Badan (kg):", min_value=30.0, max_value=200.0, value=70.0)
family_history = st.radio("Apakah ada riwayat obesitas di keluarga?", [0,1], format_func=lambda x: "Tidak" if x == 0 else "Ya")
FAVC = st.radio("Apakah sering makan makanan berkalori tinggi?", [0,1], format_func=lambda x: "Tidak" if x == 0 else "Ya")
FCVC = st.number_input("Seberapa sering makan sayur dalam sehari? (1: Jarang, 2: Kadang, 3: Sering)", min_value=1.0, max_value=3.0, value=2.0)
NCP = st.selectbox("Frekuensi Makan dalam Sehari:", options=list(NCP_options.keys()), format_func=lambda x: NCP_options[x])
CAEC = st.selectbox("Kebiasaan Makan Camilan:", options=list(CAEC_options.keys()), format_func=lambda x: CAEC_options[x])
CH2O = st.number_input("Konsumsi Air Putih (liter per hari):", min_value=0.0, max_value=5.0, value=2.0)
SCC = st.radio("Apakah Anda Menghitung Asupan Kalori?", [0, 1], format_func=lambda x: SCC_options[x])
SMOKE = st.radio("Apakah Anda Merokok?", [0, 1], format_func=lambda x: "Tidak" if x == 0 else "Ya")
FAF = st.slider("Frekuensi Aktivitas Fisik (0-3):", min_value=0, max_value=3, value=2)
TUE = st.number_input("Waktu Penggunaan Teknologi per Hari (jam):", min_value=0.0, max_value=16.0, value=2.0)
CALC = st.selectbox("Frekuensi Konsumsi Alkohol:", options=list(CALC_options.keys()), format_func=lambda x: CALC_options[x])
MTRANS = st.selectbox("Moda Transportasi Utama:", options=list(MTRANS_options.keys()), format_func=lambda x: MTRANS_options[x])

if st.button("Prediksi"):    
    data_baru = np.array([
        gender, age, height, weight, family_history, FAVC, FCVC, NCP, CAEC, SMOKE, CH2O, SCC, FAF, TUE, CALC, MTRANS
    ]).reshape(1, -1)
    
    prediksi = model.predict(data_baru)
    
    kategori_obesitas = {
        0: "Underweight",
        1: "Normal",
        2: "Overweight Level I",
        3: "Overweight Level II",
        4: "Obesity Type I",
        5: "Obesity Type II",
        6: "Obesity Type III"
    }
    
    hasil_prediksi = kategori_obesitas.get(prediksi[0], "Kategori tidak dikenali")
    st.success(f"Hasil Prediksi: {hasil_prediksi}")



