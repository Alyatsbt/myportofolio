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


## Tugas 4

### informasi tambahan mengenai akun tester
|  role  |  username  |
|--------|------------|
| admin  | alyatmonie |
| editor |  alyatsbt  |
|  user  |   zeevrd   |
|  user  |  noxemburg |

### Progress Mingguan
**full commit history bisa dilihat di branch tugas-4 dan main**

- 26 sept 2026 :
1. Menyelesaikan implementasi Tutorial 4: authentication,  manajemen session, dan penggunaan cookie.
2.  Mengimplementasikan sistem otorisasi berbasis peran (Role-Based Access Control) dengan membagi hak akses ke dalam empat tingkatan: pengunjung (guest), pengguna biasa (user), editor, dan superuser.
3. Memperbaiki bug pada logika tombol star agar menampilkan perilaku dan validasi yang benar ketika berinteraksi dengan pengunjung yang belum login.  

- 27 sept 2026 :
1. Memperbaiki dan merapikan antarmuka pengguna (UI) khusus untuk elemen tombol star. 
2. Melakukan penyesuaian tata letak dan desain UI secara menyeluruh pada berbagai tombol aksi serta form input data.
3.  Menambahkan skrip pengujian E2E (End-to-End) baru untuk menguji alur autentikasi dan memastikan sistem pembatasan akses berjalan dengan baik.

### AI Disclosure
menjelaskan penggunaan AI untuk membantu pengerjaan tugas 4 dan memperdalam pemahaman.

tools : gemini, chatGPT

link : 
https://chatgpt.com/share/6aba79c9-1d20-83ec-a2a8-973660de53bb
https://share.gemini.google/JknJ5S4Zfp4h

penggunaan:

- membantu troubleshooting TimeoutException pada testing Selenium dengan menginstruksikan penambahan atribut class="project-form" pada tag form di projects_form.html.

- membantu menyelesaikan error fatal Git saat melakukan push branch baru dengan mengoreksi typo kurang spasi pada argumen -u origin.

- membantu memahami behavior fitur star untuk user yang belum login (guest), termasuk mengarahkan guest ke halaman login ketika mencoba menggunakan fitur yang membutuhkan autentikasi.

- membantu memahami penggunaan form.instance.pk pada template Django untuk membedakan kondisi ketika form digunakan untuk menambahkan data baru dan ketika digunakan untuk meng-update data yang sudah ada.

AI membantu mempercepat proses pemahaman konsep, debugging, dan evaluasi. Namun, setiap saran tetap diperiksa dan disesuaikan kembali dengan kode serta kebutuhan tugas sebelum diterapkan.


## Tugas 5

### Pertanyaan Reflektif

1. Debouncing adalah teknik untuk menunda eksekusi suatu fungsi sampai tidak ada input baru dalam jangka waktu tertentu. Pada fitur pencarian yang menggunakan AJAX, teknik ini penting karena tanpa debouncing setiap perubahan pada input dapat langsung mengirim request ke server. Misalnya saat pengguna mengetik "compfest", browser bisa mengirim request untuk "c", "co", "com", dan seterusnya. Dengan debouncing, timer akan di-reset setiap kali pengguna mengetik, sehingga request baru dikirim setelah pengguna berhenti mengetik selama beberapa saat. Hal ini mengurangi jumlah request ke server dan membuat penggunaan AJAX menjadi lebih efisien.

2. `await` digunakan untuk menunggu sebuah Promise selesai sebelum program melanjutkan ke baris berikutnya. Pada `fetch()`, `await` digunakan agar kita dapat menunggu sampai server memberikan response sebelum membaca data JSON dari response tersebut. Jika tidak menggunakan `await`, hasil dari `fetch()` masih berupa Promise sehingga data belum dapat langsung digunakan sebagai response. Akibatnya, kita perlu menangani Promise tersebut dengan cara lain seperti `.then()`, atau jika langsung mengakses data seolah-olah response sudah tersedia, kode dapat menghasilkan error.

3. XSS (Cross-Site Scripting) adalah serangan ketika data yang berasal dari pengguna dimasukkan ke halaman web sebagai HTML atau script sehingga browser dapat menjalankan kode berbahaya tersebut. Data yang ditampilkan melalui AJAX/JavaScript lebih berisiko apabila data dimasukkan ke halaman menggunakan `innerHTML` tanpa melakukan escaping terlebih dahulu, karena JavaScript dapat secara langsung membentuk dan menyisipkan HTML dari data yang diterima server. Sementara itu, pada template Django, data yang ditampilkan menggunakan `{{ variable }}` secara default akan melalui proses escaping HTML sehingga karakter seperti `<` dan `>` tidak langsung dianggap sebagai tag. Oleh karena itu, pada implementasi AJAX saya menggunakan fungsi `escapeHtml()` untuk data yang dimasukkan ke HTML dan `strip_tags()` pada `ModelForm` untuk membersihkan input dari tag HTML di sisi server.

### Progress Mingguan

**full commit history bisa dilihat di branch tugas-5 dan main**

- 30 sept 2026 :
  1. menyelesaikan implementasi Tutorial 05 yang berfokus pada JavaScript, AJAX, Fetch API, debounce, toast notification, dan XSS protection

- 5 okt 2026 :
  1. mengubah halaman Experience dari server-rendered menjadi dynamic rendering menggunakan AJAX dan Fetch API
  2. menambahkan debounced search pada halaman Experience agar request pencarian tidak dikirim pada setiap karakter
  3. menambahkan fitur star pada Experience serta mengirimkan informasi jumlah star dan status star pengguna pada JSON
  4. mengimplementasikan penambahan Experience melalui modal menggunakan POST AJAX, CSRF token, validasi ModelForm, serta response status 201, 400, dan 403
  5. menghubungkan Django messages dengan toast notification untuk memberikan feedback setelah proses tambah, update, dan delete data
  6. menerapkan perlindungan XSS dengan `escapeHtml()` pada data yang dirender melalui JavaScript dan `strip_tags()` pada validasi `ExperienceForm`
  7. melakukan penyesuaian struktur Project agar kompatibel dengan AJAX Tutorial 05, termasuk penyesuaian field JSON dan penggunaan UUID sebagai primary key Project
  8. melakukan penyesuaian fixture `data.json` agar sesuai dengan struktur model terbaru

  ### AI Disclosure

menjelaskan penggunaan AI untuk membantu pengerjaan tugas 5 dan memperdalam pemahaman mengenai JavaScript, AJAX, dan Fetch API.

tools : ChatGPT

log: https://chatgpt.com/share/6ac3cc23-2ed4-83ec-8c75-c39702b1c5f6 

penggunaan:

- membantu memahami konsep AJAX, Fetch API, `async/await`, debouncing, DOM manipulation, CSRF, dan XSS
- membantu menyesuaikan contoh Tutorial 05 dengan struktur project saya, terutama karena field dan model pada project berbeda dengan contoh yang digunakan di tutorial
- membantu troubleshooting error pada implementasi AJAX, seperti `NoReverseMatch`, `IntegrityError: datatype mismatch`, dan masalah ketidaksesuaian tipe primary key antara model, URL, fixture, dan database
- membantu mengimplementasikan AJAX pada halaman Experience, termasuk pengambilan data JSON, debounced search, modal form, POST AJAX, dan penanganan response status 201, 400, dan 403
- membantu mengimplementasikan fitur star pada Experience dan menyesuaikan data JSON agar dapat menampilkan jumlah star serta status star pengguna yang sedang login
- membantu menghubungkan Django messages dengan fungsi toast notification
- membantu mengevaluasi perlindungan XSS melalui `escapeHtml()` pada JavaScript dan `strip_tags()` pada ModelForm
- membantu melakukan refactor dan penyesuaian struktur HTML serta CSS agar komponen Project dan Experience menggunakan class yang lebih konsisten

AI digunakan sebagai alat bantu untuk memahami konsep, mencari penyebab error, dan mengevaluasi alternatif implementasi. Kode dan keputusan akhir tetap disesuaikan secara manual dengan struktur project yang saya gunakan. Beberapa saran dari AI tidak langsung diterapkan karena perlu disesuaikan dengan model, URL routing, database, dan struktur template yang berbeda dari contoh tutorial.

Salah satu contohnya adalah penggunaan UUID pada primary key `Project`. Perubahan tersebut menyebabkan ketidaksesuaian dengan database dan fixture lama sehingga perlu dilakukan penanganan migration, reset data Project, dan penyesuaian `data.json` secara manual sebelum aplikasi dapat berjalan kembali.