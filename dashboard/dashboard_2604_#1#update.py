import streamlit as st
import pandas as pd
import plotly.express as px
import os

# --- KONFIGURASI HALAMAN ---
st.set_page_config(page_title="HR Attrition Insights", layout="wide")

# --- LOAD DATA DARI CSV ---
@st.cache_data # Menggunakan cache agar aplikasi lebih cepat saat dimuat ulang
def load_data():
    # Mengambil path file secara dinamis agar aman dijalankan di komputer mana pun
    base_path = os.path.dirname(__file__)
    csv_path = os.path.join(base_path, 'employee_data_cleaned.csv')
    
    if os.path.exists(csv_path):
        return pd.read_csv(csv_path)
    else:
        st.error(f"File {csv_path} tidak ditemukan! Pastikan file CSV ada di folder 'dashboard'.")
        return None

df_raw = load_data()

# --- HEADER ---
st.title("📊 Business Insight: Analisis Blind Spot Attrition")
st.markdown("Dashboard ini menganalisis mengapa beberapa karyawan keluar tanpa terdeteksi oleh sistem.")
st.markdown("---")

if df_raw is not None:
    # --- PENGOLAHAN DATA OTOMATIS ---
    # Catatan: Kita asumsikan data yang di-load adalah data hasil evaluasi model 
    # (mengandung kolom target dan prediksi untuk menghitung FN & TP secara real-time)
    # Namun, agar tetap sesuai dengan kesimpulan sebelumnya, kita gunakan dataset ringkasan:
    
    summary_data = {
        'Fitur Utama': ['Gaji (Monthly)', 'Usia', 'Jarak Rumah', 'Pengalaman', 'Kepuasan'],
        'Profil Tersembunyi (FN)': [5560, 37, 12.4, 11, 2.50], # Rata-rata dari data asli
        'Profil Terdeteksi (TP)': [2489, 29, 7.0, 4, 2.14],
        'Satuan': ['$', 'Thn', 'Km', 'Thn', 'Skor']
    }
    df_analysis = pd.DataFrame(summary_data)
    df_analysis['Tingkat Kontras'] = df_analysis['Profil Tersembunyi (FN)'] - df_analysis['Profil Terdeteksi (TP)']

    # --- BAGIAN 1: METRIK UTAMA (Highlight) ---
    m1, m2, m3 = st.columns(3)
    with m1:
        st.metric("Risk: Gaji Tinggi", "$5.560", "+$3.071 vs TP", delta_color="inverse")
    with m2:
        st.metric("Risk: Karyawan Senior", "37 Tahun", "+8 Tahun vs TP", delta_color="inverse")
    with m3:
        st.metric("Risk: Jarak Jauh", "12.4 Km", "+5.4 Km vs TP", delta_color="inverse")

    # --- BAGIAN 2: TABEL & VISUALISASI ---
    st.subheader("🔍 Perbandingan Detail Karakteristik")
    
    col_table, col_chart = st.columns([1, 1])

    with col_table:
        st.dataframe(df_analysis[['Fitur Utama', 'Profil Tersembunyi (FN)', 'Profil Terdeteksi (TP)', 'Tingkat Kontras']], 
                     use_container_width=True, hide_index=True)

    with col_chart:
        # Visualisasi Gaji secara terpisah karena skalanya ribuan
        df_salary = df_analysis[df_analysis['Fitur Utama'] == 'Gaji (Monthly)']
        fig_salary = px.bar(df_salary, x='Fitur Utama', y=['Profil Tersembunyi (FN)', 'Profil Terdeteksi (TP)'],
                            barmode='group', text_auto='.2s', title="Kontras Gaji Bulanan",
                            color_discrete_sequence=['#EF553B', '#636EFA'])
        st.plotly_chart(fig_salary, use_container_width=True)

    # Visualisasi Fitur Lainnya (Usia, Jarak, Pengalaman)
    df_others = df_analysis[df_analysis['Fitur Utama'].isin(['Usia', 'Jarak Rumah', 'Pengalaman'])]
    fig_others = px.bar(df_others, x='Fitur Utama', y=['Profil Tersembunyi (FN)', 'Profil Terdeteksi (TP)'],
                        barmode='group', text_auto=True, title="Faktor Demografi & Masa Kerja",
                        color_discrete_sequence=['#EF553B', '#636EFA'])
    st.plotly_chart(fig_others, use_container_width=True)

    # --- BAGIAN 3: ANALISIS & STRATEGI ---
    st.markdown("---")
    st.subheader("💡 Mengapa Model Mengalami 'Blind Spot'?")

    c1, c2 = st.columns(2)
    with c1:
        st.info("**1. Kelompok Terdeteksi (Profil Junior)**\n\nKaryawan muda dengan gaji entry-level. Pola keluarnya mudah dibaca karena faktor finansial dan 'job hopping'.")
    with c2:
        st.warning("**2. Kelompok Tersembunyi (Profil High-Value)**\n\nKaryawan senior yang mapan. Mereka keluar bukan karena uang, tapi karena stagnansi dan kelelahan perjalanan.")

    # --- BAGIAN 4: REKOMENDASI ---
    st.markdown("### 🚀 Rekomendasi Strategis untuk HR")
    tab1, tab2, tab3 = st.tabs(["Fleksibilitas", "Pengembangan Karier", "Deteksi Dini"])
    
    with tab1:
        st.write("Berikan opsi **Hybrid Work** untuk karyawan senior dengan jarak rumah >10km.")
    with tab2:
        st.write("Fokus pada **Internal Mobility** bagi karyawan dengan masa kerja 4-5 tahun (titik jenuh FN).")
    with tab3:
        st.write("Gunakan fitur tambahan seperti **Lembur** untuk memperkuat model deteksi pada profil senior.")

    st.markdown("> **📌 Kesimpulan Akhir:** Risiko terbesar perusahaan ada pada 'Silent Attrition' dari karyawan bernilai tinggi yang luput dari deteksi sistem.")