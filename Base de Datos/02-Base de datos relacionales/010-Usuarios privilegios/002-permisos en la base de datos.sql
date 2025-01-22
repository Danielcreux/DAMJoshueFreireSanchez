-- Create the user
CREATE USER 'proyectoapple'@'localhost' IDENTIFIED BY 'Proyectoapple123$';

-- Grant all privileges on the database 'miempresa' to the user
GRANT ALL PRIVILEGES ON proyectoapple.* TO 'proyectoapple'@'localhost';

-- Apply the changes
FLUSH PRIVILEGES;
