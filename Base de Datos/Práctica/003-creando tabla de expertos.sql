CREATE TABLE `examenprogramacion`.`expertos` 
(`Identificador` INT (255) NOT NULL AUTO_INCREMENT , 
`nombre` VARCHAR(255) NOT NULL , 
`resumen` TEXT NOT NULL , 
`imagen` VARCHAR(255) NOT NULL , 
`video` VARCHAR(255) NOT NULL , 
`texto` TEXT NOT NULL , 
PRIMARY KEY (`Identificador`)) ENGINE = InnoDB;