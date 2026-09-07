## Informasi Pribadi
Nama : Alya Tsabita Imani  
NPM : 2506620192  
Kelas : PBP A

## Panduan setup lokal

Ikuti langkah-langkah berikut untuk mengunduh dan menjalankan proyek ini di komputer lokal:

#### 1. Clone Repositori
Buka terminal (atau PowerShell/Git Bash), lalu jalankan perintah:
```bash
git clone [https://github.com/Alyatsbt/myportofolio.git](https://github.com/Alyatsbt/myportofolio.git)
cd myportofolio

```

#### 2. Buat & Aktifkan Virtual Environment

Gunakan virtual environment bawaan Python agar dependensi terisolasi:

* **Windows (PowerShell):**
```bash
python -m venv env
.\env\Scripts\Activate

```

* **macOS / Linux:**
```bash
python3 -m venv env
source env/bin/activate

```

#### 3. Instalasi Dependensi

Pastikan environment sudah aktif (ditandai tanda `(env)` di awal baris terminal), lalu jalankan:

```bash
pip install -r requirements.txt

```

#### 4. Jalankan Server Django

Jalankan perintah berikut untuk menyalakan server lokal:

```bash
python manage.py runserver

```

#### 5. Buka di Peramban

Buka peramban (browser) dan akses alamat berikut:
👉 `http://localhost:8000/` atau `http://127.0.0.1:8000/`

```

```

## Tugas 1

### Pertanyaan Reflektif
1. Ya, saya menggunakan beberapa elemen semantik HTML5 diantaranya `<section>`, `<main>`, `<nav>` untuk 2 page utama dan `<footer>`, dan `<header>`, tag ini membantu dalam membentuk struktur hierarki yang rapi pada html dan untuk memudahkan design css (untuk selector).

2. kesulitan saya pada page experience karna ingin membuatnya horizontal scroll (aga bermasalah karna awalnya bertumpuk vertikal). 
saya memprioritaskan tampilan desktop, namun sebenarnya tidak ada perbedaan signifikan atau permasalahan kompleks karna untuk page profile dari templatenya sudah cocok dengan saya dan untuk experience page saya menggunakan clamp() supaya ukuran elemen menyesuaikan layar.

3. batasan pada static web murni ada ketika kita mau menambahkan informasi baru harus di-hardcode, jadi ketika informasinya sudah semakin banyak akan membuang waktu banyak untuk copy-paste dan input info tersebut. karna saya belum belajar dynamic web, mungkin seiring berjalannya pembelajaran saya ingin explore dengan menambah page baru yang lebih interaktif (seperti menambah filter kategori, pop up informasi, dll).

### Progress Mingguan
**full commit history bisa dilihat di branch tugas-1 dan main**
- 1 sept 2026 : 
  1. Melakukan Inisialisasi Project Django dengan penambahan HTML, CSS, dan PWS Setup 
  2. update README.md (merapikan struktur) 
  3. perbaiki allowerd host di settings.py 
  4. membuat page profile based on tutorial-1 
- 2 sept 2026 : 
  1. update credetial database 
  2. progress pada page profile (manambahkan data diri, dll)
- 6 sept 2026 :
  1. membuat page experiences (sudah dibuat sejak tanggal 3, tapi baru commit tanggal 6 karna masih berantakan banget)
  2. implementasi horizontal scroll cards dengan flexbox, menambahkan tahun pada cards experiences
- 7 sept 2026 :
  1. mengupdate file README dengan menambahkan pertanyaan refleksi, progress, dan AI disclosure
  2. update README dengan panduan setup lokal
  3. refine final design, Melakukan modularisasi dan pengelompokan kode pada style.css, merapikan semantik HTML5


### AI Disclosure

menjelaskan penggunaan AI untuk membantu pengerjaan tugas 1 dan memperdalam pemahaman.

tools : gemini

link : https://share.gemini.google/EyfbTXw7E4hn 

penggunaan:
- menjelaskan cara kerja html dan css, membuat rangkuman keyword (tag & properti) yang sering digunakan pada html dan css
- membantu merealisasikan ide seperti 'bagaimana cara membuat navbar transparan, gimana cara interaktif scroll horizontal, dll'
- membantu permasalahan git seperti merge conflict dll

AI banyak membantu dalam realisasi ide design yang saya buat di figma serta memperluas wawasan saya mengenai struktur padding, margin dll di css, namun beberapa kali tidak menangkap pertanyaan saya seperti bagaimana cara membuat background header berubah, sehingga saya akali dengan membuat padding profile lebih tinggi dan membuat header position fixed (AI mneyarankan sticky tapi tidak memenuhi ide saya).
