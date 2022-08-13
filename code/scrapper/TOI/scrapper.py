from newspaper import Article
from newspaper import Config
import threading

genres = ["auto", "briefs", "business","city", "coronavirus", "cryptocurrency" , "education", "elections", "entertainment", 
          "gadgets-news", "health-survey", "home", "independence-day", "india", "international-yoga-day", 
          "politics", "sports", "travel", "viral-news", "world"]

user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:78.0) Gecko/20100101 Firefox/78.0'

config = Config()
config.browser_user_agent = user_agent
config.request_timeout = 10
drafts = []

def Scrapper(genre, counter, thread, doc_cnt):
    print("Thread "+thread+" Started ... !")
    with open("articles/{file}.txt".format(file=genre), encoding='utf8') as file:
        links = file.readlines()
        for url in links:
            try:
                url = url.replace("\n", "")
                toi_article = Article(url, language="en", config=config)
                toi_article.download()
                toi_article.parse()
                title = toi_article.title
                content = toi_article.text
                with open("documents/{cnt}.txt".format(cnt=counter), "w", encoding='utf8') as doc:
                    doc.write(title + "\n" + content)
                print("Article {cnt}.txt scrapped sucessfully in thread t{t}".format(cnt = counter, t=thread))
                counter = counter + 1
                doc_cnt = doc_cnt + 1
                print("Total number of documents scrapped till now in thread t{t}: {c}".format(t=thread, c=doc_cnt))
            except:
                print("Scrapping "+url+" failed! Saving this link as draft")
                drafts.append(url)

t1 = threading.Thread(target=Scrapper, args=(genres[0], 1, "1", 0))
t2 = threading.Thread(target=Scrapper, args=(genres[1], 912, "2", 0))
t3 = threading.Thread(target=Scrapper, args=(genres[2], 1289, "3", 0))
t4 = threading.Thread(target=Scrapper, args=(genres[3], 1848, "4", 0))
t5 = threading.Thread(target=Scrapper, args=(genres[4], 6495, "5", 0))
t6 = threading.Thread(target=Scrapper, args=(genres[5], 6988, "6", 0))
t7 = threading.Thread(target=Scrapper, args=(genres[6], 7309, "7", 0))
t8 = threading.Thread(target=Scrapper, args=(genres[7], 7496, "8", 0))
t9 = threading.Thread(target=Scrapper, args=(genres[8], 7854, "9", 0))
t10 = threading.Thread(target=Scrapper, args=(genres[9], 9310, "10", 0))
t11 = threading.Thread(target=Scrapper, args=(genres[10], 9360, "11", 0))
t12 = threading.Thread(target=Scrapper, args=(genres[11], 9389, "12", 0))
t13 = threading.Thread(target=Scrapper, args=(genres[12], 9539, "13", 0))
t14 = threading.Thread(target=Scrapper, args=(genres[13], 9676, "14", 0))
t15 = threading.Thread(target=Scrapper, args=(genres[14], 11827, "15", 0))
t16 = threading.Thread(target=Scrapper, args=(genres[15], 11869, "16", 0))
t17 = threading.Thread(target=Scrapper, args=(genres[16], 11969, "17", 0))
t18 = threading.Thread(target=Scrapper, args=(genres[17], 12948, "18", 0))
t19 = threading.Thread(target=Scrapper, args=(genres[18], 13197, "19", 0))
t20 = threading.Thread(target=Scrapper, args=(genres[19], 13642, "20", 0))

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
t13.start()
t14.start()
t15.start()
t16.start()
t17.start()
t18.start()
t19.start()
t20.start()

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
t13.join()
t14.join()
t15.join()
t16.join()
t17.join()
t18.join()
t19.join()
t20.join()

with open("failed_links.txt", "w", encoding='utf8') as file:
    for link in drafts:
        file.write(link+"\n")

