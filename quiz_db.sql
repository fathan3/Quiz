-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Oct 05, 2025 at 12:06 PM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `quiz_db`
--

-- --------------------------------------------------------

--
-- Table structure for table `quiz_cards`
--

CREATE TABLE `quiz_cards` (
  `id` int(11) NOT NULL,
  `question` text NOT NULL,
  `option_a` varchar(255) NOT NULL,
  `option_b` varchar(255) NOT NULL,
  `option_c` varchar(255) NOT NULL,
  `option_d` varchar(255) NOT NULL,
  `answer` char(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data for table `quiz_cards`
--

INSERT INTO `quiz_cards` (`id`, `question`, `option_a`, `option_b`, `option_c`, `option_d`, `answer`) VALUES
(1, 'Apa itu Class dalam OOP?', 'Variabel global', 'Template untuk membuat objek', 'Fungsi utama program', 'Database', 'B'),
(2, 'Apa itu Object dalam OOP?', 'Instance dari class', 'Sebuah class', 'Fungsi', 'Library', 'A'),
(3, 'Apa itu Inheritance?', 'Membuat objek baru', 'Mewarisi properti/method dari class lain', 'Menulis ulang method', 'Membuat variabel global', 'B'),
(4, 'Apa itu Polymorphism?', 'Satu fungsi memiliki banyak bentuk', 'Meniru class lain', 'Membuat objek baru', 'Mewarisi class', 'A'),
(5, 'Apa itu Encapsulation?', 'Menyembunyikan data agar tidak diakses langsung', 'Membuat class baru', 'Mewarisi method', 'Membuat objek baru', 'A'),
(6, 'Apa itu Abstraction?', 'Menyembunyikan detail implementasi dan menampilkan interface', 'Mewarisi class', 'Membuat objek', 'Membuat method baru', 'A'),
(7, 'Apa itu Constructor?', 'Method yang dijalankan saat objek dibuat', 'Fungsi global', 'Variabel class', 'Method biasa', 'A'),
(8, 'Apa itu Destructor?', 'Method yang dijalankan saat objek dihapus', 'Method global', 'Fungsi biasa', 'Variabel lokal', 'A'),
(9, 'Apa itu Method dalam OOP?', 'Fungsi yang ada di dalam class', 'Variabel class', 'Objek baru', 'Tipe data', 'A'),
(10, 'Apa itu Overriding?', 'Menulis ulang method dari parent class di child class', 'Membuat class baru', 'Membuat objek baru', 'Membuat variabel baru', 'A'),
(11, 'Apa itu algoritma?', 'Langkah-langkah menyelesaikan masalah', 'Bahasa pemrograman', 'Database', 'Objek dalam OOP', 'A'),
(12, 'Struktur data yang menggunakan prinsip FIFO disebut?', 'Stack', 'Queue', 'Linked List', 'Tree', 'B'),
(13, 'Struktur data yang menggunakan prinsip LIFO disebut?', 'Queue', 'Stack', 'Graph', 'Array', 'B'),
(14, 'SQL digunakan untuk?', 'Membuat tampilan web', 'Manipulasi database', 'Menulis algoritma', 'Membuat objek', 'B'),
(15, 'Jenis JOIN SQL yang mengembalikan semua baris dari tabel kiri?', 'INNER JOIN', 'LEFT JOIN', 'RIGHT JOIN', 'FULL JOIN', 'B'),
(16, 'Binary Search hanya bekerja pada?', 'Array acak', 'Array terurut', 'Linked List', 'Stack', 'B'),
(17, 'Apa itu loop dalam pemrograman?', 'Percabangan', 'Perulangan', 'Method', 'Class', 'B'),
(18, 'Apa itu variabel dalam pemrograman?', 'Tempat menyimpan data', 'Objek', 'Function', 'Statement', 'A'),
(19, 'Apa itu rekursi?', 'Function memanggil dirinya sendiri', 'Looping biasa', 'Membuat objek baru', 'Tipe data baru', 'A'),
(20, 'Apa itu exception handling?', 'Menangani error saat runtime', 'Membuat objek', 'Menyimpan data', 'Membuat class', 'A');

-- --------------------------------------------------------

--
-- Table structure for table `scores`
--

CREATE TABLE `scores` (
  `id` int(11) NOT NULL,
  `guest_name` varchar(50) DEFAULT NULL,
  `score` int(11) NOT NULL,
  `created_at` timestamp NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data for table `scores`
--

INSERT INTO `scores` (`id`, `guest_name`, `score`, `created_at`) VALUES
(1, 'upin', 1, '2025-10-05 08:19:30'),
(2, 'badrol', 0, '2025-10-05 08:26:14'),
(3, 'badrol', 1, '2025-10-05 08:26:23'),
(4, 'Upin', 1, '2025-10-05 08:41:05'),
(5, 'Upin', 1, '2025-10-05 08:45:14'),
(6, 'Andi', 3, '2025-10-05 09:04:40'),
(7, 'Andi', 3, '2025-10-05 09:04:41'),
(8, 'Guest', 0, '2025-10-05 09:58:36'),
(9, 'Guest', 0, '2025-10-05 09:58:36');

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

CREATE TABLE `users` (
  `id` int(11) NOT NULL,
  `username` varchar(50) NOT NULL,
  `password` varchar(50) NOT NULL,
  `role` enum('admin') NOT NULL DEFAULT 'admin'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`id`, `username`, `password`, `role`) VALUES
(1, 'admin', 'admin123', 'admin');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `quiz_cards`
--
ALTER TABLE `quiz_cards`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `scores`
--
ALTER TABLE `scores`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `quiz_cards`
--
ALTER TABLE `quiz_cards`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=21;

--
-- AUTO_INCREMENT for table `scores`
--
ALTER TABLE `scores`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;

--
-- AUTO_INCREMENT for table `users`
--
ALTER TABLE `users`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
