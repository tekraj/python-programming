import pymysql

class Database:
    def __init__(self, host, user, password, database):
        self.connection = None
        try:
            self.connection = pymysql.connect(
                host=host,
                user=user,
                password=password,
                database=database,
                cursorclass=pymysql.cursors.DictCursor
            )
        except pymysql.MySQLError as e:
            print(f"Error: {e}")

    def execute_query(self, query, params=None):
        """Execute a query and return results."""
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(query, params or ())
                self.connection.commit()
                return cursor.fetchall()
        except pymysql.MySQLError as e:
            print(f"Error: {e}")
            return None

    def close_connection(self):
        if self.connection:
            self.connection.close()
