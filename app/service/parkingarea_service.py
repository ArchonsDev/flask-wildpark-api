from mysql_pool import mysql_pool


class ParkingareaService:
    @staticmethod
    def add_parkingarea(slots):
        with mysql_pool as conn:
            query = "INSERT INTO tblparkingarea (slots) VALUES (%s)"
            c = conn.cursor()
            c.execute(query, (slots,))
            
    def get_all_parkingarea():
        with mysql_pool as conn:
            query = "SELECT * FROM tblparkingarea"
            c = conn.cursor()
            c.execute(query)
            return c.fetchall()
    
    def update_parkingarea(parking_area_id, slots):
        with mysql_pool as conn:
            query = "UPDATE tblparkingarea SET slots = %s WHERE id = %s"
            c = conn.cursor()
            c.execute(query, (slots, parking_area_id))
            return True
        
    def delete_parkingarea(parking_area_id):
        with mysql_pool as conn:
            query = "DELETE FROM tblparkingarea WHERE id = %s"
            c = conn.cursor()
            c.execute(query, (parking_area_id,))
            return True
