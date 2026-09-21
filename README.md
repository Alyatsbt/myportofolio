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

## Tugas 2

### Pertanyaan Reflektif
1. Saat kita membuka alamat `/projects/`, permintaan dari browser pertama kali diterima oleh `urls.py` proyek yang kemudian meneruskannya ke `urls.py` milik aplikasi `main`. Dari situ, rute diarahkan ke fungsi `view` yang bertugas memanggil data dari `model`. Setelah datanya diambil, `view` memasukkan ke dalam *context* dan mengirimkannya `template` HTML. Django kemudian memproses template tersebut bersama data yang ada hingga menghasilkan tampilan web yang utuh dan menampilkannya kembali di browser.

2. data untuk portofolio disimpan terpisah agar memudahkan maintenance dan apabila ada update mengenai data portofolio, yang diubah hanya model yang menyimpan data sehingga mengurangi risiko rusaknya struktur HTML, kemudian mencegah repetisi jika design html semakin kompleks

3. `makemigrations` bertugas membuat berkas catatan atau rancangan mengenai perubahan yang terjadi pada berkas `models.py`, sedangkan `migrate` bertugas mengeksekusi rancangan tersebut langsung ke data yang sedang digunakan. Contohnya saat kita membuat model baru seperti `Project` atau menambahkan kolom baru seperti `organization` pada model `Experience`. Kita wajib menjalankan `makemigrations` terlebih dahulu untuk mencatat perubahan strukturnya, lalu menjalankan `migrate` agar tabel atau kolom baru tersebut benar-benar terbentuk di dalam database

### Progress Mingguan
**full commit history bisa dilihat di branch tugas-2 dan main**
- 9 sept 2026 :
  1. menurunkan versi Django di requirements.txt agar kompatibel saat deployment di PWS
  2. menyelesaikan implementasi konsep MVT Tutorial 2 untuk bagian Experience
- 13 sept 2026 :
  1. melakukan refactor dan penyesuaian desain UI pada bagian navbar serta profil
  2. mengubah tampilan halaman experiences dari data statis menjadi dinamis
- 14 sept 2026 :
  1. membuat halaman baru Projects dengan alur MVT lengkap (pembuatan model Project, migrasi, view, routing URL, dan template dinamis)
  2. menambahkan fixture data.json serta merapikan panjang karakter URL prototype agar data berhasil dimuat di database server PWS
  3. memperbaiki penamaan berkas gambar banner (case-sensitivity dan typo) agar terbaca dengan baik di server
  4. menambahkan unit test baru untuk halaman dan model Projects (memastikan seluruh 9 test berhasil lulus)
  
### AI Disclosure
menjelaskan penggunaan AI untuk membantu pengerjaan tugas 2 dan memperdalam pemahaman.

tools : gemini

link : https://share.gemini.google/NWxgH6LAKHPM 

penggunaan:
- membantu memahami implementasi MVT dan cara kerjanya
- membantu troubleshooting error pada unit test (menyesuaikan assertion template dan mengatasi NameError pada import model)
- membantu penyesuaian styling CSS, seperti mengubah fonts dan mengatur ukuran blur background radial-gradient
- membantu mengatasi kendala deployment di PWS, seperti pembuatan fixture data.json, pemotongan URL Figma yang melebihi batas karakter PostgreSQL, dan masalah case-sensitivity pada berkas gambar
- membantu pemahaman mengenai migrations di terminal dan mengapa harus melakukan hal tersebut

AI sangat membantu mempercepat proses pencarian solusi saat menghadapi kendala teknis dan debugging, terutama terkait error di lingkungan server PWS dan unit test. Namun, beberapa saran awal tidak langsung bisa dipakai begitu saja. Misalnya saat AI menyarankan eksekusi kode oneliner di terminal PWS yang sempat error karena karakter '&' pada URL Figma, sehingga akhirnya dialihkan menggunakan JSON. 

## Tugas 3

### Pertanyaan Reflektif
1. ModelForm digunakan karna lebih praktis dan efisien daripada buat tag <input> HTML satu satu dan mengaur validasinya. ModelForm otomatis membaca struktur database dan menggenerate form, sedangkan {% csrf_token %} berguna sebagai token pengaman untuk mencegah serangan Cross-Site Request Forgery, jadi server bisa memastikan kalau data yang di submit itu benar benar asli dari web kita sendiri.

2. JSON lebih disukai di pengembangan web modern karena bentuknya jauh lebih ringkas. XML lebih boros karakter karena harus pakai banyak tag pembuka dan penutup, sedangkan JSON menggunakan format key-value yang bikin ukuran datanya lebih ringan. Karena ringan, mesin bisa membaca dan memproses (parsing) datanya dengan jauh lebih cepat, JSON juga integrasi dengan Javascript.

3. Alurnya dimulai saat ada request ke URL API, lalu fungsi view akan merespons dengan menarik data portofolio dari database (misalnya pakai Project.objects.all()). namun wujud asli data dari database Django ini kan masih berupa Objek Python, sementara sistem seperti browser, frontend, atau aplikasi mobile tidak mengerti apa itu Objek Python.  Serialisasi bertugas menerjemahkan Objek Python tersebut menjadi format teks JSON yang universal. Setelah wujudnya berubah jadi JSON, barulah data tersebut dibungkus dengan HttpResponse dan dikembalikan ke browser atau client.


### Progress Mingguan
**full commit history bisa dilihat di branch tugas-3 dan main**
- 16 sept 2026 :
1. menyelesaikan implementasi Tutorial 3 yang berfokus pada Form dan Data Delivery 
- 20 sept 2026 :
1. melakukan penyesuaian dan peningkatan desain UI pada halaman projects
2. melakukan refaktor pada CSS dengan menerapkan variabel khusus untuk styling yang lebih rapi dan terstruktur
3. mengimplementasi fitur CRUD pada page project
- 21 sept 2026 :
1. memisahkan page experience menjadi entitas mandiri dan mengimplementasikan fitur CRUD (Create, Read, Update, Delete)
2. menambahkan template form serta antarmuka modal konfirmasi untuk fitur delete data experience
3. melakukan refaktor styling dengan memindahkan format inline ke CSS eksternal serta membereskan bug pada layout UI
4. memperbaiki bug sistem termasuk duplikasi data saat update project, error validasi CSRF, dan memperbaiki layout timeline yang patah akibat data tanggal yang kosong

## AI Disclosure
menjelaskan penggunaan AI untuk membantu pengerjaan tugas 3 dan memperdalam pemahaman.

tools : gemini

link : https://gemini.google.com/share/d/16um0MLK6j3H-H0h3gv77geut81WaJ77Q?usp=sharing 

penggunaan:

- refactor file CSS sehingga struktur dam variable lebih rapi

- membantu mencari tahu penyebab error migrasi database (FieldError) yang ternyata disebabkan oleh konflik nama antara field is_ongoing dan fungsi @property di models.py

- membantu mengatasi bug duplikasi data dengan mengevaluasi dan menghapus atribut action pada projects_form.html

- membantu menyelesaikan error Forbidden (403) CSRF verification failed dengan menyisipkan kembali {% csrf_token %} beserta penutup tag form yang sempat hilang

- membantu troubleshooting error NoReverseMatch yang terjadi karena typo pada pemanggilan nama URL di fungsi redirect views.py

AI sangat membantu mempercepat siklus debugging yang berlapis, terutama ketika satu error beruntun memicu error lainnya dari sisi database, routing, hingga tampilan UI. Bantuan AI sangat efektif untuk menemukan typo kecil yang sering kali sulit disadari jika hanya dibaca sekilas (seperti konflik nama variabel atau tag HTML yang tidak tertutup). Namun, proses ini juga menunjukkan bahwa saran perbaikan dari AI harus dibaca teliti, karena sering kali letak error-nya ternyata murni dari human error di kode yang saya tulis sendiri.