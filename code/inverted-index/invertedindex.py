import json
ii = {}
with open("Inverted-Index.txt", encoding='utf8') as file:
    indexes = file.readlines()
    for index in indexes:
        arr = []
        for i in index.split(" "):
            i = i.replace("\t", "")
            i = i.replace("\n", "")
            arr.append(i)

        postings = []
        i = 1
        while i != len(arr):
            post = {"doc": arr[i], "freq": arr[i+1]}
            postings.append(post)
            i = i + 2
        ii[arr[0]] = {"postings": postings}
    

with open('Inverted-Index.json', 'w', encoding='utf8') as file:
    data = json.dumps(ii, indent=4)
    file.write(data)
