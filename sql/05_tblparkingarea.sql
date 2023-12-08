CREATE TABLE tblparkingarea (
    id INT PRIMARY KEY AUTO_INCREMENT,
    is_deleted BIT(1),
    slots INT,
    organization_id INT,
    FOREIGN KEY (organization_id) REFERENCES tblorganization(id)
);