organisedLinks = {}

def organiseGenres(link):
    newlink = str(link).replace("https://timesofindia.indiatimes.com/", "")
    newlink = str(newlink).replace("\n", "")
    genre = ""
    for i in newlink:
        if i == "/":
            break
        else:
            genre = genre + i
    if genre not in organisedLinks.keys():
        organisedLinks[genre] = []
        organisedLinks[genre].append(link)
    else:
        organisedLinks[genre].append(link)
    

with open("sitemaps.txt", encoding = 'utf8') as file:
    for link in file.readlines():
        organiseGenres(link)

for i in organisedLinks:
    with open("genres/{filename}.txt".format(filename=i), 'w', encoding='utf8') as file:
        for link in organisedLinks[i]:
            file.write(link)