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
        df = pd.read_csv(csv_path)
        # Pastikan Attrition dalam format string untuk legenda grafik yang lebih baik
        df['Status_Attrition'] = df['Attrition'].map({1: 'Leave', 0: 'Stay'})
        return df
    return None

df_raw = load_data()

# --- 3. PREPARASI DATA BENCHMARK (HASIL ANALISA NOTEBOOK) ---
summary_data = {
    'Fitur': ['Gaji (Monthly)', 'Usia', 'Jarak Rumah', 'Pengalaman', 'Kepuasan'],
    'Tersembunyi (Senior)': [5560, 37, 12.4, 11, 2.50],
    'Terdeteksi (Junior)': [2489, 29, 7.0, 4, 2.14]
}
df_analysis = pd.DataFrame(summary_data)

# --- 4. SIDEBAR: INPUT DATA ---
st.sidebar.header("📋 Panel Kendali HR")
st.sidebar.write("Gunakan panel ini untuk simulasi risiko individu.")

if df_raw is not None:
    list_id = df_raw['EmployeeId'].unique().tolist()
    id_terpilih = st.sidebar.selectbox("Cari ID Karyawan", options=list_id)
    
    row = df_raw[df_raw['EmployeeId'] == id_terpilih].iloc[0]
    d_gaji = int(row.get('MonthlyIncome', 4500))
    d_usia = int(row.get('Age', 35))
    d_jarak = int(row.get('DistanceFromHome', 12))
    d_pengalaman = int(row.get('TotalWorkingYears', 10))
    d_kepuasan = int(row.get('JobSatisfaction', 2))
else:
    id_terpilih, d_gaji, d_usia, d_jarak, d_pengalaman, d_kepuasan = 0, 4500, 35, 12, 10, 2

with st.sidebar.form("form_prediksi"):
    st.write(f"**Simulasi untuk ID: {id_terpilih}**")
    gaji = st.number_input("Gaji Bulanan ($)", value=d_gaji)
    usia = st.slider("Usia (Tahun)", 18, 60, d_usia)
    jarak = st.slider("Jarak Rumah (Km)", 1, 30, d_jarak)
    pengalaman = st.number_input("Total Pengalaman (Thn)", value=d_pengalaman)
    kepuasan = st.select_slider("Tingkat Kepuasan", options=[1, 2, 3, 4], value=d_kepuasan)
    btn_predict = st.form_submit_button("Analisis Risiko Karyawan")

# --- 5. HEADER UTAMA ---
st.title("📊 HR Strategic Dashboard: Deteksi Risiko Attrition")
st.markdown("""
Dashboard ini menyajikan analisis **Multivariate** untuk memahami faktor pendorong karyawan meninggalkan perusahaan, 
serta mendeteksi profil **'Hidden Risk'** yang sering luput dari sistem konvensional.
""")
st.markdown("---")

# --- 6. BAGIAN EDA MULTIVARIATE (REVISI DICODING) ---
st.subheader("🔍 Wawasan Strategis: Apa yang Membuat Mereka Pergi?")
col_a, col_b, col_c = st.columns(3)

if df_raw is not None:
    with col_a:
        # Analisis Multivariate: Lembur vs Attrition
        fig_ot = px.histogram(df_raw, x="OverTime", color="Status_Attrition", 
                             barmode="group", title="Pengaruh Lembur terhadap Attrition",
                             color_discrete_map={'Leave': '#EF553B', 'Stay': '#636EFA'})
        st.plotly_chart(fig_ot, use_container_width=True)
        st.caption("Insight: Karyawan dengan jam lembur tinggi memiliki proporsi keluar yang lebih besar.")

    with col_b:
        # Analisis Multivariate: Departemen vs Attrition
        fig_dept = px.histogram(df_raw, x="Department", color="Status_Attrition", 
                               barmode="group", title="Tingkat Attrition per Departemen",
                               color_discrete_map={'Leave': '#EF553B', 'Stay': '#636EFA'})
        st.plotly_chart(fig_dept, use_container_width=True)
        st.caption("Insight: Divisi Sales menunjukkan dinamika turnover yang paling tinggi.")

    with col_c:
        # Analisis Multivariate: Gaji vs Attrition
        fig_box = px.box(df_raw, x="Status_Attrition", y="MonthlyIncome", 
                        color="Status_Attrition", title="Distribusi Gaji vs Status Attrition",
                        color_discrete_map={'Leave': '#EF553B', 'Stay': '#636EFA'})
        st.plotly_chart(fig_box, use_container_width=True)
        st.caption("Insight: Karyawan yang keluar cenderung berada di rentang gaji bawah.")

st.markdown("---")

# --- 7. LOGIKA HASIL PREDIKSI INDIVIDU ---
if btn_predict:
    st.subheader(f"📑 Hasil Analisis Individu (ID: {id_terpilih})")
    
    target_benchmark = 'Tersembunyi (Senior)' if gaji > 4000 else 'Terdeteksi (Junior)'
    
    if gaji > 4000 and usia > 32 and jarak > 10:
        st.error(f"⚠️ **PERINGATAN KRITIS:** Karyawan mendekati profil **'{target_benchmark}'**.")
        st.write(f"**Analisis:** Karyawan senior ini memiliki risiko keluar akibat faktor **Burnout Laten** (Jarak rumah {jarak}km) meskipun gaji memadai.")
    elif gaji < 3000 and usia < 30:
        st.warning(f"🟡 **RISIKO TERDETEKSI:** Karyawan sesuai dengan pola **'{target_benchmark}'**.")
        st.write("**Analisis:** Profil junior yang rentan berpindah demi percepatan karier atau kenaikan gaji.")
    else:
        st.success(f"✅ **PROFIL STABIL:** Karyawan berada dalam zona risiko rendah.")

    # Grafik Head-to-Head
    df_head = df_analysis[['Fitur', target_benchmark]].copy()
    df_head[f"ID {id_terpilih}"] = [gaji, usia, jarak, pengalaman, kepuasan]
    df_plot_head = df_head.melt(id_vars='Fitur', var_name='Kategori', value_name='Nilai')

    fig_compare = px.bar(df_plot_head[df_plot_head['Fitur'] != 'Gaji (Monthly)'], 
                        x='Fitur', y='Nilai', color='Kategori', barmode='group',
                        title="Perbandingan Faktor Risiko Laten (Usia, Jarak, Pengalaman)",
                        color_discrete_map={f"ID {id_terpilih}": '#00CC96', target_benchmark: '#EF553B'})
    st.plotly_chart(fig_compare, use_container_width=True)

# --- 8. TABEL ANALISA & REKOMENDASI ---
st.markdown("---")
col_t, col_r = st.columns([1.5, 1])

with col_t:
    st.subheader("📑 Benchmark Karakteristik (TP vs FN)")
    formatted_df = df_analysis.set_index('Fitur').style.format("{:,.2f}")
    st.table(formatted_df)

with col_r:
    st.subheader("💡 Strategi Retensi")
    st.markdown("""
    1. **Fleksibilitas (Senior):** Tawarkan kebijakan *Hybrid Work* untuk rumah >10km.
    2. **Career Enrichment:** Rotasi peran untuk mencegah kejenuhan pada masa kerja 4-5 thn.
    3. **Mentorship (Junior):** Program bimbingan untuk meningkatkan loyalitas karyawan muda.
    """)

# --- 9. TERMINOLOGI ---
with st.expander("ℹ️ Memahami Istilah: Tersembunyi (Senior) vs Terdeteksi (Junior)"):
    st.markdown("""
    * **Terdeteksi (Junior):** Karyawan muda, gaji rendah. Pola attrition mereka terekam jelas di sistem.
    * **Tersembunyi (Senior):** Karyawan mapan, gaji tinggi. Risiko mereka sering 'tidak terlihat' (Blind Spot) karena dianggap loyal, padahal rentan keluar karena beban perjalanan atau kejenuhan.
    """)