import streamlit as st
import pandas as pd
import plotly.express as px
import os

# --- 1. KONFIGURASI HALAMAN ---
st.set_page_config(page_title="HR Attrition Insights Dashboard", layout="wide")

# --- 2. LOAD DATA DARI CSV ---
@st.cache_data
# def load_data():
#     base_path = os.path.dirname(__file__)
#     csv_path = os.path.join(base_path, 'employee_data_cleaned.csv')
    
#     if os.path.exists(csv_path):
#         df = pd.read_csv(csv_path)
#         df['Status_Attrition'] = df['Attrition'].map({1: 'Leave', 0: 'Stay'})
#         return df
#     return None
# @st.cache_data
# def load_data():
#     # Mengambil path absolut dari file dashboard.py berada
#     base_path = os.path.dirname(os.path.abspath(__file__))
#     # Menggabungkan dengan nama file (asumsi CSV satu folder dengan script)
#     csv_path = os.path.join(base_path, 'employee_data_cleaned.csv')
    
#     if os.path.exists(csv_path):
#         df = pd.read_csv(csv_path)
#         df['Status_Attrition'] = df['Attrition'].map({1: 'Leave', 0: 'Stay'})
#         return df
#     else:
#         st.error(f"File tidak ditemukan di: {csv_path}")
#     return None
@st.cache_data
def load_data():
    # Mengambil path absolut dari file dashboard.py berada
    base_path = os.path.dirname(os.path.abspath(__file__))
    # Menggabungkan dengan nama file (asumsi CSV satu folder dengan script)
    csv_path = os.path.join(base_path, 'employee_data_cleaned.csv')
    
    if os.path.exists(csv_path):
        df = pd.read_csv(csv_path)
        df['Status_Attrition'] = df['Attrition'].map({1: 'Leave', 0: 'Stay'})
        return df
    else:
        st.error(f"File tidak ditemukan di: {csv_path}")
    return None
    
df_raw = load_data()

# --- 3. PREPARASI DATA BENCHMARK ---
summary_data = {
    'Fitur': ['Gaji (Monthly)', 'Usia', 'Jarak Rumah', 'Pengalaman', 'Kepuasan'],
    'Tersembunyi (Senior)': [5560, 37, 12.4, 11, 2.50],
    'Terdeteksi (Junior)': [2489, 29, 7.0, 4, 2.14]
}
df_analysis = pd.DataFrame(summary_data)

# --- 4. SIDEBAR: INPUT DATA ---
st.sidebar.header("📋 Panel Kendali HR")

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

# --- 5. FUNGSI POP-UP HASIL ANALISIS (MODAL) ---
@st.dialog("🔍 Hasil Analisis Detail")
def tunjukkan_hasil(id_emp, gaji_val, usia_val, jarak_val, exp_val, sat_val):
    target_benchmark = 'Tersembunyi (Senior)' if gaji_val > 4000 else 'Terdeteksi (Junior)'
    
    # Header Pesan
    if gaji_val > 4000 and usia_val > 32 and jarak_val > 10:
        st.error(f"⚠️ **PERINGATAN KRITIS:** ID {id_emp} mendekati profil **'{target_benchmark}'**.")
    elif gaji_val < 3000 and usia_val < 30:
        st.warning(f"🟡 **RISIKO TERDETEKSI:** ID {id_emp} sesuai pola **'{target_benchmark}'**.")
    else:
        st.success(f"✅ **PROFIL STABIL:** ID {id_emp} berada dalam zona risiko rendah.")

    # Grafik Head-to-Head dalam Pop-up
    df_head = df_analysis[['Fitur', target_benchmark]].copy()
    df_head[f"ID {id_emp}"] = [gaji_val, usia_val, jarak_val, exp_val, sat_val]
    df_plot_head = df_head.melt(id_vars='Fitur', var_name='Kategori', value_name='Nilai')

    fig_comp = px.bar(df_plot_head[df_plot_head['Fitur'] != 'Gaji (Monthly)'], 
                     x='Fitur', y='Nilai', color='Kategori', barmode='group',
                     title="Analisis Faktor Risiko Laten",
                     color_discrete_map={f"ID {id_emp}": '#00CC96', target_benchmark: '#EF553B'})
    
    # Menggunakan width='stretch' sesuai log error Ibu
    st.plotly_chart(fig_comp, width='stretch')
    
    st.info("💡 **Rekomendasi:** Fokus pada keseimbangan kerja dan tantangan baru bagi profil ini.")

# --- 6. HEADER UTAMA ---
st.title("📊 HR Strategic Dashboard: Deteksi Risiko Attrition")
st.markdown("---")

# --- 7. BAGIAN EDA MULTIVARIATE (REVISI DICODING) ---
st.subheader("🔍 Wawasan Strategis: Analisis Hubungan Fitur & Attrition")
col_a, col_b, col_c = st.columns(3)

if df_raw is not None:
    with col_a:
        fig_ot = px.histogram(df_raw, x="OverTime", color="Status_Attrition", barmode="group",
                             title="OverTime vs Attrition", color_discrete_map={'Leave': '#EF553B', 'Stay': '#636EFA'})
        st.plotly_chart(fig_ot, width='stretch')

    with col_b:
        fig_dept = px.histogram(df_raw, x="Department", color="Status_Attrition", barmode="group",
                               title="Dept vs Attrition", color_discrete_map={'Leave': '#EF553B', 'Stay': '#636EFA'})
        st.plotly_chart(fig_dept, width='stretch')

    with col_c:
        fig_box = px.box(df_raw, x="Status_Attrition", y="MonthlyIncome", color="Status_Attrition",
                        title="Income vs Attrition", color_discrete_map={'Leave': '#EF553B', 'Stay': '#636EFA'})
        st.plotly_chart(fig_box, width='stretch')

# --- 8. PEMANGGILAN POP-UP ---
if btn_predict:
    tunjukkan_hasil(id_terpilih, gaji, usia, jarak, pengalaman, kepuasan)

# --- 9. TABEL ANALISA & REKOMENDASI ---
st.markdown("---")
col_t, col_r = st.columns([1.5, 1])

with col_t:
    st.subheader("📑 Benchmark Karakteristik (TP vs FN)")
    st.table(df_analysis.set_index('Fitur').style.format("{:,.2f}"))

with col_r:
    st.subheader("💡 Strategi Retensi")
    st.markdown("""
    1. **Fleksibilitas (Senior):** Kebijakan *Hybrid Work* (>10km).
    2. **Career Enrichment:** Rotasi peran pada masa kerja 4-5 thn.
    3. **Mentorship (Junior):** Program bimbingan untuk loyalitas.
    """)

with st.expander("ℹ️ Memahami Istilah: Tersembunyi (Senior) vs Terdeteksi (Junior)"):
    st.markdown("Analisis ini membedakan karyawan yang keluar karena faktor finansial (Junior) atau faktor kenyamanan kerja (Senior).")