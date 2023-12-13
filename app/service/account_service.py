from mysql_pool import mysql_pool

class AccountService:
    def create_account(firstname, lastname):
        with mysql_pool as conn:
            query = "INSERT INTO tblaccount (firstname, lastname) VALUES (%s, %s)"
            c = conn.cursor()
            c.execute(query, (firstname, lastname))

    def get_all_accounts():
        with mysql_pool as conn:
            query = "SELECT * FROM tblaccount"
            c = conn.cursor()
            c.execute(query)

            return c.fetchall()
        
    def get_account_by_id(id):
        with mysql_pool as conn:
            query = "SELECT * FROM tblaccount WHERE id=%s"
            c = conn.cursor()
            c.execute(query, (id,))

            return c.fetchone()
        
    def update_account(id, *args, **kwargs):
        pass

    def delete_account(id):
        with mysql_pool as conn:
            query = "DELETE FROM tblaccount WHERE id=%s"
            c = conn.cursor()
            c.execute(query, (id,))

            return True