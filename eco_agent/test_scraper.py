import cloudscraper
from bs4 import BeautifulSoup 
def fetch_data_bourse_agro():
    scraper=cloudscraper.create_scraper()
    response=scraper.get("https://bourseagro.com/prix/casa")
    soup=BeautifulSoup(response.text,"html.parser")
    products=[]
    for row in soup.select("tr[data-nom][data-prix]"):
        products.append({"name":row["data-nom"],
                     "price":row["data-prix"]})
    return products


if __name__=="__main__":
   products=fetch_data_bourse_agro()
   print(products)
