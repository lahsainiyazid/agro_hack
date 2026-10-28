import sqlite3 
from typing import List
from db_path import db_path

def get_all_readings(db_path:pathlib)->List[dict]:
    conn=sqlite3.connect(db_path)
    try:
        curr=conn.cursor()
        curr.execute("SELECT * from sensor_readings")
        return curr.fetchall()
    finally:
        conn.close()
def get_last_24_readings(db_path:pathlib)->List[dict]:
    conn=sqlite3.connect(db_path)
    try:
        curr=conn.cursor()
        curr.execute("""SELECT * from sensor_readings
            order by timestamp desc 
            limit 24""")
        return curr.fetchall()
    finally:
        conn.close()


if __name__=="__main__":
    my_sensors=get_all_readings(db_path)
    last_24_sensors=get_last_24_readings(db_path)
    print(my_sensors)
    print("Our last 24 readings are:")
    print(last_24_sensors)
