CREATE TABLE tblvehicle (
    id INT PRIMARY KEY AUTO_INCREMENT,
    vehicle_type VARCHAR(255),
    color VARCHAR(255),
    is_deleted BIT(1),
    make VARCHAR(255),
    model VARCHAR(255),
    plate_number VARCHAR(255),
    type VARCHAR(255),
    displacement FLOAT,
    owner_id INT,
    parking_area_id INT,
    FOREIGN KEY (owner_id) REFERENCES tblaccount(id),
    FOREIGN KEY (parking_area_id) REFERENCES tblparkingarea(id)
);