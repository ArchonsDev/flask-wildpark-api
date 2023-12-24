from mysql_pool import mysql_pool

class VehicleService:
    def add_vehicle(color, make, model, 
                    plate_number, owner_id, parking_area_id):
        with mysql_pool as conn:
            query = "INSERT INTO tblvehicle(color, make, model, plate_number, owner_id, parking_area_id) VALUES (%s, %s, %s, %s, %s, %s)"
            c = conn.cursor()
            c.execute(query, ( color, make, model, plate_number, owner_id, parking_area_id))
                
    def get_all_vehicles():
        with mysql_pool as conn:
            query = "SELECT * FROM tblvehicle"
            c = conn.cursor()
            c.execute(query)
            return c.fetchall()
        
    def get_vehicle_by_vehicle_id(vehicle_id):
        with mysql_pool as conn:
            query = "SELECT * FROM tblvehicle WHERE id=%s"
            c = conn.cursor()
            c.execute(query, (vehicle_id))
        
    def update_vehicle(vehicle_id, data):
        color = data.get('color', None)
        plate_number = data.get('plate_number', None)
        
        with mysql_pool as conn:
            query = "CALL sp_UpdateVehicle(%s, %s, %s)"
            c = conn.cursor()
            c.execute(query, (vehicle_id, color, plate_number))
            return True
    
    def delete_vehicle(vehicle_id):
        with mysql_pool as conn:
            query = "DELETE FROM tblvehicle WHERE id = %s"
            c = conn.cursor()
            c.execute(query, (vehicle_id,))
            return True
