# Studi Kasus HPC: Estimasi PM2.5 untuk Tantangan Kualitas Udara Lokal

Proyek pembelajaran yang terinspirasi dari materi kuliah **“Global Infrastructure to Address Local Challenge with HPC”**. Contoh kasusnya adalah estimasi kadar PM2.5 berdasarkan suhu, kelembapan, kecepatan angin, dan indeks lalu lintas.

> **Penting:** `data/pm25_demo.csv` berisi **data sintetis/dummy**, bukan pengukuran Thailand atau data resmi. Aplikasi ini bukan sistem prakiraan operasional dan tidak untuk keputusan kesehatan. Hubungan yang dipelajari sangat sederhana dan tidak mewakili model atmosfer sungguhan.

## Isi proyek
- `app.py` — backend Python Flask, melatih model regresi linear, mengevaluasi model, dan menyediakan endpoint prediksi.
- `templates/index.html` — antarmuka web berpalet cokelat.
- `data/pm25_demo.csv` — contoh data sintetis.
- `requirements.txt` — pustaka Python yang dibutuhkan.

## Studi kasus
Sebuah tim lokal ingin memahami bagaimana faktor cuaca dan lalu lintas berkaitan dengan PM2.5. Infrastruktur HPC dapat membantu ketika analisis diperluas ke data sensor berskala besar, citra satelit, banyak wilayah, atau simulasi atmosfer yang mahal. Prototipe ini memakai dataset kecil agar alur kerja dasarnya dapat dipelajari di laptop.

### Alur implementasi
1. Mengumpulkan fitur cuaca dan lalu lintas serta label PM2.5.
2. Membagi data menjadi data latih dan data uji.
3. Melatih model `LinearRegression`.
4. Mengukur hasil menggunakan MAE dan R².
5. Memasukkan kondisi contoh melalui halaman web untuk memperoleh estimasi.
6. Dalam proyek nyata, data harus diganti dengan data sensor/instansi yang tervalidasi, diuji lintas waktu dan lokasi, serta dibandingkan dengan model yang sesuai.

## Menjalankan secara lokal
Disarankan Python 3.10 atau lebih baru.

```bash
# 1. Buat dan aktifkan virtual environment (opsional tetapi disarankan)
python -m venv .venv

# Windows PowerShell
.venv\\Scripts\\Activate.ps1

# macOS/Linux
source .venv/bin/activate

# 2. Instal dependensi
pip install -r requirements.txt

# 3. Jalankan aplikasi
python app.py
```

Buka alamat yang ditampilkan Flask, biasanya `http://127.0.0.1:5000`.

## Mengunggah ke GitHub
1. Buat repositori baru di GitHub, misalnya `studi-kasus-hpc-pm25`.
2. Ekstrak ZIP ini, lalu buka terminal di folder proyek.
3. Jalankan:

```bash
git init
git add .
git commit -m "Tambah studi kasus estimasi PM2.5 berbasis Python"
git branch -M main
git remote add origin https://github.com/USERNAME/studi-kasus-hpc-pm25.git
git push -u origin main
```

Ganti `USERNAME` dengan nama akun GitHub dan sesuaikan URL repositori. Jangan mengunggah token/password GitHub.

## Hubungan dengan materi HPC
Proyek ini **bukan aplikasi HPC sungguhan** karena dataset dan modelnya kecil. Hubungannya adalah contoh alur pemecahan masalah lokal dengan komputasi dan analisis data. Pada skala HPC, pekerjaan serupa dapat dikembangkan dengan data berukuran besar, pemrosesan paralel, simulasi kualitas udara, dan kolaborasi antara pengelola infrastruktur serta pakar lingkungan.

## Pengembangan lanjutan
- Gunakan data PM2.5 resmi dan dokumentasikan sumber serta lisensinya.
- Tambahkan validasi berbasis waktu dan bandingkan beberapa model.
- Catat versi data/model dan pantau error prediksi.
- Jika memakai HPC, dokumentasikan sumber daya komputasi, waktu eksekusi, dan manfaat paralelisasi.
