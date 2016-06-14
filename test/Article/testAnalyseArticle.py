from app.Article.analyseArticle import *
from app.Crawler.crawlArticle import *
art = crawlArticle('sante').content

def testAnalyseArticle():
    result = analyseArticle(art)
    print(result)

testAnalyseArticle()
