from app.Crawler.crawlArticle import *

themes = ['monde', 'politique', 'societe',
          'sante', 'cinema', 'people', 'television',
          'medias', 'culture', 'web', 'livres',
          'economie']

def testCrawlArticle():
    for theme in themes:
        print(theme)
        print(crawlArticle(theme))


testCrawlArticle()
