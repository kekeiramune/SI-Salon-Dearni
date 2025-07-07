-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jul 07, 2025 at 05:13 PM
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
-- Database: `salon_dearni`
--

-- --------------------------------------------------------

--
-- Table structure for table `absensi`
--

CREATE TABLE `absensi` (
  `id_absensi` int(11) NOT NULL,
  `id_staff` int(11) DEFAULT NULL,
  `tanggal` date DEFAULT NULL,
  `jam_masuk` time DEFAULT NULL,
  `jam_keluar` time DEFAULT NULL,
  `status` enum('Hadir','Izin','Alpa') DEFAULT NULL,
  `keterangan` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `absensi`
--

INSERT INTO `absensi` (`id_absensi`, `id_staff`, `tanggal`, `jam_masuk`, `jam_keluar`, `status`, `keterangan`) VALUES
(2, 1, '2025-05-01', '10:00:00', '15:00:00', 'Hadir', 'Hadir tepat waktu'),
(4, 2, '2025-06-26', '11:00:00', '17:00:00', 'Hadir', 'Hadir tepat waktu'),
(5, 1, '2025-07-05', '10:00:00', '16:00:00', 'Izin', 'Izin Sakit');

-- --------------------------------------------------------

--
-- Table structure for table `customer`
--

CREATE TABLE `customer` (
  `id_customer` int(11) NOT NULL,
  `nama_customer` varchar(100) DEFAULT NULL,
  `alamat` varchar(255) DEFAULT NULL,
  `no_telp` varchar(15) DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL,
  `password` varchar(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `customer`
--

INSERT INTO `customer` (`id_customer`, `nama_customer`, `alamat`, `no_telp`, `email`, `password`) VALUES
(1, 'Sheryl', 'Depok', '082338170454', 'sheryla123@gmail.com', 'cust123');

-- --------------------------------------------------------

--
-- Table structure for table `detail_restock`
--

CREATE TABLE `detail_restock` (
  `id_detail_restock` int(11) NOT NULL,
  `id_restock` int(11) DEFAULT NULL,
  `id_produk` int(11) DEFAULT NULL,
  `jumlah` int(11) DEFAULT NULL,
  `harga_satuan` decimal(10,2) DEFAULT NULL,
  `subtotal` decimal(10,2) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `detail_restock`
--

INSERT INTO `detail_restock` (`id_detail_restock`, `id_restock`, `id_produk`, `jumlah`, `harga_satuan`, `subtotal`) VALUES
(1, 1, 12, 2, 30000.00, 60000.00);

-- --------------------------------------------------------

--
-- Table structure for table `detail_transaksi_layanan`
--

CREATE TABLE `detail_transaksi_layanan` (
  `id_detail_transaksi` int(11) NOT NULL,
  `id_transaksi` int(11) DEFAULT NULL,
  `id_layanan` int(11) DEFAULT NULL,
  `harga` decimal(10,2) DEFAULT NULL,
  `jumlah` int(11) DEFAULT NULL,
  `subtotal` decimal(10,2) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `layanan`
--

CREATE TABLE `layanan` (
  `id_layanan` int(11) NOT NULL,
  `nama_layanan` varchar(100) DEFAULT NULL,
  `deskripsi` varchar(255) DEFAULT NULL,
  `harga` decimal(10,2) DEFAULT NULL,
  `durasi_menit` int(11) DEFAULT NULL,
  `kategori` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `layanan`
--

INSERT INTO `layanan` (`id_layanan`, `nama_layanan`, `deskripsi`, `harga`, `durasi_menit`, `kategori`) VALUES
(1, 'Creambath', 'Perawatan dengan krim khusus disertai pijatan untuk menutrisi rambut dan relaksasi', 75000.00, 45, 'Perawatan Rambut'),
(2, 'Hair Spa', 'Menutrisi dan mengatasi masalah rambut tertentu seperti rambut kering, kusam, dan rusak', 100000.00, 60, 'Perawatan Rambut'),
(3, 'Manicure & Pedicure Spa', 'Perawatan kuku tangan dan kaki yang mencakup pemotongan, pembersihan, pengikiran.', 120000.00, 75, 'Perawatan Kuku'),
(4, 'Pedicure Spa', 'Perawatan kaki yang meliputi pembersihan, pengikiran, pengangkatan sel kulit mati, dan pijatan untuk menjaga kesehatan dan keindahan kaki.', 114000.00, 60, 'Perawatan Kuku'),
(5, 'Refleksiologi Kaki', 'Pijatan pada titik-titik refleksi di kaki untuk merangsang organ tubuh, mengurangi stres, dan meningkatkan keseimbangan energi.', 152000.00, 60, 'Pijat & Relaksasi'),
(6, 'Balinese Massage', 'Pijatan tradisional Bali yang menggabungkan teknik pijat, akupresur, dan aromaterapi untuk meredakan ketegangan otot dan meningkatkan relaksasi.', 90000.00, 60, 'Pijat & Relaksasi');

-- --------------------------------------------------------

--
-- Table structure for table `produk`
--

CREATE TABLE `produk` (
  `id_produk` int(11) NOT NULL,
  `id_supplier` int(11) DEFAULT NULL,
  `nama_produk` varchar(100) DEFAULT NULL,
  `deskripsi` varchar(255) DEFAULT NULL,
  `harga_beli` decimal(10,2) DEFAULT NULL,
  `stok` int(11) DEFAULT NULL,
  `satuan` varchar(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `produk`
--

INSERT INTO `produk` (`id_produk`, `id_supplier`, `nama_produk`, `deskripsi`, `harga_beli`, `stok`, `satuan`) VALUES
(1, 1, 'Pewarna Rambut', 'Warna merah', 30000.00, 1, 'pcs'),
(2, 2, 'Shampoo Anti Rontok', 'untuk customer yg punya masalah rambut rontok', 300000.00, 15, 'pcs'),
(3, 1, 'Hair Mask Avocado', 'masker rambut dari alpukat untuk rambut kering dan rusak', 150000.00, 20, 'pcs'),
(4, 3, 'Cat Rambut Coklat Natural', 'warna rambut alami dengan formula non-amonia', 85000.00, 30, 'tube'),
(5, 1, 'Facial Cleanser Tea Tree', 'pembersih wajah untuk kulit berjerawat', 60000.00, 25, 'botol'),
(6, 2, 'Massage Oil Lavender', 'minyak pijat aromatherapy lavender menenangkan', 50000.00, 10, 'botol'),
(7, 1, 'Serum Vitamin C', 'mencerahkan dan menyamarkan noda hitam pada wajah', 120000.00, 18, 'pcs'),
(8, 3, 'Hair Spray Extra Hold', 'menjaga gaya rambut tahan lama', 45000.00, 22, 'pcs'),
(9, 1, 'Bleaching Powder', 'digunakan untuk proses pewarnaan rambut', 70000.00, 12, 'pak'),
(10, 3, 'Body Scrub Herbal', 'lulur tradisional dengan bahan alami', 90000.00, 14, 'jar'),
(11, 2, 'Nail Polish Merah Maroon', 'kutek warna merah maroon tahan lama', 35000.00, 28, 'botol'),
(12, 1, 'Hair Spray', 'aroma mint dan terasa segar', 30000.00, 20, 'pcs'),
(16, 2, 'Cat Rambut Warna Merah', 'Cat rambut untuk bleaching merah', 40000.00, 2, 'pcs');

-- --------------------------------------------------------

--
-- Table structure for table `reservasi`
--

CREATE TABLE `reservasi` (
  `id_reservasi` int(11) NOT NULL,
  `id_customer` int(11) DEFAULT NULL,
  `tanggal_reservasi` date DEFAULT NULL,
  `jam_reservasi` time DEFAULT NULL,
  `id_layanan` int(11) DEFAULT NULL,
  `id_staff` int(11) DEFAULT NULL,
  `status` enum('Selesai','Belum Selesai','Ditunda') DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `reservasi`
--

INSERT INTO `reservasi` (`id_reservasi`, `id_customer`, `tanggal_reservasi`, `jam_reservasi`, `id_layanan`, `id_staff`, `status`) VALUES
(1, 1, '2025-07-07', '09:11:00', 1, 2, 'Selesai'),
(2, 1, '2025-07-08', '10:30:00', 2, 2, 'Selesai');

-- --------------------------------------------------------

--
-- Table structure for table `restock_produk`
--

CREATE TABLE `restock_produk` (
  `id_restock` int(11) NOT NULL,
  `tanggal_restock` date DEFAULT NULL,
  `total_biaya` decimal(10,2) DEFAULT NULL,
  `status` varchar(20) DEFAULT NULL,
  `id_staff` int(11) DEFAULT NULL,
  `id_produk` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `restock_produk`
--

INSERT INTO `restock_produk` (`id_restock`, `tanggal_restock`, `total_biaya`, `status`, `id_staff`, `id_produk`) VALUES
(1, '2025-07-05', 60000.00, 'Ordered', 1, 12);

-- --------------------------------------------------------

--
-- Table structure for table `staff`
--

CREATE TABLE `staff` (
  `id_staff` int(11) NOT NULL,
  `nama_staff` varchar(100) DEFAULT NULL,
  `alamat` varchar(255) DEFAULT NULL,
  `no_telp` varchar(15) DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL,
  `posisi` varchar(50) DEFAULT NULL,
  `password` varchar(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `staff`
--

INSERT INTO `staff` (`id_staff`, `nama_staff`, `alamat`, `no_telp`, `email`, `posisi`, `password`) VALUES
(1, 'Devi', 'Jln. Rancho Indah', '082338170454', 'devisipy1@gmail.com', 'owner', 'pass123'),
(2, 'Ratna', 'Depok Baru', '082338190367', 'rina55@gmail.com', 'karyawan', 'pass124');

-- --------------------------------------------------------

--
-- Table structure for table `supplier`
--

CREATE TABLE `supplier` (
  `id_supplier` int(11) NOT NULL,
  `nama_supplier` varchar(100) DEFAULT NULL,
  `alamat` varchar(100) DEFAULT NULL,
  `no_telp` varchar(100) DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `supplier`
--

INSERT INTO `supplier` (`id_supplier`, `nama_supplier`, `alamat`, `no_telp`, `email`) VALUES
(1, 'Rina', 'Depok', '081273849502', 'rina123@gmail.com'),
(2, 'Agus', 'Jakarta', '082134765421', 'agus_tokoonline@gmail.com'),
(3, 'Siti', 'Bandung', '085783920145', 'siti.fashion@yahoo.com');

-- --------------------------------------------------------

--
-- Table structure for table `transaksi_layanan`
--

CREATE TABLE `transaksi_layanan` (
  `id_transaksi` int(11) NOT NULL,
  `id_reservasi` int(11) DEFAULT NULL,
  `tanggal_transaksi` date DEFAULT NULL,
  `total_bayar` decimal(10,2) DEFAULT NULL,
  `metode_pembayaran` enum('Cash','Transfer','Qris') DEFAULT NULL,
  `status_pembayaran` enum('Lunas','Belum Lunas') DEFAULT 'Belum Lunas'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `transaksi_layanan`
--

INSERT INTO `transaksi_layanan` (`id_transaksi`, `id_reservasi`, `tanggal_transaksi`, `total_bayar`, `metode_pembayaran`, `status_pembayaran`) VALUES
(1, 1, '2025-07-07', 75000.00, 'Transfer', 'Lunas'),
(2, 2, '2025-07-08', 100000.00, 'Qris', 'Belum Lunas');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `absensi`
--
ALTER TABLE `absensi`
  ADD PRIMARY KEY (`id_absensi`),
  ADD KEY `id_staff` (`id_staff`);

--
-- Indexes for table `customer`
--
ALTER TABLE `customer`
  ADD PRIMARY KEY (`id_customer`);

--
-- Indexes for table `detail_restock`
--
ALTER TABLE `detail_restock`
  ADD PRIMARY KEY (`id_detail_restock`),
  ADD KEY `id_restock` (`id_restock`),
  ADD KEY `id_barang` (`id_produk`);

--
-- Indexes for table `detail_transaksi_layanan`
--
ALTER TABLE `detail_transaksi_layanan`
  ADD PRIMARY KEY (`id_detail_transaksi`),
  ADD KEY `id_transaksi` (`id_transaksi`),
  ADD KEY `id_layanan` (`id_layanan`);

--
-- Indexes for table `layanan`
--
ALTER TABLE `layanan`
  ADD PRIMARY KEY (`id_layanan`);

--
-- Indexes for table `produk`
--
ALTER TABLE `produk`
  ADD PRIMARY KEY (`id_produk`),
  ADD KEY `id_supplier` (`id_supplier`);

--
-- Indexes for table `reservasi`
--
ALTER TABLE `reservasi`
  ADD PRIMARY KEY (`id_reservasi`),
  ADD KEY `id_customer` (`id_customer`),
  ADD KEY `id_layanan` (`id_layanan`),
  ADD KEY `id_staff` (`id_staff`);

--
-- Indexes for table `restock_produk`
--
ALTER TABLE `restock_produk`
  ADD PRIMARY KEY (`id_restock`),
  ADD KEY `id_staff` (`id_staff`),
  ADD KEY `fk_id_produk` (`id_produk`);

--
-- Indexes for table `staff`
--
ALTER TABLE `staff`
  ADD PRIMARY KEY (`id_staff`);

--
-- Indexes for table `supplier`
--
ALTER TABLE `supplier`
  ADD PRIMARY KEY (`id_supplier`);

--
-- Indexes for table `transaksi_layanan`
--
ALTER TABLE `transaksi_layanan`
  ADD PRIMARY KEY (`id_transaksi`),
  ADD KEY `id_reservasi` (`id_reservasi`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `absensi`
--
ALTER TABLE `absensi`
  MODIFY `id_absensi` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT for table `customer`
--
ALTER TABLE `customer`
  MODIFY `id_customer` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `detail_restock`
--
ALTER TABLE `detail_restock`
  MODIFY `id_detail_restock` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `layanan`
--
ALTER TABLE `layanan`
  MODIFY `id_layanan` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT for table `produk`
--
ALTER TABLE `produk`
  MODIFY `id_produk` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=17;

--
-- AUTO_INCREMENT for table `reservasi`
--
ALTER TABLE `reservasi`
  MODIFY `id_reservasi` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `restock_produk`
--
ALTER TABLE `restock_produk`
  MODIFY `id_restock` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `staff`
--
ALTER TABLE `staff`
  MODIFY `id_staff` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `transaksi_layanan`
--
ALTER TABLE `transaksi_layanan`
  MODIFY `id_transaksi` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `absensi`
--
ALTER TABLE `absensi`
  ADD CONSTRAINT `absensi_ibfk_1` FOREIGN KEY (`id_staff`) REFERENCES `staff` (`id_staff`);

--
-- Constraints for table `detail_restock`
--
ALTER TABLE `detail_restock`
  ADD CONSTRAINT `detail_restock_ibfk_1` FOREIGN KEY (`id_restock`) REFERENCES `restock_produk` (`id_restock`),
  ADD CONSTRAINT `detail_restock_ibfk_2` FOREIGN KEY (`id_produk`) REFERENCES `produk` (`id_produk`);

--
-- Constraints for table `detail_transaksi_layanan`
--
ALTER TABLE `detail_transaksi_layanan`
  ADD CONSTRAINT `detail_transaksi_layanan_ibfk_1` FOREIGN KEY (`id_transaksi`) REFERENCES `transaksi_layanan` (`id_transaksi`),
  ADD CONSTRAINT `detail_transaksi_layanan_ibfk_2` FOREIGN KEY (`id_layanan`) REFERENCES `layanan` (`id_layanan`);

--
-- Constraints for table `produk`
--
ALTER TABLE `produk`
  ADD CONSTRAINT `produk_ibfk_1` FOREIGN KEY (`id_supplier`) REFERENCES `supplier` (`id_supplier`);

--
-- Constraints for table `reservasi`
--
ALTER TABLE `reservasi`
  ADD CONSTRAINT `reservasi_ibfk_1` FOREIGN KEY (`id_customer`) REFERENCES `customer` (`id_customer`),
  ADD CONSTRAINT `reservasi_ibfk_2` FOREIGN KEY (`id_layanan`) REFERENCES `layanan` (`id_layanan`),
  ADD CONSTRAINT `reservasi_ibfk_3` FOREIGN KEY (`id_staff`) REFERENCES `staff` (`id_staff`);

--
-- Constraints for table `restock_produk`
--
ALTER TABLE `restock_produk`
  ADD CONSTRAINT `fk_id_produk` FOREIGN KEY (`id_produk`) REFERENCES `produk` (`id_produk`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `restock_produk_ibfk_1` FOREIGN KEY (`id_staff`) REFERENCES `staff` (`id_staff`);

--
-- Constraints for table `transaksi_layanan`
--
ALTER TABLE `transaksi_layanan`
  ADD CONSTRAINT `transaksi_layanan_ibfk_1` FOREIGN KEY (`id_reservasi`) REFERENCES `reservasi` (`id_reservasi`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
