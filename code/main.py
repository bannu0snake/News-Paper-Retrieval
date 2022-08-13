import math
import json
import itertools
import re
class RankedRetrival:
    def query_indexing(self,query):
        q_words = query.split(" ")
        tf = {}
        for i in q_words:
            if i not in tf:
                tf[i] = 1
            else:
                tf[i] += 1
        return tf
    def tf_wt(self, tf):
        print(tf)
        tf_wt_dict = {}
        for i in tf:
            if tf[i] != 0:
                tf_wt_dict[i] = 1 + round(math.log10(tf[i]), 4)
            else:
                 tf_wt_dict[i] = 0
        return tf_wt_dict
    def extract_doc_freq(self, doc_freq, tf):
        query_doc_freq = {}
        for i in tf:
            if i in doc_freq:
                query_doc_freq[i] = doc_freq[i]
        return query_doc_freq
    def calc_IDF(self, doc_freq, N):
        idf_dict = {}
        for i in doc_freq:
            idf_dict[i] =1 + round(math.log10(N/doc_freq[i]),4 )  
        return idf_dict  
    def l2_norm(self, vals):
        l2 = 0
        for i in vals:
            l2 +=  vals[i]**2
        l2 = math.sqrt(l2)
        norm_vals = {}
        for i in vals:
            norm_vals[i] = round(vals[i]/l2, 4)
        return norm_vals
    def tf_idf_calc(self, tf, idf):
        tf_idf = {}
        for i in tf:
            tf_idf[i] = tf[i]*idf[i]
        return tf_idf
    def cosine_score(self, doc_score, query_score):
        score = 0
        for i in doc_score:
            score += doc_score[i]*query_score[i]
        return score
    def compute_tf_idf(self,tf, doc_freq, N):
        tf_wt_dict = self.tf_wt(tf)
        print("tf-weight",tf_wt_dict)
        query_doc_freq = self.extract_doc_freq(doc_freq,tf)
        print("doc freqency",query_doc_freq)
        idf_dict = self.calc_IDF(query_doc_freq,N)
        print("idf-weight",idf_dict)
        tf_idf = self.tf_idf_calc(tf_wt_dict, idf_dict)
        print("tf-idf-weight",tf_idf)
        tf_idf_norm = self.l2_norm(tf_idf)
        print("tf_idf-weight",tf_idf_norm)
        return tf_idf_norm


ranked_retrieval = RankedRetrival()

N = 29380
print("connecting to database, please wait.....")
f = open('Inverted-Index.json')
data = json.load(f)
f.close()
query = ""
while query != "exit 0":
    query = ""
    query_postings = {}
    if query == "":
        query = input("please enter your query : ")
        if query == "exit 0":
            break
    query_number = input("please enter the query number: ")

    q = query.lower()
    q_tf = ranked_retrieval.query_indexing(q)
    print(q_tf)
    for word in q_tf:
        try:
            query_postings[word] = data[word]
        except:
            print(word, " not in the inverted index, please check the spelling")
        
    f.close()
    iquery_tf ={}
    for word in query_postings:
        iquery_tf[word] = q_tf[word]
        

    print("query posting list : ")
    print(query_postings)

    merged_lists = []
    for word in query_postings:
        for i in query_postings[word]['postings']:
            if i["doc"] not in merged_lists:
                merged_lists.append(i["doc"])
    print("merged posting list : ",merged_lists)     

    docs_tf = {}
    for doc in merged_lists:
        doc_tf  = {}
        f = open("documents/"+doc, encoding="utf8")
        lines = f.read()
        c = re.sub('([^a-zA-Z0-9+])', " ", lines)
        f.close()
        idoc_tf = ranked_retrieval.query_indexing(c.lower())
        for word in idoc_tf:
            if word in data:
                doc_tf[word] = idoc_tf[word]
        docs_tf[doc] = doc_tf
    cosine_scores = {}
    for doc in merged_lists:
        print()
        print(doc)
        query_tf = {}
        for word in docs_tf[doc]:
            if word in iquery_tf:
                query_tf[word] = iquery_tf[word]
            else:
                query_tf[word] = 0
        doc_freq = {}
        for word in query_tf:
            sum = 0
            for i in data[word]['postings']:
                sum += int(i["freq"])
            doc_freq[word] = sum
        # print(doc_freq)
        tf_idf_query = ranked_retrieval.compute_tf_idf(query_tf, doc_freq, N)
        tf_idf_doc = ranked_retrieval.compute_tf_idf(docs_tf[doc], doc_freq, N)

        print(tf_idf_query,tf_idf_doc)
        cosine_score = ranked_retrieval.cosine_score(tf_idf_doc, tf_idf_query)
        print("cosine score",cosine_score)
        cosine_scores[doc] = cosine_score
        
    ranked_docs = {}

    ranked_docs = {k: v for k, v in sorted(cosine_scores.items(), key=lambda item: item[1])}
    final_ranked_docs = {}


    rank = 0
    for i in reversed(ranked_docs):
        doc = {}
        rank += 1
        doc["score"] = cosine_scores[i]
        doc["rank"] = rank
        final_ranked_docs[i] = doc
    print()
    print("final ranked documents") 
    for i in final_ranked_docs:
        print(i, final_ranked_docs[i])
        
    sample = {}
    try:
        sample = dict(itertools.islice(final_ranked_docs.items(), 20)) 
    except:
        sample = dict(itertools.islice(final_ranked_docs.items(), 10)) 
    
    # Writing to sample.json
    ret = {}
    if query_number != "1":
        with open("ranked_retrieved.json") as infile:
            ret = json.load(infile)
            ret[query_number] = sample
            ret = json.dumps(ret, indent=4)
        with open("ranked_retrieved.json", "w") as outfile:
            outfile.write(ret)
    else:
        with open("ranked_retrieved.json", "w") as outfile:
            ret[query_number] = sample
            outfile.write(json.dumps(ret, indent=4))
            

    # Relevance Feedback

    relevant_docs = {}
    if query_number != "1":
        with open("relevance.json") as infile:
            relevant_docs = json.load(infile)
    else:
        relevant_docs = {}

    relevant_list = []
    for i in sample:
        relevance = int(input("Is {doc} relevant to your query? if yes type 1, if no type 0: ".format(doc = i)))
        if relevance == 1:
            relevant_list.append(i)

    relevant_docs[query_number] = relevant_list

    with open("relevance.json", "w") as outfile:
        relevant = json.dumps(relevant_docs, indent=4)
        outfile.write(relevant) 
    