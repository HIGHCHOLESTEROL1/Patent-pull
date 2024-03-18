import requests
from bs4 import BeautifulSoup

## html data
iphoneUrl = 'https://patents.google.com/patent/USD618677S1/en'
response = requests.get(iphoneUrl)
## parse the html data
soup = BeautifulSoup(response.text, 'html.parser')

## print all the founders
founders = soup.find_all('meta', attrs={'name': 'DC.contributor'})
for founder in founders:
    name = founder.get('content')
    print(name)
#<meta name="DC.contributor" content="Bartley K. Andre" scheme="inventor">