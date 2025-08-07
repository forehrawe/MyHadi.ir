-- phpMyAdmin SQL Dump
-- version 5.2.2
-- https://www.phpmyadmin.net/
--
-- Host: localhost:3306
-- Generation Time: Aug 01, 2025 at 01:05 PM
-- Server version: 8.0.42-cll-lve
-- PHP Version: 8.3.22

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `cp63888797157_users`
--

-- --------------------------------------------------------

--
-- Table structure for table `accounts`
--

CREATE TABLE `accounts` (
  `account_id` int NOT NULL,
  `username` varchar(20) COLLATE utf8mb4_general_ci NOT NULL,
  `password` varchar(83) COLLATE utf8mb4_general_ci NOT NULL,
  `email` varchar(35) COLLATE utf8mb4_general_ci NOT NULL,
  `name` varchar(23) COLLATE utf8mb4_general_ci NOT NULL,
  `lastname` varchar(30) COLLATE utf8mb4_general_ci NOT NULL,
  `role` varchar(6) COLLATE utf8mb4_general_ci NOT NULL,
  `token` varchar(100) COLLATE utf8mb4_general_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `accounts`
--

INSERT INTO `accounts` (`account_id`, `username`, `password`, `email`, `name`, `lastname`, `role`, `token`) VALUES
(8, 'Hadighp', '13b7f84c0aa486a6b216ae6488fcd8d76d5dadbb249efb0e3989de6a2ea4a659', 'aalgvs8@gmail.com', 'hadi', 'ghesmatpour', 'user', '690c208c9ccddec7e02fcb157224d16e'),
(9, '1212', '13b7f84c0aa486a6b216ae6488fcd8d76d5dadbb249efb0e3989de6a2ea4a659', 'myemailfkpy@gmail.com', 'هادی', 'قسمت پورقره باغ', 'user', 'b44b4487b4841eaaf4b50d43c4b2b85e'),
(10, 'Majid', '3df6fa79588aab5caebf4a631695363bf7d7b75999aae9c788070b65dbaa715c', 'Mamad@gmai.com', 'Karim', 'Bagheri', 'admin', 'ea0f06d64060b7aecd956a639b798c89'),
(11, 'arshia', 'b20713011cba2b08c018ee4705e97478f06720c5ba93e91c50c763decbac5f20', 'arshia22mirzaee@gmail.com', 'Arshi', 'Mirzaee', 'admin', '2d55b442fff39cef4a66673f27189873'),
(12, 'Hadi', '8d969eef6ecad3c29a3a629280e686cf0c3f5d5a86aff3ca12020c923adc6c92', 'Lolo', 'Hohk', 'Jdj', 'user', 'abd7ad85d9bfd702c3a7a76c690580bd');

-- --------------------------------------------------------

--
-- Table structure for table `admins`
--

CREATE TABLE `admins` (
  `id` int NOT NULL,
  `acc_id` int DEFAULT NULL,
  `email` varchar(30) COLLATE utf8mb4_general_ci NOT NULL,
  `token` varchar(50) COLLATE utf8mb4_general_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `admins`
--

INSERT INTO `admins` (`id`, `acc_id`, `email`, `token`) VALUES
(1, 8, 'aalgvs8@gmail.com', '690c208c9ccddec7e02fcb157224d16e'),
(20, 11, 'arshia22mirzaee@gmail.com', '2d55b442fff39cef4a66673f27189873');

-- --------------------------------------------------------

--
-- Table structure for table `messenger`
--

CREATE TABLE `messenger` (
  `id` int NOT NULL,
  `u1_email` varchar(35) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci DEFAULT NULL,
  `u2_email` varchar(35) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci DEFAULT NULL,
  `content` varchar(500) DEFAULT NULL,
  `date_time` datetime DEFAULT NULL,
  `conversation_id` varchar(10) DEFAULT NULL,
  `sender` varchar(35) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci
;

--
-- Dumping data for table `messenger`
--

INSERT INTO `messenger` (`id`, `u1_email`, `u2_email`, `content`, `date_time`, `conversation_id`, `sender`) VALUES
(1, 'aalgvs8@gmail.com', 'arshia22mirzaee@gmail.com', 'Hello', '2025-07-30 19:39:52', '464bf59435', NULL),
(2, 'aalgvs8@gmail.com', 'arshia22mirzaee@gmail.com', 'lllll', '2025-07-30 19:40:10', '464bf59435', NULL),
(3, 'aalgvs8@gmail.com', 'arshia22mirzaee@gmail.com', 'L', '2025-07-30 19:48:01', '464bf59435', NULL),
(4, 'aalgvs8@gmail.com', 'arshia22mirzaee@gmail.com', 'Koopppouuygtddt', '2025-07-30 19:48:11', '464bf59435', NULL),
(5, 'aalgvs8@gmail.com', 'myemailfkpy@gmail.com', 'Hello', '2025-07-30 19:48:51', 'ce76a8fe6b', NULL),
(6, 'aalgvs8@gmail.com', 'myemailfkpy@gmail.com', 'ک', '2025-07-30 20:25:27', 'ce76a8fe6b', NULL),
(7, 'aalgvs8@gmail.com', 'myemailfkpy@gmail.com', 'ک', '2025-07-30 20:25:39', 'ce76a8fe6b', NULL),
(8, 'aalgvs8@gmail.com', 'myemailfkpy@gmail.com', 'عاغ', '2025-07-30 20:25:46', 'ce76a8fe6b', NULL),
(9, 'aalgvs8@gmail.com', 'myemailfkpy@gmail.com', 'Gknj', '2025-07-30 20:25:57', 'ce76a8fe6b', NULL),
(10, 'aalgvs8@gmail.com', 'myemailfkpy@gmail.com', 'Ygf', '2025-07-30 20:26:01', 'ce76a8fe6b', NULL),
(11, 'aalgvs8@gmail.com', 'myemailfkpy@gmail.com', 'هاه', '2025-07-30 20:26:35', 'ce76a8fe6b', NULL),
(12, 'aalgvs8@gmail.com', 'myemailfkpy@gmail.com', 'Ji', '2025-07-30 20:26:43', 'ce76a8fe6b', NULL),
(13, 'aalgvs8@gmail.com', 'myemailfkpy@gmail.com', 'Hugu', '2025-07-30 20:26:50', 'ce76a8fe6b', NULL),
(14, 'aalgvs8@gmail.com', 'myemailfkpy@gmail.com', 'هاع', '2025-07-30 20:26:58', 'ce76a8fe6b', NULL),
(15, 'aalgvs8@gmail.com', 'myemailfkpy@gmail.com', 'تدت', '2025-07-30 20:27:56', 'ce76a8fe6b', NULL),
(16, 'aalgvs8@gmail.com', 'myemailfkpy@gmail.com', 'ذاذا', '2025-07-30 20:28:13', 'ce76a8fe6b', NULL),
(17, 'aalgvs8@gmail.com', 'myemailfkpy@gmail.com', 'تناتت', '2025-07-30 20:28:17', 'ce76a8fe6b', NULL),
(18, 'aalgvs8@gmail.com', 'myemailfkpy@gmail.com', ' Hhgu', '2025-07-30 20:28:22', 'ce76a8fe6b', NULL),
(19, 'aalgvs8@gmail.com', 'myemailfkpy@gmail.com', 'Chcyvu', '2025-07-30 20:28:25', 'ce76a8fe6b', NULL),
(20, 'aalgvs8@gmail.com', 'myemailfkpy@gmail.com', 'Vygh', '2025-07-30 20:28:28', 'ce76a8fe6b', NULL),
(21, 'aalgvs8@gmail.com', 'myemailfkpy@gmail.com', '', '2025-07-30 20:28:29', 'ce76a8fe6b', NULL),
(22, 'aalgvs8@gmail.com', 'myemailfkpy@gmail.com', '', '2025-07-30 20:28:31', 'ce76a8fe6b', NULL),
(23, 'aalgvs8@gmail.com', 'myemailfkpy@gmail.com', 'Hyfy', '2025-07-30 20:28:35', 'ce76a8fe6b', NULL),
(24, 'aalgvs8@gmail.com', 'myemailfkpy@gmail.com', 'Yugg', '2025-07-30 20:28:46', 'ce76a8fe6b', NULL),
(25, 'aalgvs8@gmail.com', 'myemailfkpy@gmail.com', 'Ggf', '2025-07-30 20:28:49', 'ce76a8fe6b', NULL),
(26, 'Lolo', 'aalgvs8@gmail.com', 'Hello', '2025-07-30 20:29:04', '1fa33ba8e1', NULL),
(27, 'Lolo', 'aalgvs8@gmail.com', 'Hvy', '2025-07-30 20:29:08', '1fa33ba8e1', NULL),
(28, 'Lolo', 'aalgvs8@gmail.com', 'Hjhg', '2025-07-30 20:29:12', '1fa33ba8e1', NULL),
(29, 'Lolo', 'aalgvs8@gmail.com', 'علا', '2025-07-30 20:29:15', '1fa33ba8e1', NULL),
(30, 'Lolo', 'aalgvs8@gmail.com', 'دهدا', '2025-07-30 20:29:17', '1fa33ba8e1', NULL),
(31, 'Lolo', 'aalgvs8@gmail.com', 'رuggv', '2025-07-30 20:29:21', '1fa33ba8e1', NULL),
(32, 'Lolo', 'aalgvs8@gmail.com', 'Bjbgf', '2025-07-30 20:29:24', '1fa33ba8e1', NULL),
(33, 'Lolo', 'aalgvs8@gmail.com', 'Budfgj', '2025-07-30 20:29:28', '1fa33ba8e1', NULL),
(34, 'Lolo', 'aalgvs8@gmail.com', 'کککککک', '2025-07-30 20:29:33', '1fa33ba8e1', NULL),
(35, 'Lolo', 'aalgvs8@gmail.com', 'داالعلف', '2025-07-30 20:29:36', '1fa33ba8e1', NULL),
(36, 'Lolo', 'aalgvs8@gmail.com', 'دتغتغ', '2025-07-30 20:29:39', '1fa33ba8e1', NULL),
(37, 'Lolo', 'aalgvs8@gmail.com', 'اغلار', '2025-07-30 20:30:16', '1fa33ba8e1', NULL),
(38, 'Lolo', 'aalgvs8@gmail.com', 'الغا', '2025-07-30 20:30:31', '1fa33ba8e1', NULL),
(39, 'Lolo', 'aalgvs8@gmail.com', 'عاغ', '2025-07-30 20:30:38', '1fa33ba8e1', NULL),
(40, 'Lolo', 'aalgvs8@gmail.com', 'ننید', '2025-07-30 21:00:40', '1fa33ba8e1', NULL),
(41, 'Lolo', 'aalgvs8@gmail.com', 'زنزدی', '2025-07-30 21:00:42', '1fa33ba8e1', NULL),
(42, 'aalgvs8@gmail.com', 'arshia22mirzaee@gmail.com', 'koso', '2025-07-31 06:31:21', '464bf59435', NULL),
(43, 'aalgvs8@gmail.com', 'arshia22mirzaee@gmail.com', 'awdasd', '2025-07-31 06:31:28', '464bf59435', NULL),
(44, 'aalgvs8@gmail.com', 'arshia22mirzaee@gmail.com', 'wadsadf  f', '2025-07-31 06:31:32', '464bf59435', NULL),
(45, 'aalgvs8@gmail.com', 'arshia22mirzaee@gmail.com', 'wdasdw', '2025-07-31 06:31:34', '464bf59435', NULL),
(46, 'aalgvs8@gmail.com', 'arshia22mirzaee@gmail.com', 'بشص', '2025-07-31 06:31:38', '464bf59435', NULL),
(47, 'aalgvs8@gmail.com', 'arshia22mirzaee@gmail.com', 'صشیسشی', '2025-07-31 06:31:42', '464bf59435', NULL),
(48, 'aalgvs8@gmail.com', 'arshia22mirzaee@gmail.com', 'شصیسشیص', '2025-07-31 06:31:45', '464bf59435', NULL),
(49, 'aalgvs8@gmail.com', 'arshia22mirzaee@gmail.com', 'لصثلصثسبصثب', '2025-07-31 06:31:49', '464bf59435', NULL),
(50, 'aalgvs8@gmail.com', 'arshia22mirzaee@gmail.com', 'awdasd', '2025-07-31 06:41:06', '464bf59435', NULL),
(51, 'aalgvs8@gmail.com', 'arshia22mirzaee@gmail.com', '654654', '2025-07-31 09:47:59', '464bf59435', NULL),
(52, 'aalgvs8@gmail.com', 'arshia22mirzaee@gmail.com', 'هوی', '2025-07-31 09:48:11', '464bf59435', NULL),
(53, 'Lolo', 'aalgvs8@gmail.com', 'Hadi', '2025-07-31 10:52:10', '1fa33ba8e1', NULL),
(54, 'Lolo', 'aalgvs8@gmail.com', 'Hadi', '2025-07-31 10:52:13', '1fa33ba8e1', NULL),
(56, 'aalgvs8@gmail.com', 'arshia22mirzaee@gmail.com', 'اهم', '2025-07-31 20:49:32', '464bf59435', NULL);

-- --------------------------------------------------------

--
-- Table structure for table `posts`
--

CREATE TABLE `posts` (
  `id` int NOT NULL,
  `author_acc_email` varchar(35) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `post_title` varchar(30) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `post_body` varchar(1000) COLLATE utf8mb4_general_ci DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `posts`
--

INSERT INTO `posts` (`id`, `author_acc_email`, `post_title`, `post_body`) VALUES
(1, 'aalgvs8@gmail.com', 'Pc problem', 'Hello helo ndkvj bsj bsji b uudbwu bdnoha idonv uudb bab jdj jndj bek \r\nDkcjme. \r\nKdjocw kc\r\nLxnskovineo okdie diwn vuwb vi\r\nKvow vidoosla dinviw vons'),
(5, 'aalgvs8@gmail.com', 'Bob', 'Gcp');

-- --------------------------------------------------------

--
-- Table structure for table `profile`
--

CREATE TABLE `profile` (
  `acc_id` int NOT NULL,
  `phone_number` varchar(11) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `address` varchar(150) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `age` varchar(3) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `national_code` varchar(10) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `token` varchar(60) COLLATE utf8mb4_general_ci DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `profile`
--

INSERT INTO `profile` (`acc_id`, `phone_number`, `address`, `age`, `national_code`, `token`) VALUES
(8, '94984561', 'sfegergdverg', '17', '8749865654', '690c208c9ccddec7e02fcb157224d16e');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `accounts`
--
ALTER TABLE `accounts`
  ADD PRIMARY KEY (`account_id`),
  ADD UNIQUE KEY `username` (`username`),
  ADD UNIQUE KEY `email` (`email`),
  ADD UNIQUE KEY `token` (`token`),
  ADD UNIQUE KEY `email_2` (`email`);

--
-- Indexes for table `admins`
--
ALTER TABLE `admins`
  ADD PRIMARY KEY (`id`),
  ADD KEY `acc_id` (`acc_id`),
  ADD KEY `email` (`email`),
  ADD KEY `token` (`token`);

--
-- Indexes for table `messenger`
--
ALTER TABLE `messenger`
  ADD PRIMARY KEY (`id`),
  ADD KEY `u1_email` (`u1_email`),
  ADD KEY `u2_email` (`u2_email`);

--
-- Indexes for table `posts`
--
ALTER TABLE `posts`
  ADD PRIMARY KEY (`id`),
  ADD KEY `author_acc_email` (`author_acc_email`);

--
-- Indexes for table `profile`
--
ALTER TABLE `profile`
  ADD PRIMARY KEY (`acc_id`),
  ADD KEY `token` (`token`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `accounts`
--
ALTER TABLE `accounts`
  MODIFY `account_id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=13;

--
-- AUTO_INCREMENT for table `admins`
--
ALTER TABLE `admins`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=21;

--
-- AUTO_INCREMENT for table `messenger`
--
ALTER TABLE `messenger`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=57;

--
-- AUTO_INCREMENT for table `posts`
--
ALTER TABLE `posts`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `admins`
--
ALTER TABLE `admins`
  ADD CONSTRAINT `admins_ibfk_1` FOREIGN KEY (`acc_id`) REFERENCES `accounts` (`account_id`) ON DELETE CASCADE,
  ADD CONSTRAINT `admins_ibfk_2` FOREIGN KEY (`email`) REFERENCES `accounts` (`email`) ON DELETE CASCADE,
  ADD CONSTRAINT `admins_ibfk_3` FOREIGN KEY (`token`) REFERENCES `accounts` (`token`) ON DELETE CASCADE;

--
-- Constraints for table `messenger`
--
ALTER TABLE `messenger`
  ADD CONSTRAINT `messenger_ibfk_1` FOREIGN KEY (`u1_email`) REFERENCES `accounts` (`email`),
  ADD CONSTRAINT `messenger_ibfk_2` FOREIGN KEY (`u2_email`) REFERENCES `accounts` (`email`);

--
-- Constraints for table `posts`
--
ALTER TABLE `posts`
  ADD CONSTRAINT `posts_ibfk_1` FOREIGN KEY (`author_acc_email`) REFERENCES `accounts` (`email`);

--
-- Constraints for table `profile`
--
ALTER TABLE `profile`
  ADD CONSTRAINT `profile_ibfk_1` FOREIGN KEY (`acc_id`) REFERENCES `accounts` (`account_id`),
  ADD CONSTRAINT `profile_ibfk_2` FOREIGN KEY (`acc_id`) REFERENCES `accounts` (`account_id`) ON DELETE CASCADE,
  ADD CONSTRAINT `profile_ibfk_3` FOREIGN KEY (`token`) REFERENCES `accounts` (`token`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
