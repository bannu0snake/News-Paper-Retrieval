from os import link
from bs4 import BeautifulSoup
from requests import get

def domains(url, filename):
    headUrl="https://www.thehindu.com/"
    soup = BeautifulSoup(get(url).text, 'lxml')
    
    with open(filename, 'w', encoding='utf8') as file:
        site_maps=[]
        
        
        links = [ul for ul in soup.findAll('ul', attrs={'class':'sub-menu'})]
        # print(links)
        for ul in links:
            Li = [li for li in ul.findAll('li')]
            for li in Li:
                site_maps.append(li.a['href'])
        
        for i in site_maps:
            file.write(i+"\n")
            
domains("https://www.thehindu.com/", "sitemaps.txt")
                    