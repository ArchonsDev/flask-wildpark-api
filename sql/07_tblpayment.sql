CREATE TABLE tblpayment (
    id INT PRIMARY KEY AUTO_INCREMENT,
    amount FLOAT,
    date DATETIME,
    payment_type VARCHAR(255),
    payor_id INT,
    is_deleted BIT(1),
    FOREIGN KEY (payor_id) REFERENCES tblaccount (id)
);