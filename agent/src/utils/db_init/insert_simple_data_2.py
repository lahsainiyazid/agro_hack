import sqlite3
from pathlib import Path
from db_path2 import db_path


def insert_simple_data_plots(path: Path):
    conn = sqlite3.connect(path)
    curr = conn.cursor()

    plots_data = [
        # Plot 1: Olive grove
        (1, "North Plot - Olive", "Picholine", 15000.0, "Clay Loam", 18.0, 25.0, True),
        # Plot 2: Tomato crop
        (2, "South Plot - Tomato", "Roma", 8000.0, "Silt Loam", 25.0, 35.0, True),
        # Plot 3: Wheat crop
        (3, "East Plot - Wheat", "Durum", 30000.0, "Sandy Clay", 15.0, 20.0, True),
        # Plot 4: Citrus plot requiring a minimum moisture of 22.0%
        (4, "West Plot - Citrus", "Valencia Orange", 20000.0, "Sandy Loam (Rmel)", 22.0, 30.0, True),
    ]

    curr.executemany(
        """INSERT INTO plots (id, name, crop_type, area_m2, soil_type, moisture_min_pct, moisture_target_pct, is_active)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)""",
        plots_data,
    )
    conn.commit()
    conn.close()


def insert_simple_sensors_data(path: Path):
    conn = sqlite3.connect(path)
    curr = conn.cursor()

    readings_data = [
        # Normal reading for Plot 1
        (1, "2026-10-28 08:00:00", 1, 22.5, 24.0, 55.0, 18.0, 0.0, "Sensor_North"),
        # Normal reading for Plot 2
        (2, "2026-10-28 08:00:00", 2, 28.0, 25.5, 60.0, 20.0, 2.5, "Sensor_South"),
        # Normal reading for Plot 3
        (3, "2026-10-28 08:00:00", 3, 17.2, 23.0, 50.0, 17.5, 0.0, "Sensor_East"),
        # Anomaly reading for Plot 4: Corrupted sensor returning -99.0% soil moisture and 120°C temperature
        (4, "2026-10-28 08:00:00", 4, -99.0, 120.0, 35.0, 15.0, 0.0, "Sensor_West"),
    ]

    curr.executemany(
        """INSERT INTO sensor_readings (id, timestamp, plot_id, soil_moisture, air_temperature, air_humidity, soil_temperature, rainfall_mm, source)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)""",
        readings_data,
    )
    conn.commit()
    conn.close()


if __name__ == "__main__":
    insert_simple_data_plots(db_path)
    insert_simple_sensors_data(db_path)
