from bs4 import BeautifulSoup
from requests import get


def hinduarticles(url,filename):
    page_number=1
    headUrl="https://www.thehindu.com/"
    
    for x in range(1,6):
        Url = url + '?page='+ str(x)
        
        print(Url)
        soup = BeautifulSoup(get(Url).text, 'lxml')
        
        match_links=[]
        with open(filename,'a',encoding='utf8') as file:
            links = [div for div in soup.findAll('div', attrs={'class':'Other-StoryCard'})]
            # print(links)
            for div in links:
                Div = [div for div in div.findAll('h3')]
                for h in Div:
                    match_links.append(h.a['href'])
            
            
            
            # print(match_links, "\n")
            for i in match_links:
                # print(i, sep = "\n")
                file.write(i+"\n")
    
    



with open('sitemaps.txt', encoding = 'utf8') as file:
    counter = 1
    for url in file:
        # print(url.strip())
        hinduarticles(url.strip(), 'hinduarticles/link'+str(counter)+".txt")
        counter = counter + 1