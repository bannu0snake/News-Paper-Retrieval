from bs4 import BeautifulSoup
from requests import get
import threading

genres = ["auto", "briefs", "business", "cryptocurrency", "city", "coronavirus", "education", "elections", "entertainment", 
          "gadgets-news", "health-survey", "home", "independence-day", "india", "international-yoga-day", 
          "politics", "sports", "travel", "viral-news", "world"]

def Crawler(urls, filename, type):
    headUrl = 'https://timesofindia.indiatimes.com'
    links_with_text = []
    for url in urls:
        url = str(url).replace("\n", "")
        print(url)
        soup = BeautifulSoup(get(url).text, 'lxml')
        if type == "A":
            links = [div.a for div in soup.findAll('div', attrs={'class' : 'brief_box'})]
        if type == "B":
            links = [li.a for li in soup.find('div', attrs={'class' : 'main-content'}).findAll('li')]
        if type == "D":
            links = [div.a for div in soup.findAll('div', attrs={'class' : 'md_news_box'})]
        if type == "E":
            links = [li.a for li in soup.find('ul', attrs={'class' : 'cvs_wdt'}).findAll('li')]
        if type == "F":
            links = [div.h3.a for div in soup.findAll('div', attrs={'class' : 'box1'}) if div.h3 != None ]
        for a in links:
            try:
                if "photostory" not in a['href'] and "photogallery" not in a['href'] and "video" not in a['href'] and ".cms" in a['href'] and "offbeat_stories" not in a['href']:
                    links_with_text.append(a['href'])
            except TypeError:
                print("Fake link!! Skipping it ...")

    with open(filename, 'w', encoding = 'utf8') as file:
        for i in links_with_text:
            if i[0] == "/":
                file.write(headUrl+i+"\n")
            else:
                file.write(i+"\n")

def start_crawling(indexs, type, thread):
    print("Thread "+thread+" Started ... !")
    print("This genre is of type "+type)
    for i in indexs:
        with open("genres/{theGenre}.txt".format(theGenre = genres[i]), encoding='utf8') as file:
            print("Started crawling "+genres[i]+"......")
            urls = file.readlines()
            Crawler(urls, "articles/{theGenre}.txt".format(theGenre = genres[i]), type)
        print("Finished crawling "+genres[i]+"...!" + " Launching next genre .....")

typeA = [1]
typeB1 = [0, 2] 
typeB2 = [3, 4] 
typeB3 = [5, 6] 
typeB4 = [7, 9] 
typeB5 = [11, 12] 
typeB6 = [13, 14] 
typeB7 = [15, 16] 
typeB8 = [18, 19]
typeD = [8]
typeE = [10]
typeF = [17]

t1 = threading.Thread(target=start_crawling, args=(typeA, "A", "t1"))
t2 = threading.Thread(target=start_crawling, args=(typeB1, "B", "t2"))
t3 = threading.Thread(target=start_crawling, args=(typeB2, "B", "t3"))
t4 = threading.Thread(target=start_crawling, args=(typeB3, "B", "t4"))
t5 = threading.Thread(target=start_crawling, args=(typeB4, "B", "t5"))
t6 = threading.Thread(target=start_crawling, args=(typeB5, "B", "t6"))
t7 = threading.Thread(target=start_crawling, args=(typeB6, "B", "t7"))
t8 = threading.Thread(target=start_crawling, args=(typeB7, "B", "t8"))
t9 = threading.Thread(target=start_crawling, args=(typeB8, "B", "t9"))
t10 = threading.Thread(target=start_crawling, args=(typeD, "D", "t10"))
t11 = threading.Thread(target=start_crawling, args=(typeE, "E", "t11"))
t12 = threading.Thread(target=start_crawling, args=(typeF, "F", "t12"))

t1.start()
t2.start()
t3.start()
t4.start()
t5.start()
t6.start()
t7.start()
t8.start()
t9.start()
t10.start()
t11.start()
t12.start()

t1.join()
t2.join()
t3.join()
t4.join()
t5.join()
t6.join()
t7.join()
t8.join()
t9.join()
t10.join()
t11.join()
t12.join()

print("Crawling completed ... !")