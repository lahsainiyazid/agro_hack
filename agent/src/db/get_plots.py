import sqlite3 
from typing import List 
def show_all_plots()->List[str]:
    try:
        conn=sqlite3.connect("/home/yazid/agro/agent/src/db_init/farm.db")
        curr=conn.cursor()
        curr.execute("SELECT * FROM plots")
        return curr.fetchall()
    finally:
        conn.close()


if __name__=="__main__":
    all_plots=show_all_plots()
    print(all_plots)
