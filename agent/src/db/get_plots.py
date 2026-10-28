import sqlite3 
from typing import List 
from db_path import db_path
def show_all_plots(db_path:pathlib)->List[str]:
    try:
        conn=sqlite3.connect(db_path)
        curr=conn.cursor()
        curr.execute("SELECT * FROM plots")
        return curr.fetchall()
    finally:
        conn.close()


if __name__=="__main__":
    all_plots=show_all_plots(db_path)
    print(all_plots)
