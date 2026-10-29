import sqlite3 
from pathlib import Path 
from db_path import db_path 
def insert_simple_data_plots(path:Path):
    conn=sqlite3.connect("farm.db")
    curr=conn.cursor()
    plots_data = [
      # Plot 4: Citrus plot requiring a minimum moisture of 22.0%
      (4,"West Plot - Citrus","Valencia Orange",20000.0,"Sandy Loam (Rmel)",22.0,30.0,True,),]
    curr.executemany(
      """INSERT INTO plots (id,name,crop_type,area_m2,soil_type,moisture_min_pct,moisture_target_pct,is_active)
    values(?,?,?,?,?,?,?,?)""",
      plots_data,)
    conn.commit()
    conn.close()


if __name__=="__main__":
    insert_simple_data_plots(db_path)
