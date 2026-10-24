import pandas as pd 
import requests 
from urls import url 

params = {
    "latitude": 33.5731,
    "longitude": -7.5898,
    "start_date": "2010-01-01",
    "end_date": "2025-12-31",
    "daily": ",".join([
        "temperature_2m_mean", "temperature_2m_max", "temperature_2m_min",
        "precipitation_sum", "rain_sum", "precipitation_hours",
        "relative_humidity_2m_mean", "surface_pressure_mean",
        "cloud_cover_mean", "dew_point_2m_mean",
        "wind_speed_10m_max", "wind_gusts_10m_max",
        "wind_direction_10m_dominant",
        "shortwave_radiation_sum", "et0_fao_evapotranspiration",
    ]),
    "timezone": "Africa/Casablanca",
}
r=requests.get(url.strip(),params=params,timeout=60)
r.raise_for_status()
data=r.json()
df=pd.DataFrame(data['daily'])
df['time']=pd.to_datetime(df['time'])
df=df.rename(columns={'time':'date'}).set_index('date')
df['city']='Casablanca'
df.to_csv('casa_2010_2025_daily.csv')
print(df.isna().sum())
print(df.head())

