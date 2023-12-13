from mysql_pool import mysql_pool

class VehicleService:
    def add_vehicle(self, vehicle_type, color, is_deleted, make, model, 
                    plate_number, type, displacement, owner_id, parking_area_id):
        with mysql_pool as conn:
            query = "INSERT INTO tblvehicle(vehicle_type, color, is_deleted, make, model, plate_number, type, displacement, owner_id, parking_area_id) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
            c = conn.cursor()
            c.execute(query, (vehicle_type, color, is_deleted, make, model, plate_number, type, displacement, owner_id, parking_area_id))
                
    def get_all_vehicles(self):
        with mysql_pool as conn:
            query = "SELECT * FROM tblvehicle"
            c = conn.cursor()
            c.execute(query)
            return c.fetchall()
        
    def get_vehicle_by_owner_id(owner_id):
        with mysql_pool as conn:
            query = "SELECT * FROM tblvehicle WHERE owner_id=%s"
            c = conn.cursor()
            c.execute(query, (owner_id))
        
    def update_vehicle(self, owner_id, **updated_fields):
        with mysql_pool as conn: 
            set_clause = ", ".join(f"{field} = %s" for field in updated_fields.keys())
            query = f"""UPDATE tblvehicle SET {set_clause} WHERE owner_id = %s"""
            
            values = list(updated_fields.values()) + [owner_id]
            c = conn.cursor()
            c.execute(query, values)
            return True
    
    def delete_vehicle(self, owner_id):
        with mysql_pool as conn:
            query = "DELETE FROM tblvehicle WHERE owner_id = %s"
            c = conn.cursor()
            c.execute(query, (owner_id,))
            return True
