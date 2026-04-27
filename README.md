# Proyek Akhir: Menyelesaikan Permasalahan Perusahaan Edutech

## Business Understanding

# Jelaskan latar belakang bisnis dari perushaan tersebut.
🏢 Profil dan Latar Belakang Bisnis
Perusahaan ini merupakan sebuah entitas korporasi modern berskala besar yang beroperasi di sektor teknologi dan riset. Perusahaan memiliki struktur organisasi yang kompleks dengan fokus utama pada inovasi dan pelayanan pelanggan.

1. Struktur Organisasi dan Operasional
Berdasarkan data, perusahaan ini terbagi menjadi tiga departemen utama yang menjadi pilar bisnisnya:

- Research & Development (R&D): Departemen terbesar yang menunjukkan bahwa perusahaan sangat bergantung pada inovasi produk dan pengembangan teknologi.

- Sales: Divisi ujung tombak yang memastikan penetrasi pasar dan pendapatan perusahaan tetap stabil.

- Human Resources (HR): Divisi pendukung yang mengelola lebih dari 1.000 karyawan untuk menjaga stabilitas internal.

2. Diversitas Tenaga Kerja (Talent Pool)
Perusahaan memiliki tenaga kerja yang sangat beragam dalam hal latar belakang pendidikan dan spesialisasi, mulai dari bidang Life Sciences, Medical, Marketing, hingga Technical Degree. Ini menunjukkan bahwa perusahaan menjalankan bisnis yang membutuhkan keahlian teknis tinggi (misalnya: manufaktur alat medis, farmasi, atau teknologi laboratorium).

3. Dinamika Lingkungan Kerja
Bisnis perusahaan ditandai dengan mobilitas dan ritme kerja yang dinamis:

- Business Travel: Karyawan sering melakukan perjalanan bisnis (Travel_Rarely hingga Travel_Frequently), yang menunjukkan perusahaan memiliki jaringan klien atau cabang yang luas.

- Overtime (Lembur): Adanya budaya kerja lembur di beberapa posisi mencerminkan tekanan target atau proyek riset dengan deadline ketat.

- Career Progression: Terdapat tingkatan jabatan yang jelas (Job Level 1 sampai 5), dari staf pelaksana hingga manajer senior.

### Permasalahan Bisnis

# Tuliskan seluruh permasalahan bisnis yang akan diselesaikan.

Rumusan Permasalahan Bisnis (Business Problem Statements)
Permasalahan utama yang dihadapi perusahaan bukan sekadar jumlah karyawan yang keluar, melainkan ketidakmampuan sistem dalam membedakan profil risiko yang berdampak pada kerugian aset manusia yang berharga. Secara detail, permasalahan tersebut mencakup:

1. Prediksi Kehilangan Karyawan (Attrition Prediction)
Masalah mendasar adalah bagaimana perusahaan dapat memprediksi secara akurat apakah seorang karyawan akan mengundurkan diri atau bertahan. Tanpa model prediksi, perusahaan bersifat reaktif—hanya bertindak setelah surat pengunduran diri diterima—yang berujung pada biaya rekrutmen dan pelatihan ulang yang tinggi.

2. Identifikasi Faktor Penyebab Attrition (Causal Factors Identification)
Perusahaan sering kali gagal memahami alasan sebenarnya di balik pengunduran diri. Masalah ini terbagi menjadi dua fokus utama yang selaras dengan temuan data:

- Masalah pada Profil Junior (Risiko Terdeteksi): Mengapa karyawan muda dengan gaji tingkat awal cenderung memiliki tingkat perputaran (turnover) yang tinggi? Apakah faktor finansial merupakan satu-satunya pemicu?

- Masalah pada Profil Senior (Risiko Tersembunyi/Blind Spot): Mengapa karyawan berpengalaman dengan gaji tinggi (rata-rata $5.560) tetap memilih untuk keluar? Perusahaan memiliki masalah dalam mendeteksi pemicu non-finansial seperti beban perjalanan (Jarak Rumah) dan stagnansi peran yang tidak tertangkap oleh survei kepuasan standar.

3. Kegagalan Deteksi Dini pada Aset Bernilai Tinggi (High-Value Talent Loss)
Terdapat kesenjangan (gap) di mana model prediksi atau manajemen sering kali menganggap karyawan senior "aman" karena posisi dan kemapanannya. Permasalahan bisnisnya adalah bagaimana mendeteksi karyawan yang berada di zona kepuasan "moderat" (skor 2,50) yang sebenarnya menyimpan keinginan laten untuk keluar namun tidak terdeteksi oleh radar HR konvensional.

4. Inefisiensi Strategi Retensi (Non-Targeted Interventions)
Permasalahan terakhir adalah pemberian solusi yang tidak tepat sasaran. Perusahaan sering memberikan kenaikan gaji untuk mencegah attrition, padahal bagi kelompok senior, masalah utamanya adalah kelelahan fisik akibat jarak rumah. Permasalahan bisnisnya adalah menentukan siapa yang membutuhkan kebijakan Hybrid Work dan siapa yang membutuhkan program Career Enrichment.

### Cakupan Proyek

# Tuliskan cakupan proyek yang akan dikerjakan.
1. Tujuan Utama (Objective)
    - Membangun model prediktif untuk menentukan probabilitas seorang karyawan akan mengundurkan diri (Attrition).

    - Melakukan analisis mendalam untuk mengidentifikasi variabel atau faktor pendorong utama (key drivers) yang menyebabkan karyawan meninggalkan perusahaan.

2. Data dan Variabel yang Terlibat
Proyek ini akan mengolah dataset karyawan dengan rincian variabel sebagai berikut:

- Variabel Target: Label biner Attrition, di mana nilai 1 merepresentasikan karyawan yang keluar dan nilai 0 merepresentasikan karyawan yang bertahan.

- Fitur Prediktor:

    * Fitur Numerik: Meliputi aspek demografi dan finansial seperti usia (Age), pendapatan bulanan (MonthlyIncome), jarak rumah ke kantor (DistanceFromHome), serta indikator loyalitas seperti total masa kerja (TotalWorkingYears) dan lama bekerja di perusahaan (YearsAtCompany).

    * Fitur Kategorikal: Meliputi aspek operasional dan status karyawan seperti frekuensi perjalanan bisnis (BusinessTravel), departemen, peran pekerjaan (JobRole), status pernikahan, dan keberadaan kerja lembur (OverTime).

3. Batasan dan Pembersihan Data (Data Cleaning & Filtering)
Untuk menjaga integritas dan relevansi model, proyek ini akan mengeksklusi variabel yang tidak memiliki variansi (konstan) atau tidak memberikan nilai informasi bagi model prediktif, antara lain:

- EmployeeCount (seluruh nilai bernilai 1).

- Over18 (seluruh nilai bernilai "Y").

- StandardHours (seluruh nilai bernilai 80).

### Persiapan

1. Sumber Data (Data Source)
Data yang digunakan dalam proyek ini berasal dari dataset internal perusahaan yang telah dibersihkan, dengan detail sebagai berikut:

Nama File: employee_data_cleaned.csv

Format: CSV (Comma Separated Values)

Ukuran Data: 1.058 baris dengan 32 kolom (fitur).

Deskripsi: Dataset ini berisi informasi komprehensif mengenai profil karyawan, termasuk metrik demografi, performa, tingkat kepuasan, dan status pengunduran diri (attrition).

Setup environment:

Tentu, penjelasan Anda sangat bagus karena mencakup alur kerja nyata dari tahap riset hingga tahap publikasi (deployment). Penjelasan ini menunjukkan bahwa Anda memahami proses Data Science secara utuh.

Berikut adalah versi kalimat yang lebih rapi dan profesional untuk bab Setup Environment di laporan Anda, berdasarkan cerita yang Anda sampaikan:

2. Setup Environment
Dalam pengembangan proyek ini, lingkungan kerja (environment) disusun melalui beberapa tahap, mulai dari pengolahan data hingga publikasi dashboard:

- Platform Analisis: Proses analisis data awal, pembersihan, hingga pembuatan model prediksi dilakukan menggunakan Google Colab. Tahap ini menghasilkan file data final yang diberi nama employee_data_cleaned.csv.

- Editor Kode: Pembuatan kode aplikasi dashboard dilakukan menggunakan Visual Studio Code (VS Code) di perangkat lokal, dengan memanfaatkan fitur Terminal terintegrasi untuk menjalankan pengujian aplikasi secara real-time.

- Sumber Data: Sesuai dengan spesifikasi proyek dari Dicoding, seluruh analisis wajib menggunakan dataset yang telah disediakan. File employee_data_cleaned.csv digunakan sebagai sumber data utama yang dibaca oleh aplikasi dashboard.

- Deployment: Setelah aplikasi berjalan dengan baik di lingkungan lokal, kode diunggah ke repositori GitHub dan dipublikasikan secara daring menggunakan Streamlit Community Cloud, sehingga dapat diakses melalui URL: https://a590proyekpertama-ana.streamlit.app/.

Pustaka (Library) yang Digunakan:
Untuk menjalankan proyek ini, diperlukan instalasi beberapa pustaka Python berikut:

* Instalasi library utama melalui terminal
pip install streamlit pandas plotly scikit-learn imbalanced-learn

## Business Dashboard

# Jelaskan tentang business dashboard yang telah dibuat. Jika ada, sertakan juga link untuk mengakses dashboard tersebut.

## Business Dashboard

Dashboard yang dikembangkan dalam proyek ini terdiri dari dua platform utama untuk memberikan wawasan komprehensif bagi departemen HR:

### 1. Metabase Business Dashboard (Kriteria Utama)
Dashboard ini dibuat menggunakan Metabase untuk memonitor faktor-faktor pendorong attrition secara makro. 
- **Fokus Utama:** Visualisasi hubungan antara lembur (OverTime), kepuasan kerja, dan pendapatan terhadap tingkat Attrition.
- **Akses Reviewer:** File database Metabase telah disertakan dalam lampiran pengiriman (`metabase.db.mv.db`) sesuai instruksi.
- **Kredensial Login:**
    - **Email:** ana.rosyidah24@gmail.com
    - **Password:** Rosyidah89

### 2. Streamlit HR Attrition Insights (Interactive Dashboard)
Sebagai alat bantu interaktif, dibuat pula dashboard berbasis Python Streamlit untuk deteksi risiko karyawan secara individual (Blind Spot Detection).
- **Link Akses:** https://a590proyekpertama-ana.streamlit.app/
- **Fitur Utama:** Simulasi risiko berdasarkan input parameter karyawan dan perbandingan benchmark terhadap profil Senior vs Junior.

## Conclusion

# Jelaskan konklusi dari proyek yang dikerjakan.

🏁 Konklusi Proyek: Analisis Blind Spot Attrition
Proyek ini berhasil mengembangkan sistem deteksi dini pengunduran diri karyawan yang tidak hanya melihat pola umum, tetapi juga mengungkap risiko laten pada aset berharga perusahaan. Berdasarkan analisis data dan hasil pemodelan, disimpulkan beberapa poin utama:

1. Pergeseran Paradigma Risiko (Senior vs Junior)
Proyek ini membuktikan bahwa risiko pengunduran diri tidak selalu berbanding lurus dengan gaji rendah.

- Profil Junior: Memiliki tingkat keluar yang tinggi namun mudah diprediksi karena polanya berkaitan erat dengan gaji awal dan usia muda.

- Profil Senior (High-Value): Merupakan Blind Spot utama. Mereka memiliki gaji tinggi (rata-rata $5.560) dan pengalaman matang (11 tahun), namun tetap berisiko keluar karena faktor non-finansial.

2. Jarak Rumah sebagai Pemicu "Burnout" Laten
Data menunjukkan variabel Jarak Rumah memiliki kontras yang sangat tinggi (+5,4 Km) antara kelompok senior yang keluar dibandingkan kelompok junior. Hal ini menyimpulkan bahwa bagi karyawan senior yang sudah mapan secara finansial, kenyamanan waktu dan fisik jauh lebih berharga daripada nominal gaji.

3. Keterbatasan Model Standar dan Skor Kepuasan
Ditemukan bahwa karyawan senior sering kali memberikan skor kepuasan di level "moderat" (rata-rata 2,50). Skor ini sering dianggap "aman" oleh sistem HR konvensional, padahal merupakan sinyal kejenuhan kerja atau stagnansi karier.

4. Efektivitas Rekomendasi Strategis
Sebagai tindak lanjut dari proyek ini, perusahaan disarankan untuk beralih dari strategi retensi berbasis uang ke strategi berbasis kualitas hidup, seperti:

- Implementasi Hybrid Work khusus untuk menekan risiko kelelahan akibat jarak rumah yang jauh.

- Program Career Enrichment untuk memberikan tantangan baru bagi karyawan berpengalaman agar tidak terjebak dalam rutinitas.

- Pelaksanaan Stay Interview yang proaktif sebelum karyawan mencapai titik jenuh di masa kerja 4-5 tahun.

### Rekomendasi Action Items (Optional)

Berikan beberapa rekomendasi action items yang harus dilakukan perusahaan guna menyelesaikan permasalahan atau mencapai target mereka.

- Fleksibilitas Kerja: Bagi kelompok senior yang memiliki jarak rumah jauh (>12 km), pertimbangkan kebijakan kerja dikantor dan dirumah (hybrid work) untuk mengurangi faktor kelelahan fisik.
- Pengayaan Karier (Career Enrichment): Jangan hanya mengandalkan kenaikan gaji. Karyawan senior membutuhkan tantangan baru atau rotasi posisi untuk mengatasi kejenuhan kerja.
- Pendekatan Proaktif (Proactive Engagement): Tetap Lakukan wawancara (stay interview) khusus bagi karyawan dengan masa kerja 4—5 tahun (titik jenuh kelompok senior), meskipun skor kepuasan mereka terlihat berada di level rata-rata.
