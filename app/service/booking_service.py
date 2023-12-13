from mysql_pool import mysql_pool

class BookingService:
    # Create
    def create_booking(date, parking_area_id, vehicle_id, booker_id):
        with mysql_pool as conn:
            query = "CALL sp_CreateBooking(%s, %s, %s, %s)"
            c = conn.cursor()
            c.execute(query, (date, parking_area_id, vehicle_id, booker_id))
    # Read
    def get_all_bookings():
        with mysql_pool as conn:
            query = "SELECT * from vw_BookingDetails"
            c = conn.cursor()
            c.execute(query)

            return c.fetchall()
        
    def get_booking_by_id(id):
        with mysql_pool as conn:
            query = "SELECT * FROM tblbooking WHERE id=%s"
            c = conn.cursor()
            c.execute(query, (id,))

            return c.fetchone()
        
    # Update
    def update_booking(booking_id, data):
        booker_id = data.get('booker_id')
        date = data.get('date', None) 
        parking_area_id = data.get('parking_area_id', None)
        vehicle_id = data.get('vehicle_id', None)
        status = data.get('status', None)
        
        with mysql_pool as conn:
            query = "CALL sp_UpdateBooking(%s, %s, %s, %s, %s, %s)"
            c = conn.cursor()
            c.execute(query, (booking_id, booker_id, date, parking_area_id, vehicle_id, status))
    
    # No idea how to do this LOL thought might be aight to use 
    def pay_booking(booking_id, booker_id):
        with mysql_pool as conn:
            query = "UPDATE tblbooking SET status = 'Paid' where booking_id = %s AND booker_id = %s"
            c = conn.cursor()
            c.execute(query, (booking_id, booker_id))

    # Delete
    def delete_booking(id):
        with mysql_pool as conn:
            query = "DELETE FROM tblbooking WHERE id=%s"
            c = conn.cursor()
            c.execute(query, (id,))

            return c.rowcount > 0
