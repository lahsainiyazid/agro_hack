import sqlite3 

def insert_simple_sensors_data():
    conn=sqlite3.connect("farm.db")
    curr=conn.cursor()
    readings_data = [(1, "2026-10-28 08:00:00", 1, 17.2, 21.5, 58.0, 18.5, 0.0, "Sensor_North"), 
                 (2, "2026-10-28 08:00:00", 2, 19.0, 20.0, 52.0, 17.0, 0.0, "Sensor_East"), 
                 (3, "2026-10-28 08:00:00", 3, 21.5, 22.0, 60.0, 19.0, 0.0, "Sensor_South")]
    curr.executemany("""
    INSERT INTO sensor_readings (id,timestamp,plot_id,soil_moisture,air_temperature,air_humidity,soil_temperature,rainfall_mm,source)
                      values(?,?,?,?,?,?,?,?,?)""",readings_data)
    conn.commit()
    conn.close()


if __name__=="__main__":
    insert_simple_sensors_data()
