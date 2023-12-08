CREATE TABLE tblorganization (
    id INT PRIMARY KEY AUTO_INCREMENT,
    is_deleted BIT(1),
    latitude DOUBLE,
    longitude DOUBLE,
    payment_strategy VARCHAR(255),
    type VARCHAR(255),
    owner_id INT,
    FOREIGN KEY (owner_id) REFERENCES tblaccount(id)
);