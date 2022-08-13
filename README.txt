Title: News Document Retrieval

About the Project:

News Document Retrieval is an IR system where the main focus of this search engine is to collect news over 30,000 
documents that are relevant to the query entered by the user.

We crawled the data from (Times of India) and (The Hindu) around 30,000 documents creating the crawler 
in python from scratch.

Components:

1. Indexing the whole dataset using hadoop map-reduce.
2. Searching the query entered by the user with the help of Inverted index.
3. Ranking the retrieved documents accordingly
4. Taking the relevance feedback from the user for the top 20 retrieved documents.
5. Evaluating the documents from the retrieved ones using evaluation components and procedures.

Drive Link:- https://drive.google.com/drive/folders/1EgQET4TEqhOeasF6yZfZEjJKlaGIgsFf?usp=sharing

How to run our IR-system.

Step-1:-
We have shared the google drive link for the dataset and the inverted-index.json files. Install both the dataset and
the Inverted-index.json into the "code" folder.

Step-2:-
1. Run the main.py file and enter the queries and the query numbers. Please note that always start the query numbers 
   with 1
2. For each query, the program will output the results by ranking the documents accordingly.
3. After the results are shown, the program will ask the user which documents are relevant and which are not.
4. User needs to submit this feedback so that the results from the next query will be improved.
5. relevance.json and ranked_retrieved.json files will be generated after exiting this programme.

Step-3:-
1. Run the evaluation.py file to generate the PR-curves and evaluation metrics for the queries searched in 
   the step-4.


Brief Description of functionalities:

Crawling the Data and Indexing the dataset - SURYA TEJA TANGIRALA
-> A python crawler to crawl the data from the news article websites.
-> After crawling the data, we prepare the data for a hadoop map-reduce job.
-> We setup the hadoop map-reduce environment and move our dataset to the local hdfs.
-> We then write our inverted-index code in java and create the jar file.
-> We then run the jar file using hadoop and start a map-reduce job.
-> After the job is done the result will be in a text file. We then convert that text file into a json file
   so that it is easy to access the indexes and postings in the querying part.

Ranked Retrieval - Mahaboob Shaik
-> After running the main.py file you will be asked to enter the query. after entering the query you will get 
   the following results in the output
      1. all retrieved documents
      2. tf-weight, IDF-weight, Tf-Idf-weight for both query and each document and then norm weights 
         and finally cosine score for each document
      3. ranks each documents for the retrieved documents to the given query.
-> if you are done with querying "exit 0" to exit.
-> First take the user input for query and then procces the query to form query index
-> from inverted index fetch the words posting list which are in the query index
-> merge all the posting list to get all asumed relevant documents Ids
-> after finding all the document Ids iterate over every document to term frequency (TF) of each document
-> find the term frequency of the query of the for the respective document ID.
-> itereatively calculated Document frequency for all the words in the document, calculated tf of document and 
   query
-> so to calculate cosine score calculated tf-weight, IDF-weight tf-IDF-weight for document and query.
   used log to normalize weights
-> after finding tf-idf-weights are normalized  using L2 norm. and then calculated cosine score. 
-> after calculating cosine score , we ranked all retrieved docume based on cosine score and I have send 
   them to relevance feedback part for evaluation of IR system.

Evaluation Components - PRATHYUSH SIRIMALLE
-> The outputs from ranked_retrieved.json and relevance.json are taken as input to the evaluation.
-> For each query from the input the precision, recall, F1 score, average precision and Mean average precison are 
   calculated.
-> Precision is calculated as relevant-retrieved/retrieved and recall is calculated as relavant-retrieved/total 
   relevant.
-> F1 score is calculated as 2*precision*recall/precision+recall 
-> The precision-recall curve for each query is drawn.


Run ranked_retrival.py file, for each retrieved document  - SRI PRANAV YINTI
checked whether the retrieved document is relevant or not(checked for some queries).