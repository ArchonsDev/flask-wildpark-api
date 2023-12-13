from mysql_pool import mysql_pool

class ParkingareaService:
    def update_parkingarea(id, *args, **kwargs):
            pass
    
    def delete_parkingarea(id):
        with mysql_pool as conn:
            query = "DELETE FROM tblparkingarea WHERE id = %s"
            c = conn.cursor()
            c.execute(query, (id,))
            return True