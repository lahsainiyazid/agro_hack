import sqlite3
from pathlib import Path 
from db_path import db_path 
def insert_simple_sensors_data(path:Path):
  conn = sqlite3.connect("farm.db")
  curr = conn.cursor()
  readings_data = [
        (
          4,
          "2026-10-28 08:00:00",
          4,
          5.8,
          100,
          15.0,
          35.0,
          0.0,
          "Sensor_West",
      ),
  ]
  curr.executemany(
      """
    INSERT INTO sensor_readings (id,timestamp,plot_id,soil_moisture,air_temperature,air_humidity,soil_temperature,rainfall_mm,source)
                    values(?,?,?,?,?,?,?,?,?)""",
      readings_data,
  )
  conn.commit()
  conn.close()


if __name__ == "__main__":
  insert_simple_sensors_data(db_path)
