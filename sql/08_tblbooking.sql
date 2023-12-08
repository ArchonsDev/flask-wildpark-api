CREATE TABLE tblbooking (
    id INT PRIMARY KEY AUTO_INCREMENT,
    date DATETIME,
    is_deleted BIT(1),
    duration FLOAT,
    parking_area_id  INT,
    vehicle_id INT,
    booker_id INT,
    payment_id INT,
    status VARCHAR(255),
    FOREIGN KEY (parking_area_id) REFERENCES tblparkingarea(id),
    FOREIGN KEY (vehicle_id) REFERENCES tblvehicle(id),
    FOREIGN KEY (booker_id) REFERENCES tblaccount(id),
    FOREIGN KEY (payment_id) REFERENCES tblpayment(id)
);