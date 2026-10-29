import sqlite3 
from typing import List,Tuple
from src.utils.db.db_path import db_path
def get_all_plots(db_path:pathlib)->List[Tuple]:
    try:
        conn=sqlite3.connect(db_path)
        curr=conn.cursor()
        curr.execute("SELECT * FROM plots")
        return curr.fetchall()
    finally:
        conn.close()

def get_plots_ids(db_path:pathlib)->List[Tuple]:
    try:
        conn=sqlite3.connect(db_path)
        curr=conn.cursor()
        curr.execute("Select id from plots")
        return curr.fetchall()
    finally:
        conn.close()
if __name__=="__main__":
    all_plots=get_all_plots(db_path)
    all_ids=get_plots_ids(db_path)
    print("Our plots are:\n")
    print(all_plots)
    print("Our ids are:\n")
    print(all_ids)
