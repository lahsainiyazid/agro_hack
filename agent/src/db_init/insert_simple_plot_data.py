import sqlite3 

def insert_simple_data_plots():
    conn=sqlite3.connect("farm.db")
    curr=conn.cursor()
    plots_data = [
        (1,"North Plot - Olives","Picholine Olive",25000.0,"Silty Clay (Tirs)",18.0,25.0,True,),
        (2,"East Plot - Wheat","Durum Wheat",40000.0,"Clay Loam (Hamri)",15.0,22.0,True,),
        (3,"South Plot - Chickpeas","Chickpea",15000.0,"Loam",16.0,24.0,True,),]
    curr.executemany("""INSERT INTO plots (id,name,crop_type,area_m2,soil_type,moisture_min_pct,moisture_target_pct,is_active)
    values(?,?,?,?,?,?,?,?)""",plots_data)
    conn.commit()
    conn.close()

if __name__=="__main__":
    insert_simple_data_plots()
