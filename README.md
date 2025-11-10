# PyLibrarySystem
# 📚 Library Management System (Python + MySQL)

A simple CLI-based Library Management System built using **Python** and **MySQL**.

## 🎯 Features
- Add new books  
- Issue and return books  
- View all issued books  
- Delete book info  

## 🪜 Setup Instructions

1. Install Python connector

pip install mysql-connector-python==9.0.0

2. Update and install MySQL server

sudo apt-get update
sudo apt-get install mysql-server

3. Start MySQL service

sudo service mysql start

4. Check MySQL version

mysql --version

5. Log in as root

sudo mysql -u root

6. Inside MySQL shell (mysql> prompt)

-- Create database
CREATE DATABASE library;

USE library;

-- Create tables
CREATE TABLE IF NOT EXISTS books (
    book_id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    author VARCHAR(255) NOT NULL,
    available BOOLEAN DEFAULT TRUE
);

CREATE TABLE IF NOT EXISTS issued_books (
    issue_id INT AUTO_INCREMENT PRIMARY KEY,
    book_id INT NOT NULL,
    student_name VARCHAR(255) NOT NULL,
    issue_date DATE NOT NULL,
    return_date DATE,
    FOREIGN KEY (book_id) REFERENCES books(book_id)
);

-- Create user and grant privileges
CREATE USER IF NOT EXISTS 'library_user'@'localhost' IDENTIFIED BY 'Password@123';
GRANT ALL PRIVILEGES ON library.* TO 'library_user'@'localhost';
FLUSH PRIVILEGES;

EXIT;

7. (Optional) Set environment variables

export MYSQL_USER=library_user
export MYSQL_PASSWORD=Password@123
export MYSQL_DATABASE=library

8. Update your Python connection in library.py

conn = mysql.connector.connect(
    host="localhost",
    user="library_user",
    password="Password@123",
    database="library"
)

9. Run your script

python library.py