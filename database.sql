-- Create database
CREATE DATABASE IF NOT EXISTS library;

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
CREATE USER IF NOT EXISTS 'library_user'@'localhost' IDENTIFIED BY 'Sravani@123';
GRANT ALL PRIVILEGES ON library.* TO 'library_user'@'localhost';
FLUSH PRIVILEGES;