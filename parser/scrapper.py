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
        return ("PatentNum : " + patentNum.get('content') + "\n")
    return "PatentNum : None"

## print country of orgin
def countryOrgin(soup):
    country = soup.find('dd', attrs = {'itemprop': 'countryName'})
    if country:
        return ("Country of orgin : "  + country.text + "\n")
    return "Country of orgin : None"+ "\n"


## print all the founders and asignee of the patent
def founders(soup):
    founders = soup.find_all('meta', attrs={'name': 'DC.contributor'})
    result  = "Inventors:\n"
    # iterate over all inventors and print
    for founder in founders:
        if founder.get('scheme') == "inventor":
            name = founder.get('content')
            if name:
                result += (name+ "\n")
        else:
            # prints the company assignee once reached
            company = founder.get('content')
            if founder:
                result += ("Current Company assignee: " + company + "\n")

    return result

## name of patent
def name(soup):
    name = soup.find('span', attrs = {'itemprop' : 'title'})
    if name:
        return ('Name: '+ name.string+ "\n")
    return "Name: None"+ "\n"

## status of the patent
def status(soup):
    ## find status
    status = soup.find('span', attrs = {'itemprop' : 'status'})
    if status:
        return ('Status: ' + status.string + "\n")
    return "Status: None"+ "\n"

##

def main():
    ## html data
    url = input("Enter Patent link: ")
    print(' ')
    response = requests.get(url)
    ## parse the html data
    soup = BeautifulSoup(response.content, 'html.parser')
    f = open("data/data.txt", 'w', encoding="utf-8")
    f.write(name(soup))
    f.write(patentNum(soup))
    f.write(countryOrgin(soup))
    f.write(status(soup))
    f.write(founders(soup))
    f.close()
main()