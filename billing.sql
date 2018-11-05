-- phpMyAdmin SQL Dump
-- version 4.6.6deb5
-- https://www.phpmyadmin.net/
--
-- Host: localhost:3306
-- Generation Time: Nov 06, 2018 at 02:34 PM
-- Server version: 8.0.13
-- PHP Version: 7.2.10-0ubuntu0.18.04.1

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `billing`
--

-- --------------------------------------------------------

--
-- Table structure for table `admincredentials`
--

CREATE TABLE `admincredentials` (
  `username` varchar(40) NOT NULL,
  `password` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `admincredentials`
--

INSERT INTO `admincredentials` (`username`, `password`) VALUES
('root', 'toor'),
('time', 'time');

-- --------------------------------------------------------

--
-- Table structure for table `constantfields`
--

CREATE TABLE `constantfields` (
  `name` varchar(20) NOT NULL,
  `value` float NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `constantfields`
--

INSERT INTO `constantfields` (`name`, `value`) VALUES
('gstrate', 15),
('vat', 5);

-- --------------------------------------------------------

--
-- Table structure for table `invoice_data`
--

CREATE TABLE `invoice_data` (
  `entryID` int(11) NOT NULL,
  `date` date NOT NULL,
  `product` varchar(40) NOT NULL,
  `rate` int(11) NOT NULL,
  `quantity` int(11) NOT NULL,
  `gstrate` int(11) NOT NULL,
  `stax` int(11) NOT NULL,
  `subtotal` int(11) NOT NULL,
  `total` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `invoice_data`
--

INSERT INTO `invoice_data` (`entryID`, `date`, `product`, `rate`, `quantity`, `gstrate`, `stax`, `subtotal`, `total`) VALUES
(2, '2018-10-21', 'mouse', 700, 1, 20, 2, 700, 854),
(4, '2018-10-21', 'musicbox', 5000, 1, 15, 2, 5000, 5850),
(7, '2018-10-11', 'computer', 30000, 1, 15, 3, 30000, 35400),
(8, '2018-10-22', 'Keyboard', 900, 1, 15, 6, 900, 1089),
(9, '2018-10-22', 'Headphones', 400, 1, 15, 3, 400, 472),
(11, '2018-11-07', 'mouse', 500, 7, 5, 2, 3500, 3745);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `invoice_data`
--
ALTER TABLE `invoice_data`
  ADD PRIMARY KEY (`entryID`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `invoice_data`
--
ALTER TABLE `invoice_data`
  MODIFY `entryID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=12;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
