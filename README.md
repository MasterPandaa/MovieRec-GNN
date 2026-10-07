# 🎬 CineGraph-AI — Next-Gen Graph Neural Network Movie Recommendation Engine

[![Python](https://img.shields.io/badge/Python-3.9+-3776AB.svg?logo=python&logoColor=white)](#)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.x-FF4B4B.svg?logo=streamlit&logoColor=white)](#)
[![GNN Embeddings](https://img.shields.io/badge/Model-GNN%20Graph%20Embeddings-0052CC.svg)](#)
[![Scikit-Learn](https://img.shields.io/badge/scikit--learn-Vector%20Search-F7931E.svg?logo=scikit-learn&logoColor=white)](#)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](#)

**CineGraph-AI** adalah sistem rekomendasi film cerdas generasi terbaru yang memanfaatkan representasi topologi **Graph Neural Network (GNN)** dan pencarian vektor berkecepatan tinggi (*Cosine Similarity Vector Search*). Didesain untuk memberikan rekomendasi film yang sangat personal, akurat, dan kaya konteks berdasarkan riwayat preferensi tontonan pengguna.

Aplikasi ini mengintegrasikan model graph embedding terlatih (**`movie_gnn_model.pkl`**) dengan antarmuka web interaktif berbasis **Streamlit**, memungkinkan eksplorasi film, simulasi persona penonton, dan penelusuran katalog film global secara real-time.

---

## 🌟 Mengapa Menggunakan CineGraph-AI?

- 🚫 **Melampaui Keterbatasan Rekomendasi Tradisional**: Algoritma konvensional sering kali gagal menangkap korelasi non-linear antar film. CineGraph-AI memanfaatkan representasi graf (*node embeddings*) yang memetakan kedekatan tema, genre, dan relasi laten antar film ke dalam ruang vektor berdimensi tinggi.
- ⚡ **Inferensi Vektor Instan (*Sub-Millisecond Vector Search*)**: Menghitung titik pusat minat tontonan pengguna (*User Vector Centroid*) dan menghitung kemiripan kosinus terhadap seluruh katalog film secara instan.
- 🎯 **Personalisasi Multi-Watch Dinamis**: Rekomendasi beradaptasi langsung seketika pengguna menambah atau menghapus judul film dari daftar riwayat tontonan, otomatis menyaring film yang sudah pernah ditonton.
- 🔍 **Eksplorasi Katalog & Filtering Genre Cerdas**: Dilengkapi tab eksplorasi film interaktif untuk menyaring judul-judul terbaik berdasarkan genre spesifik dengan pengurutan tingkat popularitas dan rating global.

---

## 🚀 Fitur Utama

1. **GNN-Powered Graph Embeddings (`movie_gnn_model.pkl`)**:
   - Memanfaatkan vektor representasi graf berdimensi tinggi yang menangkap kedekatan semantik dan topologi relasi antar film.
2. **Personalized Multi-History Recommendation Engine**:
   - Menghitung rata-rata vektor dari seluruh film yang telah ditonton pengguna (`np.mean`) dan merekomendasikan *Top-K* film paling relevan dengan skor kemiripan tertinggi.
3. **Interactive Streamlit Web Dashboard**:
   - Antarmuka interaktif yang bersih dan responsif, dilengkapi *sidebar* interaktif untuk simulasi tontonan pengguna dan tombol *reset history* instan.
4. **Katalog & Filter Genre Global**:
   - Penelusuran katalog film berdasarkan genre (Action, Drama, Sci-Fi, Romance, dll.) yang diurutkan berdasarkan metrik popularitas dan rating.
5. **High-Performance In-Memory Model Caching (`@st.cache_resource`)**:
   - Optimalisasi pemuatan model ke RAM sehingga inferensi dan pergeseran rekomendasi berlangsung tanpa jeda (*zero latency*).
6. **Cloud Deployment Ready (`Procfile`)**:
   - Siap dideploy langsung ke berbagai platform cloud (Streamlit Community Cloud, Heroku, Render, Hugging Face Spaces, VPS).

---

## 🛠️ Tata Cara Instalasi

### 1. Prasyarat Sistem
Pastikan perangkat Anda telah terinstal:
- **Python 3.9+** ([Unduh Python](https://www.python.org/downloads/))
- **Git** ([Unduh Git](https://git-scm.com/))
- **pip** (Python Package Installer)

---

### 2. Clone Repository
```bash
git clone https://github.com/MasterPandaa/CineGraph-AI.git
cd CineGraph-AI
```

---

### 3. Setup Virtual Environment (Disarankan)

#### 🪟 Windows (PowerShell / Command Prompt)
```powershell
python -m venv venv
.\venv\Scripts\activate
```

#### 🐧 Linux / 🍎 macOS (Bash / Zsh)
```bash
python3 -m venv venv
source venv/bin/activate
```

---

### 4. Instalasi Dependensi
```bash
pip install -r requirements.txt
```

---

### 5. Menjalankan Aplikasi Streamlit
```bash
streamlit run app.py
```
Setelah aplikasi berjalan, buka browser Anda di alamat:
👉 **[http://localhost:8501](http://localhost:8501)**

---

## 📖 Panduan Penggunaan

1. **Buka Aplikasi**: Akses [http://localhost:8501](http://localhost:8501) pada browser Anda.
2. **Pilih Film pada Riwayat Tontonan**:
   - Pada panel sidebar di sebelah kiri (**"User Activity"**), pilih satu atau beberapa film yang pernah Anda tonton dan sukai.
3. **Dapatkan Rekomendasi Personal**:
   - Buka tab **"🔥 Rekomendasi Untukmu"**.
   - Sistem secara otomatis menghitung vektor preferensi Anda dan menampilkan rekomendasi film terbaik lengkap dengan informasi Rating, Judul, dan Genre.
4. **Eksplorasi Berdasarkan Genre**:
   - Buka tab **"🔍 Cari Film"**.
   - Pilih genre yang diminati dari dropdown list untuk melihat tabel film terpopuler, rating, dan negara pembuatnya.
5. **Reset & Uji Skenario Baru**:
   - Klik tombol **"Reset History"** pada sidebar untuk membersihkan preferensi dan menguji skenario persona pengguna lainnya.

---

## 📦 Struktur Project

```text
CineGraph-AI/
├── .gitattributes             # Konfigurasi format line ending Git
├── Procfile                   # Definisi runner web server (Streamlit) untuk cloud deployment
├── README.md                  # Dokumentasi & panduan penggunaan komprehensif
├── app.py                     # Antarmuka web Streamlit & algoritma rekomendasi cosine similarity
├── movie_gnn_model.pkl        # Bundle artefak model GNN (Dataframe, Graph Vectors, Title Map)
└── requirements.txt           # Daftar dependensi library Python proyek
```

---

## 🔒 Privasi & Keamanan

- **100% On-Premise & Local Execution**: Seluruh proses kalkulasi kemiripan vektor dijalankan secara lokal di runtime Python Anda tanpa mengirimkan riwayat penonton ke server eksternal.
- **Efficient Memory Footprint**: Struktur data sparse/dense array dioptimalkan dengan NumPy untuk efisiensi konsumsi memori.

---

## 📄 Lisensi

Didistribusikan di bawah lisensi [MIT](LICENSE). Bebas digunakan, dikembangkan, dan dimodifikasi untuk kebutuhan riset akademik, proyek portofolio, maupun implementasi komersial.
