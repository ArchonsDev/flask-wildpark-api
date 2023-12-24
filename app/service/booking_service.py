from mysql_pool import mysql_pool

class BookingService:
    # Create
    def create_booking(date, parking_area_id, vehicle_id, booker_id):
        try:
            with mysql_pool as conn:
                query = "CALL sp_CreateBooking(%s, %s, %s, %s)"
                c = conn.cursor()
                c.execute(query, (date, parking_area_id, vehicle_id, booker_id))
                conn.commit()
                return {"message": "Booking created successfully"}, 200
        except Exception as e:
            return {"error": e.msg}, 400
    
    # Read
    def get_all_bookings():
        with mysql_pool as conn:
            query = "SELECT * from vw_BookingDetails"
            c = conn.cursor()
            c.execute(query)
            rows = c.fetchall()

            columns = ['id', 'date', 'status', 'booker_id',  'firstname', 'lastname', 'vehicle_id', 'plate_number', 'parking_area_id']
            bookings = [dict(zip(columns, row)) for row in rows]

            return bookings
        
    def get_booking_by_id(id):
        with mysql_pool as conn:
            query = "SELECT * FROM tblbooking WHERE id=%s"
            c = conn.cursor()
            c.execute(query, (id,))
            row = c.fetchone()
            
            if row:
                columns = ['booking_id', 'date', 'parking_area_id', 'vehicle_id', 'booker_id', 'status']
                booking = dict(zip(columns, row))

                return booking

            return None
        
    # Update
    def update_booking(booking_id):
        with mysql_pool as conn:
            query = "UPDATE tblbooking set STATUS = 'Paid' where id = %s"
            c = conn.cursor()
            c.execute(query, (booking_id,))

    # Delete
    def delete_booking(id):
        with mysql_pool as conn:
            query = "DELETE FROM tblbooking WHERE id=%s"
            c = conn.cursor()
            c.execute(query, (id,))

            return c.rowcount > 0
