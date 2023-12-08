CREATE TABLE tblorganizationmember (
    organization_id INT,
    account_id INT,
    FOREIGN KEY (organization_id) REFERENCES tblorganization(id),
    FOREIGN KEY (account_id) REFERENCES tblaccount(id)
);