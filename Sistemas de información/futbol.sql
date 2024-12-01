-- MariaDB dump 10.19  Distrib 10.4.32-MariaDB, for Win64 (AMD64)
--
-- Host: localhost    Database: futbol
-- ------------------------------------------------------
-- Server version	10.4.32-MariaDB

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `divisiones`
--

DROP TABLE IF EXISTS `divisiones`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `divisiones` (
  `Identificador` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(255) NOT NULL,
  PRIMARY KEY (`Identificador`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `divisiones`
--

LOCK TABLES `divisiones` WRITE;
/*!40000 ALTER TABLE `divisiones` DISABLE KEYS */;
INSERT INTO `divisiones` VALUES (1,'Primera'),(2,'Segunda'),(3,'Primera Federación'),(4,'Segunda Federación');
/*!40000 ALTER TABLE `divisiones` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `equipos`
--

DROP TABLE IF EXISTS `equipos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `equipos` (
  `Identificador` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(255) NOT NULL,
  `divisiones_nombre` int(11) NOT NULL,
  PRIMARY KEY (`Identificador`),
  KEY `divisonesaequipos` (`divisiones_nombre`),
  CONSTRAINT `divisonesaequipos` FOREIGN KEY (`divisiones_nombre`) REFERENCES `divisiones` (`Identificador`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `equipos`
--

LOCK TABLES `equipos` WRITE;
/*!40000 ALTER TABLE `equipos` DISABLE KEYS */;
INSERT INTO `equipos` VALUES (1,'Mislata Club de Futbol',2),(2,'Manises CF',2);
/*!40000 ALTER TABLE `equipos` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `equipos_copia`
--

DROP TABLE IF EXISTS `equipos_copia`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `equipos_copia` (
  `Identificador` int(11) NOT NULL DEFAULT 0,
  `nombre` varchar(255) NOT NULL,
  `divisiones_nombre` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `equipos_copia`
--

LOCK TABLES `equipos_copia` WRITE;
/*!40000 ALTER TABLE `equipos_copia` DISABLE KEYS */;
INSERT INTO `equipos_copia` VALUES (1,'Mislata Club de Futbol',2),(2,'Manises CF',2);
/*!40000 ALTER TABLE `equipos_copia` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `fichajes`
--

DROP TABLE IF EXISTS `fichajes`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `fichajes` (
  `Identificador` int(11) NOT NULL AUTO_INCREMENT,
  `valor` decimal(15,2) NOT NULL,
  `jugadores_nombre` int(11) NOT NULL,
  `equipos_nombre` int(11) NOT NULL,
  `fechainicio` date NOT NULL,
  `fechafinal` date NOT NULL,
  PRIMARY KEY (`Identificador`),
  KEY `jugadoresafichaje` (`jugadores_nombre`),
  KEY `equiposafichaje` (`equipos_nombre`),
  CONSTRAINT `equiposafichaje` FOREIGN KEY (`equipos_nombre`) REFERENCES `equipos` (`Identificador`),
  CONSTRAINT `jugadoresafichaje` FOREIGN KEY (`jugadores_nombre`) REFERENCES `jugadores` (`Identificador`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `fichajes`
--

LOCK TABLES `fichajes` WRITE;
/*!40000 ALTER TABLE `fichajes` DISABLE KEYS */;
INSERT INTO `fichajes` VALUES (1,10000000.00,1,1,'2024-10-16','2025-10-15');
/*!40000 ALTER TABLE `fichajes` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `jornadas`
--

DROP TABLE IF EXISTS `jornadas`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `jornadas` (
  `Identificador` int(255) NOT NULL AUTO_INCREMENT,
  `fecha` date NOT NULL,
  `divisiones_nombre` int(11) NOT NULL,
  PRIMARY KEY (`Identificador`),
  KEY `divisionesajornadas` (`divisiones_nombre`),
  CONSTRAINT `divisionesajornadas` FOREIGN KEY (`divisiones_nombre`) REFERENCES `divisiones` (`Identificador`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `jornadas`
--

LOCK TABLES `jornadas` WRITE;
/*!40000 ALTER TABLE `jornadas` DISABLE KEYS */;
INSERT INTO `jornadas` VALUES (1,'2024-10-08',2);
/*!40000 ALTER TABLE `jornadas` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `jugadores`
--

DROP TABLE IF EXISTS `jugadores`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `jugadores` (
  `Identificador` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(255) NOT NULL,
  `apellidos` varchar(255) NOT NULL,
  `fechadenacimiento` date NOT NULL,
  `paises_nombre` int(11) NOT NULL,
  PRIMARY KEY (`Identificador`),
  KEY `paisesajugadores` (`paises_nombre`),
  CONSTRAINT `paisesajugadores` FOREIGN KEY (`paises_nombre`) REFERENCES `paises` (`Identificador`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `jugadores`
--

LOCK TABLES `jugadores` WRITE;
/*!40000 ALTER TABLE `jugadores` DISABLE KEYS */;
INSERT INTO `jugadores` VALUES (1,'Iker','Casillas','2003-03-12',162),(2,'Roberto','Levandos','1985-11-15',7);
/*!40000 ALTER TABLE `jugadores` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `jugadores_copia`
--

DROP TABLE IF EXISTS `jugadores_copia`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `jugadores_copia` (
  `Identificador` int(11) NOT NULL DEFAULT 0,
  `nombre` varchar(255) NOT NULL,
  `apellidos` varchar(255) NOT NULL,
  `fechadenacimiento` date NOT NULL,
  `paises_nombre` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `jugadores_copia`
--

LOCK TABLES `jugadores_copia` WRITE;
/*!40000 ALTER TABLE `jugadores_copia` DISABLE KEYS */;
INSERT INTO `jugadores_copia` VALUES (1,'Iker','Casillas','2003-03-12',162),(2,'Roberto','Levandos','1985-11-15',7);
/*!40000 ALTER TABLE `jugadores_copia` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `paises`
--

DROP TABLE IF EXISTS `paises`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `paises` (
  `Identificador` int(255) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(255) NOT NULL,
  PRIMARY KEY (`Identificador`)
) ENGINE=InnoDB AUTO_INCREMENT=195 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `paises`
--

LOCK TABLES `paises` WRITE;
/*!40000 ALTER TABLE `paises` DISABLE KEYS */;
INSERT INTO `paises` VALUES (1,'Afghanistan'),(2,'Albania'),(3,'Algeria'),(4,'Andorra'),(5,'Angola'),(6,'Antigua and Barbuda'),(7,'Argentina'),(8,'Armenia'),(9,'Australia'),(10,'Austria'),(11,'Azerbaijan'),(12,'Bahamas'),(13,'Bahrain'),(14,'Bangladesh'),(15,'Barbados'),(16,'Belarus'),(17,'Belgium'),(18,'Belize'),(19,'Benin'),(20,'Bhutan'),(21,'Bolivia'),(22,'Bosnia and Herzegovina'),(23,'Botswana'),(24,'Brazil'),(25,'Brunei'),(26,'Bulgaria'),(27,'Burkina Faso'),(28,'Burundi'),(29,'Cabo Verde'),(30,'Cambodia'),(31,'Cameroon'),(32,'Canada'),(33,'Central African Republic'),(34,'Chad'),(35,'Chile'),(36,'China'),(37,'Colombia'),(38,'Comoros'),(39,'Congo (Congo-Brazzaville)'),(40,'Congo (Democratic Republic)'),(41,'Costa Rica'),(42,'Croatia'),(43,'Cuba'),(44,'Cyprus'),(45,'Czech Republic'),(46,'Denmark'),(47,'Djibouti'),(48,'Dominica'),(49,'Dominican Republic'),(50,'Ecuador'),(51,'Egypt'),(52,'El Salvador'),(53,'Equatorial Guinea'),(54,'Eritrea'),(55,'Estonia'),(56,'Eswatini'),(57,'Ethiopia'),(58,'Fiji'),(59,'Finland'),(60,'France'),(61,'Gabon'),(62,'Gambia'),(63,'Georgia'),(64,'Germany'),(65,'Ghana'),(66,'Greece'),(67,'Grenada'),(68,'Guatemala'),(69,'Guinea'),(70,'Guinea-Bissau'),(71,'Guyana'),(72,'Haiti'),(73,'Honduras'),(74,'Hungary'),(75,'Iceland'),(76,'India'),(77,'Indonesia'),(78,'Iran'),(79,'Iraq'),(80,'Ireland'),(81,'Israel'),(82,'Italy'),(83,'Jamaica'),(84,'Japan'),(85,'Jordan'),(86,'Kazakhstan'),(87,'Kenya'),(88,'Kiribati'),(89,'Kuwait'),(90,'Kyrgyzstan'),(91,'Laos'),(92,'Latvia'),(93,'Lebanon'),(94,'Lesotho'),(95,'Liberia'),(96,'Libya'),(97,'Liechtenstein'),(98,'Lithuania'),(99,'Luxembourg'),(100,'Madagascar'),(101,'Malawi'),(102,'Malaysia'),(103,'Maldives'),(104,'Mali'),(105,'Malta'),(106,'Marshall Islands'),(107,'Mauritania'),(108,'Mauritius'),(109,'Mexico'),(110,'Micronesia'),(111,'Moldova'),(112,'Monaco'),(113,'Mongolia'),(114,'Montenegro'),(115,'Morocco'),(116,'Mozambique'),(117,'Myanmar (Burma)'),(118,'Namibia'),(119,'Nauru'),(120,'Nepal'),(121,'Netherlands'),(122,'New Zealand'),(123,'Nicaragua'),(124,'Niger'),(125,'Nigeria'),(126,'North Korea'),(127,'North Macedonia'),(128,'Norway'),(129,'Oman'),(130,'Pakistan'),(131,'Palau'),(132,'Panama'),(133,'Papua New Guinea'),(134,'Paraguay'),(135,'Peru'),(136,'Philippines'),(137,'Poland'),(138,'Portugal'),(139,'Qatar'),(140,'Romania'),(141,'Russia'),(142,'Rwanda'),(143,'Saint Kitts and Nevis'),(144,'Saint Lucia'),(145,'Saint Vincent and the Grenadines'),(146,'Samoa'),(147,'San Marino'),(148,'Sao Tome and Principe'),(149,'Saudi Arabia'),(150,'Senegal'),(151,'Serbia'),(152,'Seychelles'),(153,'Sierra Leone'),(154,'Singapore'),(155,'Slovakia'),(156,'Slovenia'),(157,'Solomon Islands'),(158,'Somalia'),(159,'South Africa'),(160,'South Korea'),(161,'South Sudan'),(162,'Spain'),(163,'Sri Lanka'),(164,'Sudan'),(165,'Suriname'),(166,'Sweden'),(167,'Switzerland'),(168,'Syria'),(169,'Taiwan'),(170,'Tajikistan'),(171,'Tanzania'),(172,'Thailand'),(173,'Timor-Leste'),(174,'Togo'),(175,'Tonga'),(176,'Trinidad and Tobago'),(177,'Tunisia'),(178,'Turkey'),(179,'Turkmenistan'),(180,'Tuvalu'),(181,'Uganda'),(182,'Ukraine'),(183,'United Arab Emirates'),(184,'United Kingdom'),(185,'United States of America'),(186,'Uruguay'),(187,'Uzbekistan'),(188,'Vanuatu'),(189,'Vatican City'),(190,'Venezuela'),(191,'Vietnam'),(192,'Yemen'),(193,'Zambia'),(194,'Zimbabwe');
/*!40000 ALTER TABLE `paises` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `partidos`
--

DROP TABLE IF EXISTS `partidos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `partidos` (
  `Identificador` int(255) NOT NULL AUTO_INCREMENT,
  `visitante` int(255) NOT NULL,
  `local` int(255) NOT NULL,
  `jornada` int(255) NOT NULL,
  `horadeinicio` time NOT NULL,
  `golesvisitante` int(255) NOT NULL,
  `goleslocal` int(255) NOT NULL,
  PRIMARY KEY (`Identificador`),
  KEY `visitanteapartido` (`visitante`),
  KEY `localapartido` (`local`),
  KEY `jornadaapartido` (`jornada`),
  CONSTRAINT `jornadaapartido` FOREIGN KEY (`jornada`) REFERENCES `jornadas` (`Identificador`),
  CONSTRAINT `localapartido` FOREIGN KEY (`local`) REFERENCES `equipos` (`Identificador`),
  CONSTRAINT `visitanteapartido` FOREIGN KEY (`visitante`) REFERENCES `equipos` (`Identificador`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `partidos`
--

LOCK TABLES `partidos` WRITE;
/*!40000 ALTER TABLE `partidos` DISABLE KEYS */;
INSERT INTO `partidos` VALUES (1,2,1,1,'21:00:00',1,3);
/*!40000 ALTER TABLE `partidos` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-11-29 20:15:20
