DELIMITER //
CREATE PROCEDURE sp_InsertAccount(
    IN p_firstname VARCHAR(255),
    IN p_lastname VARCHAR(255)
)
BEGIN
    INSERT INTO tblaccount (firstname, lastname) VALUES (p_firstname, p_lastname);
END //

CREATE PROCEDURE sp_DeleteAccount(
    IN p_account_id INT
)
BEGIN
    DELETE FROM tblaccount WHERE id = p_account_id;
END //

DELIMITER //
CREATE PROCEDURE sp_InsertVehicle(
    IN p_color VARCHAR(255),
    IN p_make VARCHAR(255),
    IN p_model VARCHAR(255),
    IN p_plate_number VARCHAR(255),
    IN p_owner_id INT,
    IN p_parking_area_id INT
)
BEGIN
    INSERT INTO tblvehicle (color, make, model, plate_number, owner_id, parking_area_id)
    VALUES (p_color, p_make, p_model, p_plate_number, p_owner_id, p_parking_area_id);
END //

CREATE PROCEDURE sp_DeleteVehicle(
    IN p_owner_id INT
)
BEGIN
    DELETE FROM tblvehicle WHERE id = p_owner_id;
END //

DELIMITER //
CREATE PROCEDURE sp_UpdateVehicle(
    IN p_vehicle_id INT,
    IN p_owner_id INT,
    IN p_color VARCHAR(255), 
    IN p_make VARCHAR(255),
    IN p_model VARCHAR(255), 
    IN p_plate_number VARCHAR(255), 
    IN p_parking_area_id INT
)
BEGIN
    UPDATE tblvehicle
    SET
        color = COALESCE(p_color, color),
        make = COALESCE(p_make, make),
        model = COALESCE(p_model, model),
        plate_number = COALESCE(p_plate_number, plate_number),
        parking_area_id = COALESCE(p_parking_area_id, parking_area_id)
    WHERE
        id = p_vehicle_id and owner_id = p_owner_id;
END //

DELIMITER //
CREATE PROCEDURE sp_UpdateBookingStatus(
    IN p_booking_id INT,
    IN p_status VARCHAR(255)
)
BEGIN
    UPDATE tblbooking SET status = p_status WHERE id = p_booking_id;
END //

DELIMITER //
CREATE TRIGGER tr_AfterDeleteAccount
AFTER DELETE ON tblaccount
FOR EACH ROW
BEGIN
    DELETE FROM tblvehicle WHERE owner_id = OLD.id;
END //

DELIMITER ;

CREATE VIEW vw_VehiclesWithOwners AS
SELECT
    v.id AS vehicle_id,
    v.color,
    v.make,
    v.model,
    v.plate_number,
    a.id AS owner_id,
    a.firstname AS owner_firstname,
    a.lastname AS owner_lastname
FROM
    tblvehicle v
    JOIN tblaccount a ON v.owner_id = a.id;

CREATE VIEW vw_BookingDetails AS
SELECT
    b.id AS booking_id,
    b.date,
    b.status,
    a.id AS booker_id,
    a.firstname AS booker_firstname,
    a.lastname AS booker_lastname,
    v.id AS vehicle_id,
    v.plate_number,
    pa.id AS parking_area_id
FROM
    tblbooking b
    JOIN tblaccount a ON b.booker_id = a.id
    JOIN tblvehicle v ON b.vehicle_id = v.id
    JOIN tblparkingarea pa ON b.parking_area_id = pa.id;
