CREATE TABLE tblvehicle (
    id INT PRIMARY KEY AUTO_INCREMENT,
    color VARCHAR(255),
    make VARCHAR(255),
    model VARCHAR(255),
    plate_number VARCHAR(255),
    owner_id INT,
    parking_area_id INT,
    FOREIGN KEY (owner_id) REFERENCES tblaccount(id),
    FOREIGN KEY (parking_area_id) REFERENCES tblparkingarea(id)
);