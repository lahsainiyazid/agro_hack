import sqlite3 


def create_sensor_readings_table():
    conn=sqlite3.connect("farm.db")
    cur=conn.cursor()
    cur.execute("""
    Create table IF NOT EXISTS sensor_readings
                       (id integer  PRIMARY KEY,
                       timestamp datetime,
                       plot_id integer references plots(id),
                       soil_moisture REAL ,
                       air_temperature REAL ,
                       air_humidity REAL ,
                       soil_temperature REAL ,
                       rainfall_mm REAL ,
                       source TEXT) """)
    conn.commit()
    conn.close()

def create_plots_table():
    conn=sqlite3.connect("farm.db")
    cur=conn.cursor()
    cur.execute("""
    Create table IF NOT EXISTS plots 
    (id integer  PRIMARY KEY,
    name TEXT,
    crop_type TEXT,
    area_m2 REAL,
    soil_type TEXT,
    moisture_min_pct REAL,
    moisture_target_pct REAL,
    is_active BOOLEAN
     )
                   """)
    conn.commit()
    conn.close()

create_plots_table()
create_sensor_readings_table()
