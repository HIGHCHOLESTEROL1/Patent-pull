import Scrapper
from bs4 import BeautifulSoup
import requests

def readData(url):
    ## html data
    response = requests.get(url)
    ## parse the html data
    soup = BeautifulSoup(response.content, 'html.parser')
    f = open("data/data.txt", 'w', encoding="utf-8")
    f.write(scrapper.name(soup))
    f.write(scrapper.patentNum(soup))
    f.write(scrapper.countryOrgin(soup))
    f.write(scrapper.status(soup))
    f.write(scrapper.founders(soup))
    f.close()
