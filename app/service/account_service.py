from mysql_pool import mysql_pool
from ..models import AccountModel

class AccountService:
    def create_account(firstname, lastname):
        with mysql_pool as conn:
            query = "CALL sp_InsertAccount(%(firstname)s, %(lastname)s, @inserted_id)"
            params = {
                "firstname": firstname,
                "lastname": lastname
            }
            c = conn.cursor()
            c.execute(query, params)
            
            c.execute("SELECT @inserted_id")
            inserted_id = c.fetchone()[0]

            conn.commit()

            return AccountModel(inserted_id, firstname, lastname)

    def get_all_accounts():
        with mysql_pool as conn:
            query = "SELECT * FROM tblaccount"
            c = conn.cursor()
            c.execute(query)
            rows = c.fetchall()

            accounts = []
            for data in rows:
                accounts.append(AccountModel(*data).to_dict())

            return accounts

        
    def get_account_by_id(id):
        with mysql_pool as conn:
            query = "SELECT * FROM tblaccount WHERE id=%(id)s"
            params = {
                "id": id
            }
            c = conn.cursor()
            c.execute(query, params)
            data = c.fetchone()

            return AccountModel(*data)
        
    def update_account(id, firstname, lastname):
        with mysql_pool as conn:
            query = "CALL sp_UpdateAccount(%(id)s, %(firstname)s, %(lastname)s, @new_firstname, @new_lastname)"
            params = {
                "id": id,
                "firstname": firstname,
                "lastname": lastname
            }
            c = conn.cursor()
            c.execute(query, params)

            c.execute("SELECT @new_firstname, @new_lastname")
            result = c.fetchone()

            return AccountModel(id, result[0], result[1])

    def delete_account(id):
        with mysql_pool as conn:
            query = "CALL sp_DeleteAccount(%(id)s)"
            params = {
                "id": id
            }
            c = conn.cursor()
            c.execute(query, params)
