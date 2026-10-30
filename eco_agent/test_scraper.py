import cloudscraper
from bs4 import BeautifulSoup 
scraper=cloudscraper.create_scraper()
response=scraper.get("https://marjane.ma/courses-en-ligne/11-marche")
soup=BeautifulSoup(response.text,"html.parser")
elements=soup.find_all("h2")
print(elements)

