-- MySQL dump 10.13  Distrib 5.7.17, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: projektdb
-- ------------------------------------------------------
-- Server version	5.7.21-log

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `equipment`
--

DROP TABLE IF EXISTS `equipment`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `equipment` (
  `id_equipment` int(11) NOT NULL AUTO_INCREMENT,
  `id_weapon` int(11) NOT NULL,
  `id_helm` int(11) NOT NULL,
  `id_shoulders` int(11) NOT NULL,
  `id_chestplate` int(11) NOT NULL,
  `id_pants` int(11) NOT NULL,
  `id_gloves` int(11) NOT NULL,
  `id_boots` int(11) NOT NULL,
  PRIMARY KEY (`id_equipment`),
  KEY `weapon_id_weapon_fk` (`id_weapon`),
  KEY `helm_id_helm_fk` (`id_helm`),
  KEY `shoulders_id_shoulders_fk` (`id_shoulders`),
  KEY `chestplate_id_chestplate_fk` (`id_chestplate`),
  KEY `pants_id_pants_fk` (`id_pants`),
  KEY `gloves_id_gloves_fk` (`id_gloves`),
  KEY `boots_id_boots_fk` (`id_boots`),
  CONSTRAINT `boots_id_boots_fk` FOREIGN KEY (`id_boots`) REFERENCES `boots` (`id_boots`),
  CONSTRAINT `chestplate_id_chestplate_fk` FOREIGN KEY (`id_chestplate`) REFERENCES `chestplate` (`id_chestplate`),
  CONSTRAINT `gloves_id_gloves_fk` FOREIGN KEY (`id_gloves`) REFERENCES `gloves` (`id_gloves`),
  CONSTRAINT `helm_id_helm_fk` FOREIGN KEY (`id_helm`) REFERENCES `helm` (`id_helm`),
  CONSTRAINT `pants_id_pants_fk` FOREIGN KEY (`id_pants`) REFERENCES `pants` (`id_pants`),
  CONSTRAINT `shoulders_id_shoulders_fk` FOREIGN KEY (`id_shoulders`) REFERENCES `shoulders` (`id_shoulders`),
  CONSTRAINT `weapon_id_weapon_fk` FOREIGN KEY (`id_weapon`) REFERENCES `weapon` (`id_weapon`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `equipment`
--

LOCK TABLES `equipment` WRITE;
/*!40000 ALTER TABLE `equipment` DISABLE KEYS */;
INSERT INTO `equipment` VALUES (1,2,6,4,4,7,3,3);
/*!40000 ALTER TABLE `equipment` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2018-03-25 18:19:21
