import requests
from bs4 import BeautifulSoup
from PIL import Image

## soup text in external file
def write(soup, response):
    g = open('htmlData.txt', 'w', encoding = 'utf-8')
    g.write(soup.prettify())
    g.close()

## print the Patent number
def patentNum(soup):
    patentNum = soup.find('meta', attrs ={'name': 'citation_patent_number'})
    if patentNum:
        print("PatentNum : " + patentNum.get('content'))

## print country of orgin
def countryOrgin(soup):
    country = soup.find('dd', attrs = {'itemprop': 'countryName'})
    if country:
        print("Country of orgin : "  + country.text)


## print all the founders and asignee of the patent
def founders(soup):
    founders = soup.find_all('meta', attrs={'name': 'DC.contributor'})
    print("Inventors: ")
    # iterate over all inventors and print
    for founder in founders:
        if founder.get('scheme') == "inventor":
            name = founder.get('content')
            if name:
                print(name)
        else:
            # prints the company assignee once reached
            company = founder.get('content')
            if founder:
                print("Current Company assignee: " + company)

## name of patent
def name(soup):
    name = soup.find('span', attrs = {'itemprop' : 'title'})
    if name:
        print('Name: '+ name.string)

## status of the patent
def status(soup):
    ## find status
    status = soup.find('span', attrs = {'itemprop' : 'status'})
    if status:
        print('Status: ' + status.string)

##

def main():
    ## html data
    url = input("Enter Patent link: ")
    print(' ')
    response = requests.get(url)
    ## parse the html data
    soup = BeautifulSoup(response.content, 'html.parser')
    name(soup); patentNum(soup); countryOrgin(soup); status(soup); founders(soup);
main()