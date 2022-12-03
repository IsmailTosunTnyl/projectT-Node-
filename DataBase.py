import mysql.connector
from dotenv import load_dotenv
import os

load_dotenv()
print(os.getenv('dbHost'))

class DB():

    def __init__(self):
        self.mydb = mysql.connector.connect(user=os.getenv('dbUser'), password=os.getenv('dbPassword'),
                                    host=os.getenv('dbHost'),
                                    database=os.getenv('dbDatabase'))


if __name__ == "__main__":
    db = DB()
    print(db.mydb)