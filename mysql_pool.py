from mysql.connector.pooling import MySQLConnectionPool, PooledMySQLConnection

class MySQLPool:
    def __init__(self, host, user, password, database, port=3306) -> None:
        self.connection_pool = MySQLConnectionPool(
            pool_name="myPool",
            pool_size=16,
            host=host,
            user=user,
            password=password,
            database=database,
            port=port
        )

    def __enter__(self) -> PooledMySQLConnection:
        self.conn = self.connection_pool.get_connection()
        return self.conn
    
    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
        self.conn.commit()
        self.conn.close()
        self.conn = None
