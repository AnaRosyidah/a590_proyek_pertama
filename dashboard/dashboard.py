import streamlit as st
import pandas as pd
import plotly.express as px
import os

# --- 1. KONFIGURASI HALAMAN ---
st.set_page_config(page_title="HR Attrition Insights Dashboard", layout="wide")

# --- 2. LOAD DATA DARI CSV ---
@st.cache_data
def load_data():
    base_path = os.path.dirname(__file__)
    csv_path = os.path.join(base_path, 'employee_data_cleaned.csv')
    
    if os.path.exists(csv_path):
        return pd.read_csv(csv_path)
    else:
        # Jika file tidak di folder yang sama, coba cari di folder utama
        return None

df_raw = load_data()

# --- 3. PREPARASI DATA BENCHMARK (HASIL ANALISA) ---
summary_data = {
    'Fitur': ['Gaji (Monthly)', 'Usia', 'Jarak Rumah', 'Pengalaman', 'Kepuasan'],
    'Tersembunyi (Senior)': [5560, 37, 12.4, 11, 2.50],
    'Terdeteksi (Junior)': [2489, 29, 7.0, 4, 2.14]
}
df_analysis = pd.DataFrame(summary_data)
df_melted = df_analysis.melt(id_vars='Fitur', var_name='Kelompok', value_name='Nilai')

# --- 4. SIDEBAR: MENU INPUT PREDIKSI ---
st.sidebar.header("📋 Input Data Karyawan")
st.sidebar.write("Pilih ID Karyawan untuk memuat data otomatis.")

# 1. Siapkan daftar ID Karyawan
if df_raw is not None:
    # Menggunakan EmployeeId karena kolom Nama tidak ada
    list_id = df_raw['EmployeeId'].unique().tolist()
else:
    list_id = [0]

# 2. Selectbox ID Karyawan
id_terpilih = st.sidebar.selectbox("Cari ID Karyawan", options=list_id)

# 3. Ambil data default berdasarkan ID yang dipilih
if df_raw is not None and id_terpilih in df_raw['EmployeeId'].values:
    row = df_raw[df_raw['EmployeeId'] == id_terpilih].iloc[0]
    
    # Mengambil data asli dari kolom CSV
    d_gaji = int(row.get('MonthlyIncome', 4500))
    d_usia = int(row.get('Age', 35))
    d_jarak = int(row.get('DistanceFromHome', 12))
    d_pengalaman = int(row.get('TotalWorkingYears', 10))
    d_kepuasan = int(row.get('JobSatisfaction', 2))
else:
    d_gaji, d_usia, d_jarak, d_pengalaman, d_kepuasan = 4500, 35, 12, 10, 2

# 4. Form Input
with st.sidebar.form("form_prediksi"):
    nama = st.text_input("ID Karyawan Terpilih", value=f"ID: {id_terpilih}", disabled=True)
    
    gaji = st.number_input("Gaji Bulanan ($)", value=d_gaji)
    usia = st.slider("Usia (Tahun)", 18, 60, d_usia)
    jarak = st.slider("Jarak Rumah (Km)", 1, 30, d_jarak)
    pengalaman = st.number_input("Total Pengalaman (Thn)", value=d_pengalaman)
    kepuasan = st.select_slider("Tingkat Kepuasan", options=[1, 2, 3, 4], value=d_kepuasan)
    
    btn_predict = st.form_submit_button("Cek Risiko Sekarang")
    
# --- 5. HEADER UTAMA ---
st.title("📊 HR Business Insight: Analisis Blind Spot Attrition")
st.markdown("Dashboard ini mendeteksi karyawan yang berisiko keluar namun sering luput dari sistem (Blind Spot).")
st.markdown("---")

# --- 6. LOGIKA HASIL PREDIKSI (Jika Tombol Diklik) ---# --- 6. LOGIKA HASIL PREDIKSI (Perbaikan Grafik Komparatif) ---
if btn_predict:
    st.subheader(f"🔍 Hasil Analisis untuk: {nama}")
    
    # Menentukan Kelompok Benchmark yang relevan
    # Jika gaji > 4000, dia dibandingkan dengan profil Senior, jika tidak dengan Junior
    target_benchmark = 'Tersembunyi (Senior)' if gaji > 4000 else 'Terdeteksi (Junior)'
    
    # 1. Pesan Peringatan
    if gaji > 4000 and usia > 32 and jarak > 10:
        st.error(f"⚠️ **PERINGATAN KRITIS:** {nama} mendekati profil **'{target_benchmark}'**.")
    elif gaji < 3000 and usia < 30:
        st.warning(f"🟡 **RISIKO TERDETEKSI:** {nama} sesuai dengan pola **'{target_benchmark}'**.")
    else:
        st.success(f"✅ **STABIL:** {nama} berada di bawah ambang batas risiko kelompoknya.")

    # --- PERBAIKAN VISUALISASI: HEAD-TO-HEAD COMPARISON ---
    
    # Ambil data individu dan benchmark yang relevan saja
    df_head_to_head = df_analysis[['Fitur', target_benchmark]].copy()
    df_head_to_head[nama] = [gaji, usia, jarak, pengalaman, kepuasan]
    
    # Melt untuk keperluan Plotly
    df_plot = df_head_to_head.melt(id_vars='Fitur', var_name='Kategori', value_name='Nilai')

    col1, col2 = st.columns(2)

    with col1:
        # Perbandingan Gaji (Skala Besar)
        fig_gaji = px.bar(
            df_plot[df_plot['Fitur'] == 'Gaji (Monthly)'],
            x='Kategori', y='Nilai', color='Kategori',
            title=f"Analisis Gaji: {nama} vs Rata-rata {target_benchmark}",
            text_auto='.2s',
            color_discrete_map={nama: '#00CC96', target_benchmark: '#EF553B'}
        )
        st.plotly_chart(fig_gaji, use_container_width=True)

    with col2:
        # Perbandingan Faktor Risiko Lain (Skala Kecil)
        fig_risiko = px.bar(
            df_plot[df_plot['Fitur'] != 'Gaji (Monthly)'],
            x='Fitur', y='Nilai', color='Kategori',
            barmode='group',
            title="Analisis Faktor Perilaku & Usia",
            color_discrete_map={nama: '#00CC96', target_benchmark: '#EF553B'}
        )
        st.plotly_chart(fig_risiko, use_container_width=True)

    # --- KESIMPULAN OTOMATIS BERDASARKAN SELISIH ---
    selisih_jarak = jarak - df_analysis.loc[df_analysis['Fitur'] == 'Jarak Rumah', target_benchmark].values[0]
    
    st.info(f"""
    **Insight Utama:** {nama} memiliki jarak rumah **{abs(selisih_jarak):.1f} km {'lebih jauh' if selisih_jarak > 0 else 'lebih dekat'}** dibandingkan rata-rata karyawan kelompok {target_benchmark} yang telah keluar. 
    Hal ini merupakan indikator penting dalam menentukan tingkat kelelahan (*burnout*) karyawan.
    """)
    
    # --- 6.1 KESIMPULAN DETAIL (Dinamis) ---
    st.write("### 📝 Kesimpulan Strategis")
    
    with st.container():
        # Kasus 1: Senior / Hidden Risk
        if gaji > 4000 and usia > 32 and jarak > 10:
            st.markdown(f"""
            **Analisis Profil:** {nama} adalah aset **High-Value (Senior)** bagi perusahaan. Meskipun secara finansial (Gaji: ${gaji:,}) terlihat sangat mapan, faktor risiko utama adalah **jarak rumah ({jarak} km)** yang cukup signifikan.
            
            **Potensi Blind Spot:** - Perusahaan sering menganggap karyawan seperti {nama} setia karena posisi dan gajinya. 
            - Namun, beban perjalanan harian dapat memicu kelelahan fisik (*burnout*) yang tidak terdeteksi oleh survei kepuasan standar.
            
            **Rekomendasi Utama:**
            - Segera tawarkan opsi kerja jarak jauh (*Work-from-Home*) atau jadwal fleksibel.
            - Lakukan diskusi empat mata mengenai rencana jangka panjang sebelum karyawan mencapai titik jenuh.
            """)
            
        # Kasus 2: Junior / Detected Risk
        elif gaji < 3000 and usia < 30:
            st.markdown(f"""
            **Analisis Profil:** {nama} termasuk dalam kategori **Junior/Entry-level**. Tingkat pengunduran diri pada kelompok ini secara historis memang tinggi (*predictable*).
            
            **Faktor Pendorong:** - Umumnya didorong oleh motivasi mencari kenaikan gaji signifikan atau percepatan karier di tempat lain.
            - Dengan usia {usia} tahun, motivasi eksplorasi karier masih sangat dominan.
            
            **Rekomendasi Utama:**
            - Berikan program bimbingan (*mentorship*) untuk meningkatkan keterikatan emosional dengan perusahaan.
            - Tinjau kembali struktur kenaikan gaji berkala agar tetap kompetitif di pasar.
            """)
            
        # Kasus 3: Karyawan Stabil
        else:
            st.markdown(f"""
            **Analisis Profil:** Saat ini, {nama} berada dalam profil **Karyawan Stabil**. Parameter gaji, usia, dan kenyamanan kerja berada pada titik keseimbangan yang baik.
            
            **Wawasan:** - Tidak ditemukan anomali yang menunjukkan tanda-tanda pengunduran diri dalam waktu dekat.
            - Tetap pantau skor kepuasan kerja (saat ini: {kepuasan}/4) agar tidak mengalami penurunan drastis.
            
            **Rekomendasi Utama:**
            - Pertahankan kondisi kerja saat ini. 
            - Libatkan dalam proyek-proyek strategis untuk menjaga motivasi jangka panjang.
            """)

# --- 7. TIGA GRAFIK VISUALISASI UTAMA ---
st.subheader("📈 Visualisasi Tren Attrition")
c1, c2 = st.columns(2)

with c1:
    # GRAFIK 1: Kontras Gaji
    df_salary = df_melted[df_melted['Fitur'] == 'Gaji (Monthly)']
    fig1 = px.bar(df_salary, x='Kelompok', y='Nilai', color='Kelompok',
                 title="1. Blind Spot Gaji: Senior vs Junior", text_auto='.2s',
                 color_discrete_sequence=['#EF553B', '#636EFA'])
    st.plotly_chart(fig1, use_container_width=True)

with c2:
    # GRAFIK 2: Demografi
    df_demo = df_melted[df_melted['Fitur'].isin(['Usia', 'Pengalaman'])]
    fig2 = px.bar(df_demo, x='Fitur', y='Nilai', color='Kelompok', barmode='group',
                 title="2. Profil Usia & Masa Kerja", text_auto=True)
    st.plotly_chart(fig2, use_container_width=True)

# GRAFIK 3: Line Chart Profil Perilaku
fig3 = px.line(df_melted[df_melted['Fitur'] != 'Gaji (Monthly)'], 
              x='Fitur', y='Nilai', color='Kelompok', markers=True,
              title="3. Pola Perilaku Laten (Jarak & Kepuasan)", line_shape="spline")
st.plotly_chart(fig3, use_container_width=True)

# --- 8. TABEL ANALISA & REKOMENDASI ---
st.markdown("---")
col_t, col_r = st.columns([1.5, 1])

with col_t:
    st.subheader("📑 Tabel Karakteristik Detail")
    
    # Memformat angka agar lebih rapi:
    # - set_index('Fitur') agar kolom Fitur menjadi judul baris
    # - format("{:,.2f}") memberikan koma ribuan dan 2 angka desimal
    formatted_df = df_analysis.set_index('Fitur').style.format("{:,.2f}")
    
    st.table(formatted_df)

with col_r:
    st.subheader("💡 Strategi HR")
    st.markdown("""
    1. **Fleksibilitas:** Fokus pada karyawan rumah >10km.
    2. **Retensi Senior:** Gaji tinggi bukan jaminan loyalitas.
    3. **Stay Interview:** Lakukan pada masa kerja 4-5 tahun.
    """)

st.info("📌 **Kesimpulan:** Risiko terbesar adalah kehilangan karyawan senior berharga yang terlihat 'aman' di permukaan.")

# --- 9. PANDUAN TERMINOLOGI (TAMBAHAN) ---
with st.expander("ℹ️ Memahami Istilah: Tersembunyi vs Terdeteksi"):
    st.markdown("""
    ### 1. Attrition Terdeteksi (Profil Junior)
    * **Siapa mereka?** Karyawan tingkat awal (*entry-level*) atau Junior dengan usia di bawah 30 tahun dan gaji di bawah $3.000.
    * **Karakteristik:** Memiliki pola pengunduran diri yang dapat diprediksi oleh sistem karena faktor gaji dan jenjang karier singkat.
    * **Dampak Bisnis:** Risiko operasional yang cenderung mudah diantisipasi melalui rekrutmen rutin.

    ### 2. Attrition Tersembunyi (Profil Senior / High-Value)
    * **Siapa mereka?** Karyawan mapan dengan usia di atas 32 tahun dan gaji di atas $4.000.
    * **Mengapa disebut 'Tersembunyi'?** Karena indikator finansial mereka terlihat sangat stabil (gaji tinggi), sehingga sering dianggap 'aman' oleh manajemen.
    * **Faktor Risiko Laten:** Pemicu utama mereka keluar adalah faktor non-finansial, seperti **jarak rumah yang jauh (>10km)** yang memicu kelelahan fisik (*burnout*).
    * **Dampak Bisnis:** Risiko strategis yang sangat tinggi karena perusahaan kehilangan mentor, keahlian teknis mendalam, dan biaya penggantian yang sangat mahal.
    """)