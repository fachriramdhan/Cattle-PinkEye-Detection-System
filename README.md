# 🐄 Deteksi Dini Penyakit Mata *Pink Eye* pada Sapi  
### Berbasis Citra Digital Menggunakan YOLOv4-Tiny

Aplikasi web ini merupakan **sistem deteksi dini penyakit mata Pink Eye (Infectious Bovine Keratoconjunctivitis)** pada sapi berbasis **citra digital** menggunakan algoritma **YOLOv4-Tiny**.  
Sistem dikembangkan sebagai **project skripsi** untuk membantu peternak dan pihak terkait dalam melakukan pemantauan kesehatan sapi secara **cepat, otomatis, dan berbasis Artificial Intelligence (AI)** melalui gambar.

---

## 📌 Latar Belakang

Penyakit **Pink Eye** merupakan salah satu penyakit mata yang umum menyerang sapi dan dapat menyebabkan:

- Penurunan produktivitas ternak
- Gangguan penglihatan hingga kebutaan
- Kerugian ekonomi bagi peternak

Pemeriksaan manual membutuhkan waktu serta tenaga ahli. Oleh karena itu, pemanfaatan **Computer Vision** dan **Deep Learning** diharapkan mampu membantu proses **deteksi dini** secara lebih **efisien, objektif, dan scalable**.

---

## 🎯 Tujuan Sistem

Sistem ini dirancang untuk:

- Mendeteksi keberadaan penyakit mata **Pink Eye** pada sapi dari citra digital
- Menampilkan hasil deteksi berupa:
  - **Bounding box**
  - **Label kelas**
  - **Confidence score**
- Menyediakan antarmuka web yang **mudah digunakan** oleh pengguna non-teknis

---

## 🧠 Metodologi & Teknologi

### 🔍 Metode Deteksi
- **Algoritma**: YOLOv4-Tiny  
- **Pendekatan**: Object Detection berbasis Deep Learning  
- **Inference Engine**: OpenCV DNN Module  

---

### 🛠️ Technology Stack

#### Backend & AI
- **Python**
- **YOLOv4-Tiny**
- **OpenCV (DNN)**
- **NumPy**
- **Pillow (PIL)**

#### Web Framework
- **Flask** – Backend web application

#### Frontend
- **HTML**
- **Tailwind CSS**

---

## 📂 Struktur Folder Project

Struktur direktori project **Deteksi Pink Eye Sapi**:

```text
project-root/
├── app.py              # Main application script
├── configs/             # YOLOv4-Tiny configuration files
├── weights/             # YOLOv4 trained weights (not uploaded)
├── fonts/               # Font for image annotation
├── static/              # Input & output images
├── templates/           # HTML templates
├── coco.names           # YOLO class labels
└── README.md            # Project documentation

---

📌 Catatan:
Folder weights/ tidak diunggah ke GitHub karena ukuran file yang besar.

---

📁 Visual Struktur Folder

⚙️ Fitur Aplikasi

Upload gambar sapi melalui web interface

Pengaturan parameter deteksi:

Confidence threshold

Overlap (NMS) threshold

Deteksi otomatis penyakit mata

Visualisasi hasil deteksi:

Bounding box

Label kelas

Confidence score

Informasi waktu proses deteksi

Tampilan antarmuka yang responsif dan user-friendly

---

🔄 Alur Kerja Sistem

Pengguna mengunggah gambar sapi

Sistem melakukan preprocessing citra

Model YOLOv4-Tiny melakukan deteksi objek

Sistem menampilkan:

Gambar hasil deteksi

Label kelas

Confidence score

Waktu proses deteksi

---

🧩 Implementasi Sistem (app.py)

File app.py berfungsi sebagai inti aplikasi, dengan tanggung jawab utama:

Memuat model YOLOv4-Tiny (cfg, weights, labels)

Melakukan preprocessing dan inference citra

Menerapkan Non-Maximum Suppression (NMS)

Menampilkan hasil deteksi melalui antarmuka web berbasis Flask

---

🔐 Highlight Teknis

OpenCV DNN digunakan untuk inference tanpa framework deep learning berat

Non-Maximum Suppression (NMS) untuk mengurangi bounding box duplikat

Visualisasi bounding box & label menggunakan Pillow

Pengukuran waktu proses untuk evaluasi performa sistem

---

🚀 Cara Menjalankan Aplikasi
1️⃣ Persiapan Environment

Pastikan Python sudah terinstall, kemudian install dependency:

pip install flask opencv-python pillow numpy

2️⃣ Menjalankan Aplikasi
python app.py


Aplikasi akan berjalan pada alamat berikut:

http://localhost:5000

---

📊 Output Sistem

Gambar hasil deteksi tersimpan di folder static/

Informasi hasil deteksi ditampilkan langsung pada halaman web

Waktu inference ditampilkan dalam satuan detik

---

🎓 Catatan Akademik

Project ini dikembangkan sebagai bagian dari penelitian skripsi, dengan fokus pada:

Penerapan Deep Learning di bidang peternakan

Implementasi Computer Vision untuk deteksi penyakit hewan

Pengembangan sistem berbasis web yang aplikatif

---

📄 Lisensi

Project ini dibuat untuk kepentingan akademik dan edukasi.
Penggunaan ulang diperbolehkan dengan mencantumkan sumber.

👨‍💻 Author

Fachri Ramdhan
