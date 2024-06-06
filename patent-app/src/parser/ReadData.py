import Scrapper
from bs4 import BeautifulSoup
import requests

def readData(url):
    ## html data
    response = requests.get(url)
    ## parse the html data
    soup = BeautifulSoup(response.content, 'html.parser')
    f = open("data/data.txt", 'w', encoding="utf-8")
    f.write(Scrapper.name(soup))
    f.write(Scrapper.patentNum(soup))
    f.write(Scrapper.countryOrgin(soup))
    f.write(Scrapper.status(soup))
    f.write(Scrapper.founders(soup))
    f.close()
    
readData('https://patents.google.com/patent/JP6268657B2/en?q=(mechanic+drone)&oq=mechanic+drone')
