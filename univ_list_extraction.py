from bs4 import BeautifulSoup
import urllib2
url='http://colleges.usnews.rankingsandreviews.com/best-colleges/sitemap'
page = urllib2.urlopen(url)
soup=BeautifulSoup(page.read())
#print soup
#print(soup.get_text())

p_tags=soup.find_all('a')
print p_tags
