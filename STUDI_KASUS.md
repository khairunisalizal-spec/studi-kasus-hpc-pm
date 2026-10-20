# Studi Kasus: Estimasi PM2.5 sebagai Tantangan Lokal dengan Dukungan Komputasi

## 1. Latar belakang
Kualitas udara merupakan persoalan lokal yang dipengaruhi oleh berbagai faktor, termasuk kondisi cuaca dan aktivitas manusia. Materi kuliah *Global Infrastructure to Address Local Challenge with HPC* menjelaskan bahwa sumber daya komputasi berkinerja tinggi dapat membantu peneliti menyelesaikan persoalan nyata, termasuk prakiraan kualitas udara PM2.5. Salah satu contoh yang disebut dalam resume adalah penggunaan superkomputer LANTA di Thailand.

## 2. Rumusan masalah
Bagaimana membuat prototipe sederhana yang memperkirakan kadar PM2.5 berdasarkan beberapa variabel lingkungan, sekaligus menunjukkan bagaimana analisis data dapat dikembangkan lebih lanjut dengan infrastruktur HPC?

## 3. Tujuan
Membuat aplikasi web sederhana berbasis Python yang melatih model regresi linear dari dataset contoh, menampilkan metrik evaluasi, dan menerima input pengguna untuk menghasilkan estimasi PM2.5.

## 4. Data dan batasan
Data yang disertakan dalam proyek ini merupakan **data sintetis yang dibuat untuk demonstrasi**, bukan data pengukuran aktual. Variabel yang digunakan adalah suhu (°C), kelembapan (%), kecepatan angin (m/s), indeks lalu lintas (0–100), serta PM2.5 (µg/m³) sebagai target. Karena datanya sintetis, hasil model tidak dapat dianggap sebagai gambaran kondisi udara nyata di Thailand atau wilayah lain.

## 5. Metode implementasi
Program membaca data CSV, memisahkan fitur dan target, membagi data menjadi 80% data latih dan 20% data uji, kemudian melatih model `LinearRegression` dari scikit-learn. Kinerja dievaluasi dengan Mean Absolute Error (MAE) dan koefisien determinasi (R²). Aplikasi Flask menyediakan halaman web dan endpoint `/api/predict` untuk mengirim input dari formulir HTML ke model Python.

## 6. Peran HPC
Pada demonstrasi ini, komputasi berjalan di komputer biasa. HPC menjadi relevan jika skala pekerjaan bertambah: misalnya ribuan sensor, data satelit beresolusi tinggi, banyak titik geografis, simulasi atmosfer, atau eksperimen model yang dijalankan paralel. HPC bukan sekadar komputer yang cepat; penggunaannya perlu disertai pembagian kerja, pengelolaan data, validasi ilmiah, dan kolaborasi dengan pakar lingkungan.

## 7. Hasil yang diharapkan
Pengguna dapat memasukkan kondisi contoh dan memperoleh nilai estimasi dari model yang sudah dilatih. Halaman juga menampilkan metrik evaluasi model. Nilai metrik hanya menjelaskan performa pada data sintetis yang disediakan; angka tersebut tidak membuktikan kemampuan memprediksi kondisi udara nyata.

## 8. Kesimpulan
Proyek ini menerapkan gagasan utama materi kuliah, yaitu memanfaatkan komputasi untuk membantu memahami tantangan lokal. Prototipe menunjukkan alur dasar pengolahan data, pelatihan model, evaluasi, dan penyajian hasil melalui web. Agar bermanfaat secara nyata, proyek harus menggunakan data valid, evaluasi yang sesuai, serta masukan dari ahli kualitas udara. Infrastruktur HPC dapat mendukung tahap lanjutan ketika data dan kompleksitas simulasi meningkat.
