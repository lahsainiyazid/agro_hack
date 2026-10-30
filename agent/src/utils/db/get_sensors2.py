import sqlite3 
from typing import List,Tuple
from src.utils.db.db_path2 import db_path

def get_all_readings(db_path:Pathlib)->List[dict]:
    with sqlite3.connect(db_path) as conn:
        conn.row_factory=sqlite3.Row 
        curr=conn.cursor()
        curr.execute("SELECT * FROM sensor_readings")
        return [dict(row) for row in curr.fetchall()]
        
def get_last_24h_readings(db_path:pathlib)->List[dict]:
    with sqlite3.connect(db_path) as conn:
        conn.row_factory=sqlite3.Row 
        curr=conn.cursor()
        curr.execute("""SELECT * from sensor_readings 
         where timestamp>datetime ((SELECT MAX(timestamp) from sensor_readings),'-24 hours')
         order by timestamp desc""")
        return [dict(row) for row in curr.fetchall()]
def get_last_12h_readings(db_path:pathlib)->List[dict]:
    with sqlite3.connect(db_path) as conn:
        conn.row_factory=sqlite3.Row 
        curr=conn.cursor()
        curr.execute("""SELECT * from sensor_readings 
         where timestamp>datetime ((SELECT MAX(timestamp) from sensor_readings),'-12 hours')
         order by timestamp desc""")
        return [dict(row) for row in curr.fetchall()]


def get_last_6h_readings(db_path:pathlib)->List[dict]:
    with sqlite3.connect(db_path) as conn:
        conn.row_factory=sqlite3.Row 
        curr=conn.cursor()
        curr.execute("""SELECT * from sensor_readings 
         where timestamp>datetime ((SELECT MAX(timestamp) from sensor_readings),'-6 hours')
         order by timestamp desc""")
        return [dict(row) for row in curr.fetchall()]


def get_last_3h_readings(db_path:pathlib)->List[dict]:
    with sqlite3.connect(db_path) as conn:
        conn.row_factory=sqlite3.Row 
        curr=conn.cursor()
        curr.execute("""SELECT * from sensor_readings 
         where timestamp>datetime ((SELECT MAX(timestamp) from sensor_readings),'-3 hours')
         order by timestamp desc""")
        return [dict(row) for row in curr.fetchall()]


def get_last_h_readings(db_path:pathlib)->List[dict]:
    with sqlite3.connect(db_path) as conn:
        conn.row_factory=sqlite3.Row 
        curr=conn.cursor()
        curr.execute("""SELECT * from sensor_readings 
         where timestamp>datetime ((SELECT MAX(timestamp) from sensor_readings),'-1 hour')
         order by timestamp desc""")
        return [dict(row) for row in curr.fetchall()]



if __name__=="__main__":
    my_sensors=get_all_readings(db_path)
    last_24h_sensors=get_last_24h_readings(db_path)
    last_12h_readings=get_last_12h_readings(db_path)
    last_3h_readings=get_last_3h_readings(db_path)
    last_h_readings=get_last_h_readings(db_path)
    print(my_sensors)
    print("Our last 24hours readings are:")
    print(last_24h_sensors)
    print("Our last 12 hours readings are:")
    print(last_12h_readings)
    print("Our last 3 hours readings are:")
    print(last_3h_readings)
    print("Our last hour readings are:")
    print(last_h_readings)
    
