import sqlite3 


def insert_simple_wrong_sensors_data():
    conn=sqlite3.connect("farm.db")
    curr=conn.cursor()
    readings_data=[]
