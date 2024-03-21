import requests
from bs4 import BeautifulSoup
from PIL import Image

def main():
    ## html data
    url = input("Enter Patent link: ")
    response = requests.get(url, auth = ('user', 'pass'), encoding = 'utf-8')
    ## parse the html data
    soup = BeautifulSoup(response.text, 'html.parser', encoding = 'utf-8')
    write(soup)


## soup text in external file
def write(soup):
    f = open("htmlData.txt", 'w', encoding = 'utf-8')
    f.write(soup.text)
    f.close()

## print the Patent number
def patentNum(soup):
    patentNum = soup.find('meta', attrs ={'name': 'citation_patent_number'})
    print("PatentNum : " + patentNum.get('content'))

## country of orgin
def countryOrgin(soup):
    country = soup.find('dd', attrs = {'itemprop': 'countryName'})
    print("Country of orgin : "  + country.text)


## print all the founders
def founders(soup):
    founders = soup.find_all('meta', attrs={'name': 'DC.contributor'})
    #<meta name="DC.contributor" content="Bartley K. Andre" scheme="inventor">
    print("Inventors: ")
    for founder in founders:
        if founder.get('scheme') == "inventor":
            name = founder.get('content')
            print(name)

        else:
            print("Current Company assignee: " + founder.get('content'))

