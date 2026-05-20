# 🧠 Mini Quiz - OOP Implementation

Aplikasi **Interactive Flashcard Quiz** modern yang dibangun menggunakan **Python Flask** dengan arsitektur **OOP (Object-Oriented Programming)** dan **MySQL** sebagai media penyimpanan data.

---

## 🚀 Fitur Utama

1. **OOP Architecture**: Logika bisnis dibungkus secara rapi dalam class-class terpisah untuk pengelolaan data yang modular.
2. **Interactive Quiz Interface**: Tampilan interaktif menggunakan Ajax/Fetch API untuk menjawab soal secara real-time dan mendapatkan skor akhir.
3. **Admin Dashboard**: Panel manajemen konten kuis untuk melakukan operasi CRUD (Create, Read, Update, Delete) soal secara mudah dan aman.
4. **Real-time Scoring & History**: Perhitungan skor instan yang langsung disimpan ke dalam database beserta nama peserta (Guest).

---

## 🛠️ Tech Stack

*   **Backend**: Python 3.x (Flask Framework)
*   **Database**: MySQL (MariaDB)
*   **Frontend**: HTML5, CSS3 (Modern Responsive UI), JavaScript (Vanilla JS & Fetch API), Jinja2 Templating
*   **Authentication**: Session-based login untuk administrator.

---

## 🏛️ Desain Arsitektur & OOP

Aplikasi ini mendemonstrasikan implementasi OOP yang kuat dalam mendesain aplikasi web dengan memisahkan concern logis ke dalam beberapa class di [models.py](file:///d:/quiz/models.py):

### 1. `User` (Enkapsulasi & Autentikasi)
Mengelola data kredensial admin dan logika autentikasi login ke panel admin.
*   **Properti**: `db`, `username`, `password`
*   **Method**: `authenticate()` - Memvalidasi kecocokan username dan password di database.

### 2. `QuizCard` (Model Data & CRUD Active Record Pattern)
Merepresentasikan satu kartu kuis / soal pilihan ganda. Class ini menggunakan pola Active Record untuk berinteraksi langsung dengan database.
*   **Properti**: `db`, `id`, `question`, `option_a`, `option_b`, `option_c`, `option_d`, `answer`
*   **Method**:
    *   `save()` - Menyimpan soal kuis baru ke database.
    *   `update()` - Mengubah data soal kuis yang sudah ada berdasarkan ID.
    *   `delete()` - Menghapus soal kuis dari database.
    *   `to_dict()` - Mengonversi objek menjadi format dictionary (berguna untuk JSON parsing).
    *   `get_all(db)` *(Static Method)* - Mengambil semua daftar soal kuis dari database.

### 3. `QuizManager` (Logika Bisnis & Scoring)
Mengelola alur pengerjaan kuis oleh Guest, memeriksa jawaban, dan mencatat perolehan skor akhir.
*   **Properti**: `db`, `guest_name`, `score`
*   **Method**:
    *   `check_answer(question_id, selected)` - Mengecek kecocokan pilihan jawaban Guest dengan kunci jawaban di database dan menambahkan skor jika benar.
    *   `save_score()` - Menyimpan rekap nama Guest beserta skor akhir ke database.

---

## 🗄️ Struktur Database

Skema database terdiri dari tiga tabel utama di [quiz_db.sql](file:///d:/quiz/quiz_db.sql):

### 1. Tabel `users`
Menyimpan data pengguna admin untuk mengakses panel CRUD.
```sql
CREATE TABLE `users` (
  `id` INT(11) NOT NULL AUTO_INCREMENT,
  `username` VARCHAR(50) NOT NULL,
  `password` VARCHAR(50) NOT NULL,
  `role` ENUM('admin') NOT NULL DEFAULT 'admin',
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
);
```

### 2. Tabel `quiz_cards`
Menyimpan bank soal kuis pilihan ganda beserta kunci jawabannya.
```sql
CREATE TABLE `quiz_cards` (
  `id` INT(11) NOT NULL AUTO_INCREMENT,
  `question` TEXT NOT NULL,
  `option_a` VARCHAR(255) NOT NULL,
  `option_b` VARCHAR(255) NOT NULL,
  `option_c` VARCHAR(255) NOT NULL,
  `option_d` VARCHAR(255) NOT NULL,
  `answer` CHAR(1) NOT NULL,
  PRIMARY KEY (`id`)
);
```

### 3. Tabel `scores`
Mencatat riwayat skor yang diperoleh oleh para Guest setelah menyelesaikan kuis.
```sql
CREATE TABLE `scores` (
  `id` INT(11) NOT NULL AUTO_INCREMENT,
  `guest_name` VARCHAR(50) DEFAULT NULL,
  `score` INT(11) NOT NULL,
  `created_at` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP(),
  PRIMARY KEY (`id`)
);
```

---

## 🔑 Kredensial Default

Untuk masuk ke Panel Admin, gunakan kredensial bawaan berikut:
*   **Username**: `admin`
*   **Password**: `admin123`

---

## ⚙️ Cara Instalasi & Menjalankan Proyek

Ikuti langkah-langkah di bawah ini untuk menjalankan proyek di komputer lokal Anda:

### 1. Prasyarat
Pastikan Anda sudah menginstal:
*   [Python 3.x](https://www.python.org/downloads/)
*   Server MySQL (seperti [XAMPP](https://www.apachefriends.org/), Laragon, atau MySQL installer)

### 2. Konfigurasi Database
1. Aktifkan modul **Apache** dan **MySQL** pada control panel XAMPP Anda.
2. Buka browser dan akses **phpMyAdmin** (`http://localhost/phpmyadmin/`).
3. Buat database baru bernama `quiz_db`.
4. Pilih database tersebut, lalu masuk ke tab **Import**.
5. Pilih file `quiz_db.sql` dari direktori proyek ini dan klik **Import** / **Go**.

### 3. Instalasi Dependensi Python
Buka terminal/CMD di direktori proyek ini, lalu jalankan perintah:
```bash
pip install -r requirements.txt
```

### 4. Konfigurasi Aplikasi
Buka berkas [config.py](file:///d:/quiz/config.py) dan sesuaikan kredensial MySQL dengan server lokal Anda jika diperlukan:
```python
class Config:
    SECRET_KEY = 'this_should_be_secret'
    MYSQL_HOST = 'localhost'
    MYSQL_USER = 'root'
    MYSQL_PASSWORD = ''  # Isi password jika MySQL Anda memilikinya
    MYSQL_DB = 'quiz_db'
```

### 5. Jalankan Aplikasi
Jalankan Flask server dengan perintah:
```bash
python app.py
```
Setelah berjalan, buka browser dan akses aplikasi di:
👉 **[http://127.0.0.1:5000/](http://127.0.0.1:5000/)**

---

## 📂 Struktur Proyek

```text
quiz/
├── static/                # Aset statis seperti CSS dan JS
├── templates/             # Halaman web HTML (Jinja2 Templates)
│   ├── admin.html         # Panel dashboard CRUD admin
│   ├── index.html         # Halaman utama aplikasi
│   ├── login.html         # Halaman login administrator
│   └── quiz.html          # Halaman pengerjaan kuis Guest
├── app.py                 # File utama inisialisasi Flask
├── config.py              # Konfigurasi database MySQL
├── models.py              # Implementasi OOP (User, QuizCard, QuizManager)
├── quiz_db.sql            # Dump basis data MySQL
├── requirements.txt       # Dependensi library Python
└── routes.py              # Routing request URL web
```
