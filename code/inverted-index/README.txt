For compiling the java code:

--> javac -d . InvertedIndexDriver.java InvertedIndexMapper.java InvertedIndexReducer.java  

For creating the jar file:

--> jar cfm InvertedIndex.jar manifest.txt InvertedIndex/*.class

For starting the hadoop job:
1. Make sure that you store the dataset in the hdfs file system.

--> hdfs dfs -copyFromLocal  "dataset path" "hdfs path"
--> [FOR EXAMPLE]: hdfs dfs -copyFromLocal  /home/surya/Information-Retrieval/documents /

2. Start the hadoop job by running the jar file

--> hadoop jar InvertedIndex.jar "Input dataset path in hdfs" "Output path in hdfs"
--> [FOR EXAMPLE]: hadoop jar InvertedIndex.jar /documents /IR-output

3. Store the output of the hadoop map-reduce job in the output.txt file.

--> hdfs dfs -cat /{Output path in hdfs}/part-00000 >> Inverted-Index.txt

store this output.txt in the same level where this readme file is present

4. Now run the invertedindex.py file to convert the output.txt file into json