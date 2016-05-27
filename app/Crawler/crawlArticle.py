import requests
from bs4 import BeautifulSoup

# TODO purifier l'article ramassée
themes = ['international', 'politique', 'societe',
         'economie', 'culture', 'idees', 'planete',
         'sport', 'sciences', 'campus']

urlBase = 'http://www.lemonde.fr/'

class Article:
    def __init__(self, title, content, author):
        self.title = title
        self.content = content
        self.author = author
    def __str__(self):
        strRes = self.title + '\n'
        strRes += self.author + '\n'
        strRes += self.content
        return strRes


def crawlArticle(theme):
    assert(theme in themes)
    url = urlBase + theme
    page = requests.get(url)
    pageHTML = page.content.decode(page.encoding)
    soup = BeautifulSoup(pageHTML, 'lxml')
    laUne = soup.find('article', class_='titre_une')
    articlePage = laUne.find('a')
    articleURL = 'http://www.lemonde.fr' + articlePage['href']
    pageArticle = requests.get(articleURL)
    pageArticleHTML = pageArticle.content.decode(pageArticle.encoding)
    soupArticle = BeautifulSoup(pageArticleHTML, 'lxml')
    article = soupArticle.find('article', class_='article')
    title = article.find('h1', itemprop='Headline').text
    author = article.find('span', itemprop='author').text
    content = article.find('div', id='articleBody').text
    return Article(title, content, author)


print(crawlArticle('economie'))


