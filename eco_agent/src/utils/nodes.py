from src.utils.objects import analyst
import cloudscraper 
from bs4 import BeautifulSoup
from typing import List,Dict

def fetch_data_bourse_agro(state:analyst):
    """
    This is a function to fetch data from bourseargo website
    """
    scraper=cloudscraper.create_scraper()
    response=scraper.get("https://bourseagro.com/prix/casa")
    soup=BeautifulSoup(response.text,"html.parser")
    products=[]
    for row in soup.select("tr[data-nom][data-prix]"):
        products.append({"nom":row["data-nom"],"prix":row["data-prix"]})
    return {"agro_bourse_data":products}
