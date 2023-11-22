import mysql.connector.pooling

class MySQLPool:
    def __init__(self, **db_config) -> None:
        self.connection_pool = mysql.connector.pooling.MySQLConnectionPool(
            pool_name="myPool",
            pool_size=16,
            **db_config
        )

    def __enter__(self) -> mysql.connector.pooling.PooledMySQLConnection:
        self.conn = self.connection_pool.get_connection()
        return self.conn
    
    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
        self.conn.commit()
        self.conn.close()
        self.conn = None
