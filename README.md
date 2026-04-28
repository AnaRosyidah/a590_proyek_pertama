# Proyek Akhir: Menyelesaikan Permasalahan Perusahaan Edutech

## Business Understanding

Kondisi dan Gambaran Umum Bisnis
Setelah mengeksplorasi dataset ini, saya melihat bahwa perusahaan yang sedang dianalisis adalah perusahaan teknologi dan riset dengan skala operasional yang cukup masif. Fokus utama bisnis mereka nampaknya terletak pada inovasi produk, yang terlihat dari besarnya porsi sumber daya manusia di bagian pengembangan.

1. Fokus Departemen dan Roda Bisnis
Dari data yang ada, operasional perusahaan bertumpu pada tiga pilar utama. Bagian Research & Development (R&D) menjadi jantung perusahaan dengan jumlah tim paling banyak, disusul oleh tim Sales yang bergerak di garis depan untuk menjaga pendapatan, serta Human Resources yang mengelola administrasi lebih dari seribu karyawan agar koordinasi internal tetap terjaga.

2. Karakteristik SDM dan Keahlian khusus
Karyawan di perusahaan ini bukan pekerja umum, melainkan tenaga ahli dengan latar belakang pendidikan yang sangat spesifik, seperti Life Sciences dan medis. Hal ini mengindikasikan bahwa bisnis yang dijalankan kemungkinan besar bergerak di industri yang sangat teknis, misalnya manufaktur perangkat kesehatan atau bidang farmasi.

3. Lingkungan Kerja dan Tekanan Operasional
Saya menemukan beberapa poin penting mengenai dinamika kerja sehari-hari di sini:

Mobilitas Tinggi: Perjalanan dinas sudah menjadi hal biasa bagi karyawan, baik yang sifatnya jarang maupun rutin. Ini menandakan perusahaan memiliki jaringan klien yang cukup luas.

Beban Kerja: Adanya catatan lembur di beberapa posisi menunjukkan bahwa tekanan pekerjaan cukup tinggi, mungkin karena target penjualan atau tenggat waktu riset yang ketat.

Struktur Karier: Perusahaan sudah memiliki jenjang karier yang tertata rapi dari level staf (Level 1) hingga posisi manajerial tertinggi (Level 5), yang artinya ada ruang bagi karyawan untuk terus naik jabatan.

### Permasalahan Bisnis

Identifikasi Masalah Bisnis
Masalah utama yang saya temukan bukan hanya soal banyaknya orang yang keluar, tapi perusahaan sepertinya "kecolongan" karena tidak bisa melihat siapa saja karyawan penting yang sebenarnya sudah tidak betah. Masalah ini bisa saya bagi menjadi beberapa poin:

1. Penanganan yang Terlambat (Sifatnya Reaktif)
Selama ini perusahaan baru bertindak setelah karyawan mengajukan surat resign. Ini sangat merugikan karena biaya untuk mencari dan melatih orang baru itu sangat mahal. Masalahnya adalah bagaimana kita bisa tahu lebih awal sebelum mereka benar-benar pergi.

2. Tidak Tahu Alasan Sebenarnya di Balik Resign
Perusahaan sering salah menebak alasan karyawan keluar. Dari data, ada dua kelompok yang alasannya bertolak belakang:

* Kelompok Junior: Apakah mereka keluar cuma karena gaji kecil, atau ada faktor lain yang membuat mereka tidak betah di awal karier?

* Kelompok Senior: Ini yang paling berbahaya. Mereka gajinya sudah besar (rata-rata $5.560), tapi tetap keluar. Ada masalah dalam mendeteksi pemicu selain uang, seperti capek karena rumahnya jauh atau merasa bosan dengan kerjaan yang itu-itu saja.

3. Salah Sangka Terhadap Karyawan Lama
Ada anggapan bahwa karyawan senior itu "aman" karena posisinya sudah mapan. Padahal, banyak dari mereka yang tingkat kepuasannya di level menengah (skor 2,50). Mereka tidak terlihat marah atau protes, tapi diam-diam berencana keluar. Masalahnya, sistem HR yang sekarang tidak bisa menangkap sinyal halus seperti ini.

4. Solusi yang Tidak Tepat Sasaran
Seringkali perusahaan hanya mengandalkan kenaikan gaji untuk menahan orang agar tidak resign. Padahal, untuk karyawan senior, uang bukan masalah utama, melainkan kelelahan fisik. Masalah bisnisnya adalah kita belum bisa membedakan siapa yang butuh kebijakan kerja fleksibel (hybrid) dan siapa yang butuh tantangan baru atau promosi.

### Cakupan Proyek

Sasaran dan Ruang Lingkup Proyek
1. Tujuan yang Ingin Dicapai
Dalam proyek ini, saya berfokus pada dua hal utama:

* Membuat Model Prediksi: Membangun sistem yang bisa menghitung seberapa besar kemungkinan seorang karyawan akan resign (Attrition) di masa depan.

* Mencari Faktor Penyebab: Melakukan bedah data untuk mengetahui variabel apa saja yang paling sering memicu karyawan untuk meninggalkan perusahaan (key drivers).

2. Data yang Digunakan
Analisis ini menggunakan data karyawan dengan pembagian sebagai berikut:

Target Analisis: Kolom Attrition, yang menjadi acuan utama (Nilai 1 untuk yang keluar, dan 0 untuk yang tetap bertahan).

Data Pendukung (Prediktor):

* Data Angka (Numerik): Saya akan melihat pengaruh umur, gaji bulanan, jarak dari rumah ke kantor, serta pengalaman kerja (total masa kerja dan lama bekerja di perusahaan ini).

* Data Kategori: Meliputi riwayat perjalanan dinas, departemen tempat bekerja, posisi/jabatan, status pernikahan, hingga ada atau tidaknya jam lembur.

3. Pembersihan dan Penyaringan Data
Agar hasil prediksinya akurat, saya telah menyaring data dan membuang kolom yang tidak berguna. Ada beberapa kolom yang isinya sama semua untuk seluruh karyawan sehingga tidak memberikan informasi apa pun dalam analisis, yaitu:

* EmployeeCount: Isinya hanya angka 1 di semua baris.

* Over18: Semua karyawan sudah dewasa (berusia di atas 18 tahun).

* StandardHours: Jam kerja standar semuanya sama, yaitu 80 jam.

### Persiapan

Persiapan
Pada tahap ini, saya akan menyiapkan yang dibutuhkan sebelum masuk ke inti analisis. Saya akan mulai dari menyiapkan data hasil pembersihan hingga mengatur database lokal dan visualisasi menggunakan Docker.

* Menyiapkan Data
Data utama yang digunakan dalam proyek ini adalah hasil dari proses pembersihan dan seleksi fitur yang telah dilakukan sebelumnya.

- Dataset Utama: employee_data.csv[https://github.com/dicodingacademy/dicoding_dataset/tree/main/employee]

- Detail: Dataset ini mencakup 1.058 entri karyawan dengan 32 parameter (fitur), mencakup data demografi, performa, hingga status attrition.

- Penyimpanan: File ini saya simpan di dalam direktori dashboard/ sebagai sumber data utama yang akan diproses lebih lanjut ke dalam database.

* Menyiapkan Environment Proyek
Untuk menjaga konsistensi pengerjaan, saya membagi proses ini menjadi analisis data di Google Colab dan pengelolaan database serta visualisasi di lingkungan lokal.

1. Instalasi Library (Requirements)
Saya menggunakan library spesifik agar proses manipulasi data dan pembuatan model machine learning tetap stabil. Berikut adalah daftar library yang perlu disiapkan:

pip install pandas==2.2.2 numpy==1.26.4 scipy==1.13.0 sqlalchemy==2.0.29
pip install matplotlib==3.8.4 seaborn==0.13.2 plotly==5.20.0
pip install scikit-learn==1.4.2 imbalanced-learn==0.12.2 joblib==1.4.0

2. Pengaturan Database dan Kontainerisasi
Agar integrasi data lebih rapi dan monitoring menjadi lebih luas, saya menggunakan kombinasi SQLite dan Docker:

* Database Karyawan (SQLite): Saya menggunakan SQLite untuk menyimpan data karyawan. Penggunaan SQLite dipilih karena ringan dan tidak memerlukan konfigurasi server yang rumit, namun tetap kuat saat diintegrasikan dengan SQLAlchemy di dalam kode Python.

* Monitoring dengan Metabase (Docker): Untuk keperluan visualisasi tambahan yang lebih dinamis, saya menjalankan Metabase melalui Docker.

* Persistent Data: Saya memastikan riwayat visualisasi tetap tersimpan aman di dalam database Metabase (metabase.db.mv.db) yang dikelola di dalam kontainer, sehingga data tidak hilang meskipun kontainer dimatikan.

Mengapa Alur Ini Digunakan?
Saya memilih menggunakan SQLite agar database bersifat portabel dan mudah dibaca langsung dari folder proyek. Sementara itu, penggunaan Docker saya khususkan untuk menjalankan Metabase agar saya memiliki alat analisis tambahan yang terpisah dari kode utama. Dengan cara ini, lingkungan kerja menjadi lebih terorganisir antara tempat menyimpan data (SQLite) dan alat untuk memantaunya (Metabase).

Sekarang semua alat dan bahan sudah siap! Selanjutnya, kita akan langsung masuk ke tahap Data Preparation untuk melihat bagaimana data ini diolah sebelum kita masuk ke tahap analisis yang lebih dalam.

## Business Dashboard

Dashboard yang dikembangkan dalam proyek ini terdiri dari dua platform utama untuk memberikan wawasan komprehensif bagi departemen HR:

### 1. Metabase Business Dashboard (Kriteria Utama)

Silakan ikuti langkah-langkah di bawah ini untuk menjalankan environment Metabase menggunakan Docker.

1. Spesifikasi Environment
Versi Metabase: v0.49.13

File Database: metabase.db.mv.db (Sudah disertakan dalam root folder proyek).

2. Langkah-Langkah Menjalankan
Buka terminal pada folder proyek, lalu jalankan perintah berikut secara berurutan:

A. Menarik Image Metabase (Pull Image)

* docker pull metabase/metabase:v0.49.13

B. Menjalankan Container Metabase

* docker run -d -p 3000:3000 --name metabase_check metabase/metabase:v0.49.13

C. Menyalin File Database ke Dalam Container
Agar dashboard yang telah dibuat dapat muncul, file database harus disalin ke dalam container yang sedang berjalan:

* docker cp metabase.db.mv.db metabase_check:/metabase.db/metabase.db.mv.db

D. Melakukan Restart Container
Restart diperlukan agar Metabase membaca file database yang baru saja disalin:
* docker restart metabase_check 
3. Akses Dashboard & Kredensial
Tunggu sekitar 1-2 menit hingga proses inisialisasi selesai, kemudian akses melalui browser di:

URL: http://localhost:3000
Username: ana.rosyidah24@gmail.com
Password: Rosyidah89


## ConclusionKesimpulan Akhir Proyek: Analisis Risiko Pengunduran Diri
Melalui proyek ini, saya berhasil memetakan alasan-alasan di balik keluarnya karyawan yang selama ini mungkin luput dari pengawasan manajemen. Analisis ini menunjukkan bahwa penyebab resign tidak sesederhana masalah gaji saja. Berikut adalah poin-poin kesimpulannya:

1. Perbedaan Karakteristik antara Karyawan Senior dan Junior
Temuan utama saya menunjukkan adanya perbedaan mencolok antara dua kelompok ini:

Kelompok Junior: Biasanya lebih mudah diprediksi karena alasan mereka keluar cukup umum, yaitu usia yang masih muda dan gaji yang masih di level awal.

Kelompok Senior: Ini adalah kelompok yang paling berisiko karena mereka sering dianggap loyal. Padahal, meski gaji mereka sudah tinggi (rata-rata di angka $5.560) dan sudah berpengalaman belasan tahun, mereka tetap memiliki keinginan untuk keluar karena faktor di luar uang.

2. Pengaruh Jarak Rumah terhadap Kelelahan Kerja
Data memperlihatkan adanya selisih jarak rumah yang cukup jauh (+5,4 Km) pada kelompok senior yang memilih keluar dibanding kelompok lainnya. Hal ini menandakan bahwa bagi mereka yang sudah mapan secara finansial, kenyamanan fisik dan efisiensi waktu perjalanan ke kantor jauh lebih penting daripada tambahan bonus atau gaji.

3. Skor Kepuasan yang Menipu
Saya menemukan bahwa karyawan senior cenderung memberikan nilai kepuasan di angka menengah (sekitar 2,50). Di mata perusahaan, angka ini sering dianggap aman-aman saja, padahal sebenarnya ini adalah sinyal bahwa mereka mulai jenuh atau merasa kariernya sudah tidak berkembang lagi (stagnan).

4. Usulan Perbaikan Strategi HR
Agar perusahaan tidak kehilangan talenta terbaiknya, saya menyarankan agar kebijakan penahanan karyawan (retention) tidak lagi hanya fokus pada kenaikan gaji, melainkan pada kualitas hidup, seperti:

* Penerapan Kerja Hybrid: Khusus untuk karyawan yang rumahnya jauh guna mengurangi stres di perjalanan.

* Tantangan Baru (Career Enrichment): Memberikan variasi tugas atau rotasi jabatan agar karyawan lama tidak merasa bosan.

* Wawancara Berkala: Melakukan diskusi pribadi secara proaktif, terutama saat karyawan memasuki masa kerja 4—5 tahun, sebelum mereka benar-benar mencapai titik jenuh.

### Rekomendasi Action Items (Optional)
Rekomendasi Tindakan untuk Perusahaan
Berdasarkan temuan dari data tersebut, saya menyarankan beberapa langkah nyata yang bisa segera diambil oleh tim manajemen dan HR:

* Penerapan Pola Kerja Hybrid: Untuk rekan-rekan di level senior yang tinggalnya cukup jauh dari kantor (di atas 12 km), perusahaan sebaiknya mulai menerapkan sistem kerja fleksibel. Mengurangi frekuensi perjalanan ke kantor bagi mereka akan sangat membantu menjaga kebugaran fisik dan mental, sehingga risiko keluar karena faktor kelelahan perjalanan bisa ditekan.

* Penyegaran Peran dan Tanggung Jawab: Kita tidak bisa hanya mengandalkan kenaikan gaji untuk menahan karyawan senior. Perlu ada program rotasi jabatan atau pemberian tanggung jawab pada proyek baru yang lebih menantang. Hal ini penting agar mereka tidak merasa terjebak dalam rutinitas yang membosankan setelah bekerja sekian lama.

* Diskusi Santai Berkala (Stay Interview): HR perlu lebih proaktif mengajak bicara karyawan yang sudah masuk masa kerja 4 hingga 5 tahun. Jangan menunggu mereka tidak puas dulu baru diajak diskusi. Seringkali kelompok ini terlihat stabil di permukaan, padahal sebenarnya mereka sudah berada di titik jenuh dan butuh didengarkan aspirasinya sebelum memutuskan untuk mencari peluang di tempat lain.
