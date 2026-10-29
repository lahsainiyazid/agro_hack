import sqlite3 
from typing import List,Dict 
from pathlib import Path 
from src.utils.db.db_path import db_path

def get_all_plots(db_path:Path)->List[Dict]:
    with sqlite3.connect(db_path) as conn:
        conn.row_factory=sqlite3.Row 
        curr=conn.cursor()
        curr.execute("SELECT * FROM plots ")
        return [dict(row) for row in curr.fetchall()]


if __name__=="__main__":
  my_plots=get_all_plots(db_path)
  print(my_plots)
