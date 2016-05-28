import requests
from bs4 import BeautifulSoup

# TODO purifier l'article ramassée
themes = ['monde', 'politique', 'societe',
         'sante', 'cinema', 'people', 'television',
         'medias', 'culture', 'web', 'livres',
         'style', 'economie', 'sport']

urlBase = 'http://www.20minutes.fr/'

class Article:
    def __init__(self, title, content, summary):
        self.title = title
        self.content = content
        self.summary = summary
    def __str__(self):
        strRes = self.title + '\n'
        strRes += self.summary + '\n'
        strRes += self.content
        return strRes


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
        content += item.text + '\n'
    return Article(title, content, summary)

print(crawlArticle('people'))


