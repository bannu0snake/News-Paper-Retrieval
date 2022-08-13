from newspaper import Article
from newspaper import Config
import threading



user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:78.0) Gecko/20100101 Firefox/78.0'

config = Config()
config.browser_user_agent = user_agent
config.request_timeout = 10
drafts = []


def Scrapper(text_indexes, counter, thread, doc_cnt):
    print("Thread "+thread+" Started ... !")
    for i in text_indexes:
        with open("hinduarticles/link{ind}.txt".format(ind=i+1), encoding='utf8') as file:
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
                    

t1 = threading.Thread(target=Scrapper, args=([0,1,2,3],14112, "1", 0))
t2 = threading.Thread(target=Scrapper, args=([4,5,6,7], 14953, "2", 0))
t3 = threading.Thread(target=Scrapper, args=([8,9,10,11], 15794, "3", 0))
t4 = threading.Thread(target=Scrapper, args=([12,13,14,15], 16635, "4", 0))
t5 = threading.Thread(target=Scrapper, args=([16,17,18,19], 17476, "5", 0))
t6 = threading.Thread(target=Scrapper, args=([20,21,22,23], 18317, "6", 0))
t7 = threading.Thread(target=Scrapper, args=([24,25,26,27], 19158, "7", 0))
t8 = threading.Thread(target=Scrapper, args=([28,29,30,31], 19999, "8", 0))
t9 = threading.Thread(target=Scrapper, args=([32,33,34,35], 20770, "9", 0))
t10 = threading.Thread(target=Scrapper, args=([36,37,38,39], 21641, "10", 0))
t11 = threading.Thread(target=Scrapper, args=([40,41,42,43], 22527, "11", 0))
t12 = threading.Thread(target=Scrapper, args=([44,45,46,47], 23368, "12", 0))
t13 = threading.Thread(target=Scrapper, args=([48,49,50,51], 24209, "13", 0))
t14 = threading.Thread(target=Scrapper, args=([52,53,54,55], 25050, "14", 0))
t15 = threading.Thread(target=Scrapper, args=([56,57,58,59], 25891, "15", 0))
t16 = threading.Thread(target=Scrapper, args=([60,61,62,63], 26732, "16", 0))
t17 = threading.Thread(target=Scrapper, args=([64,65,66,67], 27573, "17", 0))
t18 = threading.Thread(target=Scrapper, args=([68,69,70,71], 28414, "18", 0))
t19 = threading.Thread(target=Scrapper, args=([72], 29255, "19", 0))


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


with open("failed_links.txt", "w", encoding='utf8') as file:
    for link in drafts:
        file.write(link+"\n")

