from bs4 import BeautifulSoup
from requests import get

def sitemapscrawler(url, filename):
    headUrl = 'https://timesofindia.indiatimes.com'
    soup = BeautifulSoup(get(url).text, 'lxml')

    with open(filename, 'w', encoding = 'utf8') as file:
        links_with_text = []
        productLinks = [li for li in soup.findAll('li', attrs={'class' : 'grid'})]
        for li in productLinks:
            for ul in li:
                # print(ul)
                for li2 in ul:
                    for a in li2:
                        # print(a)
                        try:
                            if ".cms" not in a['href'] and "/videos/" not in a['href'] and a['href'] != "" and a['href'][0] == "/":
                                links_with_text.append(headUrl + a['href'])
                        except TypeError:
                            print("Type error occured")
                        except KeyError:
                            print("Key error occured")

        for i in links_with_text:
            file.write(i+"\n")

sitemapscrawler("https://timesofindia.indiatimes.com/sitemap.cms", "sitemaps.txt")