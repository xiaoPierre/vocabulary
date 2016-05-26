import requests
from bs4 import BeautifulSoup

def crawlImage(word):
    urlBase = 'http://lemoteur.orange.fr/?module=lemoteur&bhv=images&kw='
    url = urlBase + word
    page = requests.get(url)
    pageHTML = page.content.decode(page.encoding)
    soup = BeautifulSoup(pageHTML, 'lxml')
    image = soup.find('span', class_='imageElement')
    if image:
        adresseImage = image.find('img')['src']
        return adresseImage
    else:
        return ''

print(crawlImage('bite'))