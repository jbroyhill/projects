
--
-- Table structure for table `employees`
--

DROP TABLE IF EXISTS `employees`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `employees` (
  `EmployeeID` int(11) NOT NULL,
  `EmployeeName` varchar(45) NOT NULL,
  `EmployeeTypeID` int(11) NOT NULL DEFAULT '1',
  `PayTypeID` int(11) NOT NULL DEFAULT '1',
  `CompanyID` int(11) NOT NULL,
  `ProjectID` int(11) NOT NULL,
  PRIMARY KEY (`EmployeeID`),
  KEY `EmploeeTypeID_idx` (`EmployeeTypeID`),
  KEY `PayTypeID_idx` (`PayTypeID`),
  KEY `CompanyID_idx` (`CompanyID`),
  KEY `ProID_idx` (`ProjectID`),
  CONSTRAINT `CompanyID` FOREIGN KEY (`CompanyID`) REFERENCES `gamecompany` (`CompanyID`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `EmployeeTypeID` FOREIGN KEY (`EmployeeTypeID`) REFERENCES `employeetype` (`EmployeeTypeID`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `PayTypeID` FOREIGN KEY (`PayTypeID`) REFERENCES `paytype` (`PayTypeID`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `ProID` FOREIGN KEY (`ProjectID`) REFERENCES `project` (`ProjectID`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `employees`
--

LOCK TABLES `employees` WRITE;
/*!40000 ALTER TABLE `employees` DISABLE KEYS */;
INSERT INTO `employees` VALUES (1,'Fred',1,1,0,0),(2,'Chuck',1,1,0,0),(3,'Clarence',1,1,0,0),(4,'Sam',1,1,0,0),(5,'Carly',1,1,0,0),(6,'ose',2,1,0,0),(7,'Sarah',2,1,0,0),(8,'Victoria',2,1,0,0),(9,'Ben',2,1,0,0),(10,'Ned',2,2,0,0),(11,'Val',3,2,0,0),(12,'Dana',3,2,0,0),(13,'Thomas',3,2,0,0),(14,'Larry',3,2,0,0),(15,'Haileu',3,2,0,0),(16,'Andrew',4,2,0,0),(17,'Ryan',4,2,0,0),(18,'Minnie',4,2,0,0),(19,'Roxy',4,2,0,0),(20,'August',4,2,0,0);
/*!40000 ALTER TABLE `employees` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `employeetype`
--

DROP TABLE IF EXISTS `employeetype`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `employeetype` (
  `EmployeeTypeID` int(11) NOT NULL DEFAULT '1',
  `Programmer` varchar(45) NOT NULL,
  `Artist` varchar(45) NOT NULL,
  `Designer` varchar(45) NOT NULL,
  `Producer` varchar(45) NOT NULL,
  `EmployeeTypeDescription` varchar(45) NOT NULL,
  PRIMARY KEY (`EmployeeTypeID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `employeetype`
--

LOCK TABLES `employeetype` WRITE;
/*!40000 ALTER TABLE `employeetype` DISABLE KEYS */;
INSERT INTO `employeetype` VALUES (1,'1','0','0','0','Programmer'),(2,'0','1','0','0','Artist'),(3,'0','0','1','0','Designer'),(4,'0','0','0','1','Producer');
/*!40000 ALTER TABLE `employeetype` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `gamecompany`
--

DROP TABLE IF EXISTS `gamecompany`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `gamecompany` (
  `CompanyID` int(11) NOT NULL,
  PRIMARY KEY (`CompanyID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `gamecompany`
--

LOCK TABLES `gamecompany` WRITE;
/*!40000 ALTER TABLE `gamecompany` DISABLE KEYS */;
INSERT INTO `gamecompany` VALUES (1);
/*!40000 ALTER TABLE `gamecompany` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `paytype`
--

DROP TABLE IF EXISTS `paytype`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `paytype` (
  `PayTypeID` int(11) NOT NULL DEFAULT '1',
  `TypeDescription` varchar(45) NOT NULL,
  `TypeAmounts` varchar(45) NOT NULL,
  PRIMARY KEY (`PayTypeID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `paytype`
--

LOCK TABLES `paytype` WRITE;
/*!40000 ALTER TABLE `paytype` DISABLE KEYS */;
INSERT INTO `paytype` VALUES (1,'Low Pay','$30-60'),(2,'High Pay','$61-150');
/*!40000 ALTER TABLE `paytype` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `project`
--

DROP TABLE IF EXISTS `project`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `project` (
  `ProjectID` int(11) NOT NULL,
  `ProjectName` varchar(45) NOT NULL,
  `ProjectShipDate` varchar(45) NOT NULL,
  `ProjectStateID` int(11) NOT NULL,
  `ProjectTypeID` int(11) NOT NULL,
  `CompanyID` int(11) NOT NULL,
  PRIMARY KEY (`ProjectID`),
  KEY `ProjectStateID_idx` (`ProjectStateID`),
  KEY `ProjectTypeID_idx` (`ProjectTypeID`),
  KEY `CompanyID_idx` (`CompanyID`),
  CONSTRAINT `CompID` FOREIGN KEY (`CompanyID`) REFERENCES `gamecompany` (`CompanyID`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `ProjectStateID` FOREIGN KEY (`ProjectStateID`) REFERENCES `projectstate` (`ProjectStateID`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `ProjectTypeID` FOREIGN KEY (`ProjectTypeID`) REFERENCES `projecttype` (`ProjectTypeID`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `project`
--

LOCK TABLES `project` WRITE;
/*!40000 ALTER TABLE `project` DISABLE KEYS */;
INSERT INTO `project` VALUES (1,'Bucket','01-20-19',1,1,0),(2,'Handle','05-20-19',1,1,0),(3,'Wave','06-31-20',2,2,0),(4,'Sword','11-20-21',2,2,0),(5,'Shield','10-20-25',3,2,0);
/*!40000 ALTER TABLE `project` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `projectstate`
--

DROP TABLE IF EXISTS `projectstate`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `projectstate` (
  `ProjectStateID` int(11) NOT NULL,
  `StateDescription` varchar(45) NOT NULL,
  PRIMARY KEY (`ProjectStateID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `projectstate`
--

LOCK TABLES `projectstate` WRITE;
/*!40000 ALTER TABLE `projectstate` DISABLE KEYS */;
INSERT INTO `projectstate` VALUES (1,'Near release'),(2,'Deep Development'),(3,'Long Development');
/*!40000 ALTER TABLE `projectstate` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `projecttype`
--

DROP TABLE IF EXISTS `projecttype`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `projecttype` (
  `ProjectTypeID` int(11) NOT NULL,
  `TypeDescription` varchar(45) NOT NULL,
  PRIMARY KEY (`ProjectTypeID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `projecttype`
--

LOCK TABLES `projecttype` WRITE;
/*!40000 ALTER TABLE `projecttype` DISABLE KEYS */;
INSERT INTO `projecttype` VALUES (1,'Puzzle Game'),(2,'Adventure Game');
/*!40000 ALTER TABLE `projecttype` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2019-10-12 23:47:52
