CREATE DATABASE movie_db;
USE movie_db;



CREATE TABLE movies (
    movie_id INT AUTO_INCREMENT PRIMARY KEY,
    movie_name VARCHAR(100),
    show_time VARCHAR(50),
    ticket_price INT,
    available_seats INT
);


CREATE TABLE bookings (
    booking_id INT AUTO_INCREMENT PRIMARY KEY,
    movie_name VARCHAR(100),
    seats_booked INT,
    total_amount INT,
    booking_date DATE
);
