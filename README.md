# 🐄 Deteksi Dini Penyakit Mata *Pink Eye* pada Sapi
### **Berbasis Citra Digital Menggunakan YOLOv4-Tiny**

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Framework-Flask-lightgrey.svg)](https://flask.palletsprojects.com/)
[![YOLOv4-Tiny](https://img.shields.io/badge/Model-YOLOv4--Tiny-green.svg)](https://github.com/AlexeyAB/darknet)
[![License](https://img.shields.io/badge/License-Academic-orange.svg)](#)

Aplikasi web ini merupakan **sistem deteksi dini penyakit mata Pink Eye** (*Infectious Bovine Keratoconjunctivitis*) pada sapi. Dikembangkan sebagai **Proyek Skripsi**, sistem ini memanfaatkan teknologi *Artificial Intelligence* (AI) untuk membantu peternak melakukan pemantauan kesehatan mata sapi secara cepat, otomatis, dan akurat melalui analisis citra digital.

---

## 📌 Latar Belakang
Penyakit **Pink Eye** merupakan infeksi mata menular yang umum menyerang ternak sapi. Dampak dari penyakit ini meliputi:
* **Penurunan Produktivitas:** Penurunan berat badan karena sapi mengalami nyeri saat makan.
* **Gangguan Penglihatan:** Risiko kebutaan permanen jika tidak ditangani segera.
* **Kerugian Ekonomi:** Biaya pengobatan yang besar bagi industri peternakan.

Sistem ini hadir sebagai solusi berbasis **Computer Vision** untuk mendeteksi gejala secara objektif tanpa harus mendatangkan ahli secara langsung di tahap awal.

---

## 🎯 Tujuan Sistem
1. **Otomatisasi:** Menggantikan pengecekan visual manual dengan sistem AI.
2. **Kecepatan:** Memberikan hasil deteksi dalam hitungan detik.
3. **Aksesibilitas:** Memudahkan peternak melalui antarmuka web yang sederhana dan responsif.

---

## 🧠 Metodologi & Teknologi

### **Metode Deteksi**
* **Algoritma:** YOLOv4-Tiny.
* **Inference Engine:** OpenCV DNN (Deep Neural Networks).
* **Alur:** Pre-processing -> Object Detection -> Non-Maximum Suppression (NMS) -> Output Visual.

### **Tech Stack**
* **Backend:** Python, Flask
* **AI/CV:** OpenCV, NumPy, Pillow
* **Frontend:** HTML5, Tailwind CSS

---

## 📂 Struktur Folder Project
```text
project-root/
├── app.py              # Logika utama Flask dan AI Inference
├── configs/            # File konfigurasi model (.cfg)
├── weights/            # File bobot model (.weights) - *Harus diisi manual*
├── fonts/              # Font untuk label pada hasil deteksi
├── static/             # Folder penyimpanan gambar (Input/Output)
├── templates/          # File HTML (index.html, dsb)
├── coco.names          # Daftar label kelas
└── README.md           # Dokumentasi Proyek
```
---

⚙️ Penjelasan Parameter Deteksi
Dalam aplikasi ini, Anda dapat mengatur dua parameter utama untuk mengoptimalkan hasil:

Confidence Threshold: Batas minimum tingkat keyakinan model.

Contoh: Jika diatur 0.5, sistem hanya menampilkan objek dengan tingkat keyakinan di atas 50%.

NMS (Non-Maximum Suppression) Threshold: Digunakan untuk mengeliminasi bounding box yang tumpang tindih. Semakin rendah nilainya, semakin ketat sistem dalam menghapus kotak ganda pada satu objek yang sama.

---

🚀 Cara Menjalankan Aplikasi
Metode 1: Local Installation
Clone Repositori:
```git clone [https://github.com/username/project-pink-eye.git](https://github.com/username/project-pink-eye.git)
cd project-pink-eye
```

Install Dependensi:
```
pip install flask opencv-python pillow numpy
```

Siapkan Model: Pastikan file .weights sudah diletakkan di dalam folder weights/.
Jalankan:
```
python app.py
```

Akses melalui browser di: http://localhost:5000

Metode 2: Menggunakan Docker
Jika Anda ingin menjalankan aplikasi di lingkungan yang terisolasi:
Build Image:
```
docker build -t pinkeye-detection .
```

Run Container:
```
docker run -p 5000:5000 pinkeye-detection
```

---

🔄 Alur Kerja Sistem
Upload: User mengunggah foto mata sapi melalui form web.

Processing: Sistem memproses gambar menggunakan OpenCV DNN dengan model YOLOv4-Tiny.

Filtering: Kotak deteksi difilter menggunakan parameter Confidence dan NMS.

Result: Gambar hasil deteksi (beserta kotak dan akurasi) ditampilkan di layar beserta durasi waktu prosesnya.

🎓 Catatan Akademik
Project ini dikembangkan untuk kepentingan penelitian skripsi. Fokus utama adalah pada implementasi Deep Learning yang ringan (lightweight) agar dapat berjalan pada perangkat dengan komputasi menengah ke bawah tanpa memerlukan GPU kelas atas.

📄 Lisensi & Kontribusi
Project ini bersifat open-source untuk tujuan pendidikan. Jika Anda menggunakan kode ini untuk penelitian, mohon cantumkan sumber atau sitasi.

Author: [Fachri Ramdhan]

---
