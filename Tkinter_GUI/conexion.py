import mysql.connector
class DataBase:
    def __init__(self):
        self.connection=mysql.connector.connect(
            host="localhost",
            user="root",
            password="**********",
            database="bienes_raices_future"
        )
        
        self.cursor = self.connection.cursor()