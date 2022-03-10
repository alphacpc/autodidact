-- MySQL dump 10.13  Distrib 8.0.28, for Linux (x86_64)
--
-- Host: localhost    Database: Exercice1
-- ------------------------------------------------------
-- Server version	8.0.28

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `correspondance`
--

DROP TABLE IF EXISTS `correspondance`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `correspondance` (
  `id_p` int NOT NULL,
  `id_veh` int NOT NULL,
  PRIMARY KEY (`id_p`,`id_veh`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `correspondance`
--

LOCK TABLES `correspondance` WRITE;
/*!40000 ALTER TABLE `correspondance` DISABLE KEYS */;
INSERT INTO `correspondance` VALUES (5,2),(9,19),(12,5),(19,2);
/*!40000 ALTER TABLE `correspondance` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `piece`
--

DROP TABLE IF EXISTS `piece`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `piece` (
  `id_p` int NOT NULL AUTO_INCREMENT,
  `categorie` varchar(100) DEFAULT NULL,
  `date_recup` date DEFAULT NULL,
  `id_ref` int DEFAULT NULL,
  PRIMARY KEY (`id_p`),
  KEY `id_ref` (`id_ref`),
  CONSTRAINT `piece_ibfk_1` FOREIGN KEY (`id_ref`) REFERENCES `reference` (`id_ref`)
) ENGINE=InnoDB AUTO_INCREMENT=25 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `piece`
--

LOCK TABLES `piece` WRITE;
/*!40000 ALTER TABLE `piece` DISABLE KEYS */;
INSERT INTO `piece` VALUES (2,'mecanique','2012-11-20',9684),(4,'mecanique','2012-11-20',9684),(5,'Electrique','2007-04-20',9683),(6,'Electrique','2007-01-20',9691),(7,'Carosserie','2010-01-20',9689),(8,'Mecanique','2006-07-20',9686),(9,'Electrique','2014-01-20',9687),(10,'Carosserie','2012-11-20',9683),(11,'Carosserie','2014-08-20',9688),(12,'Carosserie','2029-09-20',9690),(13,'Mecanique','2016-05-20',9691),(14,'Electrique','2013-06-20',9687),(15,'Mecanique','2027-01-20',9688),(16,'Electrique','2015-06-20',9688),(17,'Carosserie','2025-08-20',9689),(18,'Electrique','2013-07-20',9688),(19,'Carosserie','2005-03-20',9683),(20,'Mecanique','2019-10-20',9686),(21,'Mecanique','2006-10-20',9683),(22,'Electrique','2020-08-20',9687),(23,'Carosserie','2016-04-20',9689),(24,'Mecanique','2023-07-20',9689);
/*!40000 ALTER TABLE `piece` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `reference`
--

DROP TABLE IF EXISTS `reference`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `reference` (
  `id_ref` int NOT NULL AUTO_INCREMENT,
  `prix` float DEFAULT '0',
  PRIMARY KEY (`id_ref`)
) ENGINE=InnoDB AUTO_INCREMENT=9692 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `reference`
--

LOCK TABLES `reference` WRITE;
/*!40000 ALTER TABLE `reference` DISABLE KEYS */;
INSERT INTO `reference` VALUES (9683,1500000),(9684,2500000),(9685,3500000),(9686,4500000),(9687,5500000),(9688,6500000),(9689,7500000),(9690,8500000),(9691,9500000);
/*!40000 ALTER TABLE `reference` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `vehicule`
--

DROP TABLE IF EXISTS `vehicule`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `vehicule` (
  `id_veh` int NOT NULL AUTO_INCREMENT,
  `marque` varchar(25) DEFAULT NULL,
  `annee` int DEFAULT NULL,
  `modele` varchar(25) DEFAULT NULL,
  PRIMARY KEY (`id_veh`)
) ENGINE=InnoDB AUTO_INCREMENT=20 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `vehicule`
--

LOCK TABLES `vehicule` WRITE;
/*!40000 ALTER TABLE `vehicule` DISABLE KEYS */;
INSERT INTO `vehicule` VALUES (1,'Chevrolet',2020,'C2020X'),(2,'Rolls Royce',2022,'R2022V4'),(3,'Dodge',2019,'D2019B7'),(4,'Tesla',2019,'T2019V4'),(5,'Chevrolet',2018,'C2018Y'),(6,'Mercedes-Benz',2022,'M2022Y'),(7,'Lamborghini',2019,'L2019Y'),(8,'Chevrolet',2021,'C2021FX'),(9,'Lamborghini',2018,'L2018B7'),(10,'Chevrolet',2021,'C2021B7'),(11,'Chevrolet',2021,'C2021B7'),(12,'Ford',2018,'F2018FX'),(13,'Lamborghini',2022,'L2022B7'),(14,'Lamborghini',2021,'L2021Z9'),(15,'Porsche',2020,'P2020B7'),(16,'Rolls Royce',2019,'R2019B7'),(17,'Porsche',2021,'P2021X'),(18,'Rolls Royce',2021,'R2021Z9'),(19,'Dodge',2022,'D2022V4');
/*!40000 ALTER TABLE `vehicule` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-03-10  8:27:14
