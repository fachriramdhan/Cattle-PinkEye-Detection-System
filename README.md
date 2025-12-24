🐄 Deteksi Dini Penyakit Mata Pink Eye pada Sapi
Berbasis Citra Digital Menggunakan YOLOv4-Tiny

Aplikasi web ini merupakan sistem deteksi dini penyakit mata Pink Eye pada sapi berbasis citra digital menggunakan algoritma YOLOv4-Tiny.
Sistem dikembangkan sebagai project skripsi untuk membantu peternak dan pihak terkait dalam melakukan pemantauan kesehatan sapi secara cepat dan otomatis melalui gambar.

📌 Latar Belakang

Penyakit Pink Eye (Infectious Bovine Keratoconjunctivitis) merupakan salah satu penyakit mata yang umum menyerang sapi dan dapat menurunkan produktivitas ternak jika tidak ditangani sejak dini.
Pemanfaatan teknologi Computer Vision dan Deep Learning diharapkan dapat membantu proses deteksi awal secara lebih efisien dibandingkan pemeriksaan manual.

🎯 Tujuan Sistem

Mendeteksi keberadaan penyakit mata Pink Eye pada sapi dari citra digital
Menampilkan hasil deteksi berupa bounding box dan tingkat kepercayaan (confidence score)
Memberikan sistem deteksi yang mudah digunakan melalui antarmuka web

🧠 Metode yang Digunakan

Algoritma: YOLOv4-Tiny
Framework: OpenCV DNN
Bahasa Pemrograman: Python
Web Framework: Flask
Frontend: HTML, Tailwind CSS
Library Pendukung:
OpenCV
NumPy
Pillow (PIL)

# Struktur Folder Project

Berikut adalah struktur folder project **Deteksi Pink Eye Sapi**:

![Struktur Folder](assets/folder-structure.png)

Keterangan:

- **app.py** → Script utama aplikasi
- **configs/** → File konfigurasi YOLOv4
- **weights/** → Model YOLOv4 (tidak diupload GitHub)
- **fonts/** → Font untuk annotasi gambar
- **static/** → File gambar input, output, dan background
- **templates/** → File HTML
- **coco.names** → Label class YOLOv4
- **README.md** → Dokumentasi project

⚙️ Fitur Aplikasi

Upload gambar sapi melalui web
Pengaturan confidence threshold dan overlap threshold
Deteksi otomatis objek penyakit mata
Visualisasi bounding box dan label kelas
Menampilkan skor kepercayaan (confidence)
Informasi waktu proses deteksi
Tampilan responsif dan user-friendly

🔄 Alur Kerja Sistem

Pengguna mengunggah gambar sapi
Sistem melakukan preprocessing citra
Model YOLOv4-Tiny melakukan deteksi objek
Sistem menampilkan:
Gambar hasil deteksi
Label kelas
Confidence score
Waktu proses
