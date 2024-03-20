import requests
from bs4 import BeautifulSoup
from PIL import Image

## html data
url = input("Enter Patent link: ")
response = requests.get(url, auth = ('user', 'pass'))
## parse the html data
soup = BeautifulSoup(response.text, 'html.parser')
## text data
text_data = soup.get_text()
print()

## print html data into seperate file for examination
f = open("htmlData.txt", 'w')
f.write(response.text)
f.close()


## print the Patent number
## <meta name="citation_patent_number" content="US:D618677:S1">
patentNum = soup.find('meta', attrs ={'name': 'citation_patent_number'})
print("PatentNum : " + patentNum.get('content'))

## country of orgin
## <dd itemprop="countryName">United States</dd>
country = soup.find('dd', attrs = {'itemprop': 'countryName'})
print("Country of orgin : "  + country.text)

## patent display
## <meta name="citation_pdf_url" content="https://patentimages.storage.googleapis.com/9d/51/c7/a3227ec100304d/USD618677.pdf">
## imageLink = soup.find('meta', attrs = {'name' : 'citation_pdf_url'}).get('content')
## image = Image.open(imageLink)
## image.show()

## print all the founders
founders = soup.find_all('meta', attrs={'name': 'DC.contributor'})
#<meta name="DC.contributor" content="Bartley K. Andre" scheme="inventor">
print("Inventors: ")
for founder in founders:
    if founder.get('scheme') == "inventor":
        name = founder.get('content')
        print(name)

    else:
        print("Current Company assignee: " + founder.get('content'))

