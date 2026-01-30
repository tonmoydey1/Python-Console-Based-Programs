CREATE DATABASE bank_db;
USE bank_db;


CREATE TABLE accounts (
    account_no INT AUTO_INCREMENT PRIMARY KEY,
    customer_name VARCHAR(100),
    account_type VARCHAR(20),
    balance INT,
    status VARCHAR(20)
);



CREATE TABLE transactions (
    transaction_id INT AUTO_INCREMENT PRIMARY KEY,
    account_no INT,
    transaction_type VARCHAR(20),
    amount INT,
    transaction_date DATE
);
