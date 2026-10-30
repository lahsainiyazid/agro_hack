import pandas as pd
from pathlib import Path 
from src.utils.db.db_path2 import db_path 
from src.utils.db.get_sensors2 import get_last_24h_readings 


def check_anomaly(path:Path=db_path):
    df=pd.DataFrame(get_last_24h_readings(db_path))
    print(df)

if __name__=="__main__":
    check_anomaly()

