from app.Crawler.crawlImage import *

words2 = ['généraliste', 'partout', 'nombre', 'médecin', 'généraliste', 'baisse', 'presque', 'partout']


def testCrawlImage():
    for word in words2:
        print(crawlImage(word))

testCrawlImage()