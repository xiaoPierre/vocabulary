import requests
from app.Model.Article import *
from bs4 import BeautifulSoup
import random

themes = ['monde', 'politique', 'societe',
         'sante', 'cinema', 'people', 'television',
         'medias', 'culture', 'web', 'livres',
         'economie']

urlBase = 'http://www.20minutes.fr/'




def crawlArticle(theme):
    assert(theme in themes)
    url = urlBase + theme
    page = requests.get(url)
    pageHTML = page.content.decode(page.encoding)
    soup = BeautifulSoup(pageHTML, 'lxml')
    articleURL = urlBase[0:-1] + soup.find('section', class_='row').find('article').find('a')['href']
    pageArticle = requests.get(articleURL)
    pageArticleHTML = pageArticle.content.decode(pageArticle.encoding)
    soupArticle = BeautifulSoup(pageArticleHTML, 'lxml')
    article = soupArticle.find('div', class_='article')
    title = article.find('h1', itemprop='headline').text
    summary = article.find('span', class_='hat-summary').text
    contentBlocks = article.find('div', itemprop='articleBody').find_all('p')
    content = ''
    for item in contentBlocks:
        content += item.text.strip()
    return Article(title, content, summary)

def crawlRandomArticle():
    theme = random.choice(themes)
    return crawlArticle(theme)

